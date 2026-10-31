#!/usr/bin/env python3
"""Check repository layout only; does not validate CAD geometry or screenshot truth."""
import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LEGACY = {
    "fc-enclosure": "model.f3d",
    "esp32-c3-supermini": "model.stl",
    "bh1750-gy302": "model.step",
}
IMAGES = {"assembly.png", "three-view.png", "exploded.png"}

def check(root, release=None):
    errors = []
    models = root / "models"
    if not models.is_dir():
        return ["models/ missing"]
    dirs = sorted(p for p in models.iterdir() if p.is_dir())
    if release and release not in {p.name for p in dirs}:
        errors.append("Unknown release model: " + release)
    for p in models.iterdir():
        if not p.is_dir():
            errors.append("Unexpected file in models/: " + p.name)
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
            allowed = rel == "README.md" or rel in allowed_sources or rel in {"images/" + i for i in IMAGES}
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
