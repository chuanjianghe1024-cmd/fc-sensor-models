#!/usr/bin/env python3
"""Check repository layout only; does not validate CAD geometry or screenshot truth."""
import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LEGACY = {"fc-enclosure": "model.f3d"}
RESERVED = {"assets", "tools", "generated", "__pycache__"}
IMAGES = {"assembly.png", "three-view.png", "exploded.png"}

def check(root, release=None):
    errors = []
    dirs = sorted(p for p in root.iterdir()
                  if p.is_dir() and not p.name.startswith(".") and p.name not in RESERVED)
    if not dirs:
        errors.append("No model projects found at repository root")
    if release and release not in {p.name for p in dirs}:
        errors.append("Unknown release model: " + release)
    assets = root / "assets"
    if not (assets / "README.md").is_file():
        errors.append("assets/README.md missing")
    if assets.is_dir():
        for asset in assets.iterdir():
            if not asset.is_dir():
                if asset.name != "README.md":
                    errors.append("Unexpected assets file: " + asset.name)
                continue
            sources = [p for p in asset.iterdir() if p.is_file() and p.name in
                       {"model.stl", "model.step", "model.f3d", "model.f3z"}]
            if len(sources) != 1 or any(p.stat().st_size == 0 for p in sources):
                errors.append(asset.name + ": require one nonempty shared reference model")
            if not (asset / "README.md").is_file():
                errors.append(asset.name + ": shared reference README missing")
    for model in dirs:
        name = model.name
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(name + ": use stable lowercase kebab-case directory")
        required = release == name or name not in LEGACY
        allowed_sources = {"model.f3d", "model.f3z"}
        if not required and name in LEGACY:
            allowed_sources.add(LEGACY[name])
        sources = [p for p in model.iterdir() if p.name in allowed_sources and p.is_file()]
        if len(sources) != 1:
            errors.append(name + ": require exactly one authoritative model")
        for p in model.rglob("*"):
            if not p.is_file():
                continue
            rel = p.relative_to(model).as_posix()
            if rel.startswith(("generated/", "__pycache__/")):
                continue
            allowed = rel in {"README.md", "WIRING.md", "ASSEMBLY.md"} or rel in allowed_sources or rel in {"images/" + i for i in IMAGES} or (rel.startswith("docs/") and p.suffix.lower() in {".md", ".png", ".jpg", ".jpeg", ".svg", ".pdf"})
            if not allowed:
                errors.append(name + ": unexpected tracked-layout file " + rel)
            elif p.stat().st_size == 0:
                errors.append(name + ": empty file " + rel)
        readme = model / "README.md"
        if not readme.is_file():
            errors.append(name + ": README.md missing")
            continue
        text = readme.read_text(encoding="utf-8")
        for field in ("Version", "Tag"):
            if not re.search(r"^" + field + r": .+$", text, re.M):
                errors.append(name + ": missing " + field)
        for link in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
            if not link.startswith(("https://", "http://")) and not (model / link).is_file():
                errors.append(name + ": broken image link " + link)
        if required:
            version = re.search(r"^Version: (v\d+\.\d+\.\d+)$", text, re.M)
            tag = re.search(r"^Tag: (.+)$", text, re.M)
            if not version or not tag or tag.group(1) != name + "/" + version.group(1):
                errors.append(name + ": release Version/Tag must match model-id/vX.Y.Z")
            for image in ("three-view.png", "exploded.png"):
                if not (model / "images" / image).is_file():
                    errors.append(name + ": release image missing: " + image)
    home = root / "README.md"
    if not home.is_file():
        errors.append("Root showcase README missing")
    else:
        home_text = home.read_text(encoding="utf-8")
        for model in dirs:
            if model.name + "/" not in home_text:
                errors.append(model.name + ": missing root showcase entry")
            if release == model.name and not re.search(
                r"!\[[^\]]*\]\(" + re.escape(model.name + "/images/three-view.png") + r"\)", home_text):
                errors.append(model.name + ": root showcase must embed latest three-view.png")
    for doc in root.rglob("*.md"):
        if any(part.startswith(".") or part in {"generated", "__pycache__"} for part in doc.relative_to(root).parts):
            continue
        for link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link) or link.startswith("#"):
                continue
            target = link.split("#", 1)[0]
            if target and not (doc.parent / target).exists():
                errors.append(str(doc.relative_to(root)) + ": broken local link " + link)
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release", metavar="MODEL_ID")
    args = parser.parse_args()
    errors = check(ROOT, args.release)
    if errors:
        print("\n".join("ERROR: " + e for e in errors))
        return 1
    print("Layout OK. CAD geometry, screenshot accuracy and physical fit require separate verification.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
