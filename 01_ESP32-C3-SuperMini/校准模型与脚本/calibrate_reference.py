"""Calibrate the user's imported mesh as an enclosure reference (mm).
Not a manufacturing model. Component positions not measured remain illustrative.
"""
from pathlib import Path
import sys, json, hashlib
deps=Path(__file__).resolve().parents[3]/'hardware-tools'/'caddeps'
if deps.is_dir(): sys.path.insert(0,str(deps))
import numpy as np
import trimesh

out = Path(__file__).resolve().parent
source = Path(__file__).resolve().parent.parent/'原始下载模型'/'esp32c3supermini.stl'
m = trimesh.load(source, force='mesh')
v = m.vertices.copy()
# Source USB and PCB are a single connected, watertight mesh.
# Identify the connector's surface, including its shared PCB contact vertices.
usb = ((v[:,0] <= 5.90001) & (v[:,1] >= 4.5538) &
       (v[:,1] <= 13.4462) & (v[:,2] >= .99999))
uv = v[usb].copy()
assert np.allclose(uv.min(0), [-1.4, 4.55384636, 1], atol=1e-4)
assert np.allclose(uv.max(0), [5.9, 13.44615364, 4.3], atol=1e-4)
v[:,0] *= 22.5 / 22.799999237060547
v[:,1] *= 17.8 / 18
# Keep connector length, shift its front to 1 mm ahead of the PCB.
v[usb,0] = uv[:,0] + .4
v[usb,1] = (uv[:,1]-9) * 8.8 / (uv[:,1].max()-uv[:,1].min()) + 8.9
v[usb,2] = 1 + (uv[:,2]-1) * 3.1 / (uv[:,2].max()-1)
m.vertices = v
assert m.is_watertight and m.is_winding_consistent
assert m.volume > 0
assert np.allclose(m.extents, [23.5,17.8,4.1], atol=1e-5)
pcb = v[v[:,2] < 1e-5]
assert np.allclose(np.ptp(pcb,axis=0)[:2], [22.5,17.8], atol=1e-5)
assert np.allclose(np.ptp(v[usb],axis=0)[1:], [8.8,3.1], atol=1e-5)
dest = out/'C3-SuperMini-calibrated-mm.stl'
m.export(dest)
check = trimesh.load(dest, force='mesh')
assert check.is_watertight and np.allclose(check.extents,[23.5,17.8,4.1],atol=1e-5)
report = dict(source=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
    pcb_mm=[22.5,17.8],usb_overhang_mm=1,usb_cross_section_mm=[8.8,3.1],
    full_model_mm=check.extents.tolist(),watertight=bool(check.is_watertight),
    faces=len(check.faces),board_thickness_mm=1,
    limitations=['PCB thickness 1 mm retained from source, not measured.',
    'Other component shapes and positions remain approximate source geometry.',
    'Soldered BH1750 assembly envelope 20 x 27 x 8.8 mm is separate.',
    'No previous enclosure reused.'])
(out/'calibration.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
