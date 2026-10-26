"""Photo-derived BH1750/GY-302 assembly reference, dimensions in millimetres."""
from pathlib import Path
import sys,json,math
deps=Path(__file__).resolve().parents[3]/'hardware-tools'/'caddeps'
if deps.is_dir(): sys.path.insert(0,str(deps))
import cadquery as cq
import numpy as np
OUT=Path(__file__).resolve().parent
W,L,T,H=14.2,18.5,1.1,2.0
holes=[(2.48,2.58),(11.61,2.51)]
pins=[(1.92,17.43),(4.53,17.42),(7.15,17.47),(9.83,17.43),(12.45,17.42)]
parts=[]
assy=cq.Assembly(name='BH1750_GY302_photo_reference_mm')
def add(name,shape,color):
    shape=shape.val() if isinstance(shape,cq.Workplane) else shape
    assert shape.isValid(),name
    assy.add(shape,name=name,color=cq.Color(*color))
    parts.append((name,shape,color))
def box(x,y,w,l,z,h):
    return cq.Workplane('XY').box(w,l,h,centered=(True,True,False)).translate((x,y,z))
def ring(x,y,outer,inner,z,h):
    return cq.Workplane('XY').center(x,y).circle(outer/2).circle(inner/2).extrude(h).translate((0,0,z))
pcb=box(W/2,L/2,W,L,0,T)
for x,y in holes:
    pcb=pcb.cut(cq.Workplane('XY').center(x,y).circle(1.7).extrude(T))
for x,y in pins:
    pcb=pcb.cut(cq.Workplane('XY').center(x,y).circle(.55).extrude(T))
add('PCB_14p2x18p5x1p1',pcb,(.025,.17,.30))
for i,(x,y) in enumerate(pins,1):
    add(f'P{i}_plated_hole',ring(x,y,1.26,1.1,0,T),(.70,.72,.70))
    add(f'P{i}_top_pad',ring(x,y,1.8,1.1,T,.025),(.78,.78,.72))
    # The lower annulus remains inside the measured board-thickness envelope.
    add(f'P{i}_bottom_pad',ring(x,y,1.8,1.1,0,.025),(.78,.78,.72))
for i,(x,y) in enumerate(holes,1):
    add(f'H{i}_rim',ring(x,y,3.65,3.4,T,.015),(.55,.55,.45))

def passive(name,x,y,w,l,h,ceramic=False,horizontal=False):
    color=(.55,.40,.22) if ceramic else (.07,.075,.08)
    add(name,box(x,y,w,l,T+.08,h-.08),color)
    if horizontal:
        for side in [-1,1]:
            add(name+('_endL' if side<0 else '_endR'),box(x+side*(w/2-.13),y,.26,l+.06,T,.12),(.73,.74,.74))
    else:
        for side in [-1,1]:
            add(name+('_endA' if side<0 else '_endB'),box(x,y+side*(l/2-.18),w+.08,.36,T,.12),(.73,.74,.74))

# Positions projected from the four photographed PCB corners; no schematic claims.
passive('Cap_left',.945,13.499,.8,1.8,.80,True)
passive('Cap_row_1',7.076,13.459,.85,1.8,.80,True)
passive('Cap_row_2',8.558,13.408,.85,1.8,.80,True)
for i,x in enumerate([9.990,11.431,12.913],1):
    passive('Res_row_'+str(i),x,13.38,.8,1.8,.45)
passive('Res_near_holes',7.329,4.120,1.8,.8,.45,horizontal=True)
passive('Cap_near_holes',7.392,2.823,1.8,.8,.80,True,True)

# Regulator, three soldered leads. Highest feature defines the 2.0 mm envelope.
add('Regulator_body',box(4.376,13.548,1.35,2.90,T+.1,.8),(.06,.065,.07))
for i,(x,y) in enumerate([(3.35,13.55),(5.40,12.63),(5.40,14.47)],1):
    add('Regulator_lead_'+str(i),box(x,y,.7,.45,T,.22),(.72,.73,.73))
sx,sy=7.277,6.955
add('BH1750_body_reference',box(sx,sy,2.7,1.6,T+.08,.70),(.035,.038,.04))
for side in [-1,1]:
    for i,dy in enumerate([-.55,0,.55]):
        add(f'Sensor_lead_{side}_{i}',box(sx+side*1.51,sy+dy,.40,.29,T,.22),(.72,.73,.73))
# Flat optical region is only a visual marker; the light opening must clear the package.
add('Optical_region_visual_marker',box(sx,sy,1.10,.70,T+.78,.015),(.09,.105,.11))
add('Solder_bridge_reference',box(11.95,10.92,.75,.8,T,.2),(.60,.61,.61))

step=OUT/'BH1750-GY302-18p5x14p2-reference.step'
assy.export(str(step))
compound=cq.Compound.makeCompound([s for _,s,_ in parts])
cq.exporters.export(compound,str(OUT/'BH1750-GY302-reference.stl'),tolerance=.025,angularTolerance=.12)
b=compound.BoundingBox()
print('Tessellated envelope:',b.xlen,b.ylen,b.zlen)
assert np.allclose([b.xlen,b.ylen,b.zlen],[W,L,H],atol=.01)
reimport=cq.importers.importStep(str(step)).val()
assert reimport.isValid()
rb=reimport.BoundingBox()
assert np.allclose([rb.xlen,rb.ylen,rb.zlen],[W,L,H],atol=1e-5)
report={'units':'mm','measured':{'length':L,'width':W,'pcb_thickness':T,'assembly_thickness':H},
 'coordinate_system':'Origin at bottom-left of component-side photo, X across width, Y toward 5-pin row, Z toward components.',
 'estimated':{'mounting_holes_xy':holes,'mounting_hole_diameter':3.4,'pin_holes_xy':pins,'pin_hole_diameter':1.1,'sensor_center_xy':[sx,sy]},
 'components':len(parts),'step_roundtrip_valid':True,'verified_extents':[rb.xlen,rb.ylen,rb.zlen],
 'limitations':['Photo-derived hole sizes, component dimensions and positions are approximate.',
 'PCB thickness and total thickness are user measurements. Individual component heights are allocated within that envelope.',
 'No pin headers, wires or hand-solder blobs included. No old enclosure reused.']}
(OUT/'dimensions.json').write_text(json.dumps(report,indent=2),encoding='utf-8')

# CAD geometry preview, not a modified photograph.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
fig=plt.figure(figsize=(11,6),dpi=160,facecolor='#eff3f6')
for index,(elev,azim,title) in enumerate([(90,-90,'Component side'),(30,-65,'Assembly - 2.0 mm total')],1):
    ax=fig.add_subplot(1,2,index,projection='3d',computed_zorder=False)
    ax.set_facecolor('#eff3f6')
    triangles=[]; colors=[]
    for name,s,col in parts:
        vs,fs=s.tessellate(.05)
        p=np.array([[v.x,v.y,v.z] for v in vs])
        triangles.extend(p[np.array(fs)]);colors.extend([col]*len(fs))
    poly=Poly3DCollection(triangles,facecolors=colors,edgecolors='none',linewidths=0,zsort='average',antialiased=False)
    ax.add_collection3d(poly)
    ax.set_xlim(0,W);ax.set_ylim(0,L);ax.set_zlim(0,4)
    ax.set_box_aspect((W,L,4));ax.view_init(elev=elev,azim=azim);ax.set_proj_type('ortho')
    ax.set_axis_off();ax.set_title(title,pad=0,fontsize=13)
fig.suptitle('BH1750 / GY-302 reference | PCB 18.5 x 14.2 x 1.1 mm',fontsize=15)
fig.text(.5,.04,'Hole and component placement estimated from photographs; no pins or wires.',ha='center',fontsize=10,color='#48586a')
plt.tight_layout(rect=[0,.06,1,.93]);fig.savefig(OUT/'preview.png');plt.close(fig)

# Orthographic z-buffer render avoids painter-order artifacts on the large PCB face.
from PIL import Image,ImageDraw,ImageFont
canvas=Image.new('RGB',(1500,850),(239,243,246))
draw=ImageDraw.Draw(canvas)
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',27)
small=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',21)
draw.text((65,25),'BH1750 / GY-302 | PCB 18.5 x 14.2 x 1.1 mm',font=font,fill=(25,40,55))
for panel,eye in enumerate([np.array([0.,0.,1.]),np.array([.8,-1.,1.3])]):
    eye/=np.linalg.norm(eye)
    right=np.array([1.,0.,0.]) if panel==0 else np.cross([0,0,1],eye)
    right/=np.linalg.norm(right);up=np.cross(eye,right)
    matrix=np.array([right,up,eye])
    tris=[];cols=[]
    light=np.array([-.4,-.3,1.]);light/=np.linalg.norm(light)
    for name,s,col in parts:
        vs,faces=s.tessellate(.04)
        p=np.array([[v.x,v.y,v.z] for v in vs])
        for f in faces:
            t=p[np.array(f)];n=np.cross(t[1]-t[0],t[2]-t[0]);n/=max(np.linalg.norm(n),1e-15)
            tris.append(t@matrix.T)
            cols.append(np.clip(np.array(col)*255*(.65+.35*max(0,np.dot(n,light))),0,255))
    tris=np.array(tris);flat=tris.reshape(-1,3)
    lo=flat[:,:2].min(0);hi=flat[:,:2].max(0)
    scale=min(620/(hi[0]-lo[0]),610/(hi[1]-lo[1]))
    tris[:,:,0]=(tris[:,:,0]-(lo[0]+hi[0])/2)*scale+350
    tris[:,:,1]=-(tris[:,:,1]-(lo[1]+hi[1])/2)*scale+330
    rgb=np.full((660,700,3),[239,243,246],dtype=np.uint8)
    depth=np.full((660,700),-np.inf)
    for t,col in zip(tris,cols):
        x0=max(0,int(np.floor(t[:,0].min())));x1=min(699,int(np.ceil(t[:,0].max())))
        y0=max(0,int(np.floor(t[:,1].min())));y1=min(659,int(np.ceil(t[:,1].max())))
        if x0>x1 or y0>y1:continue
        a,b,c=t;den=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
        if abs(den)<1e-8:continue
        yy,xx=np.mgrid[y0:y1+1,x0:x1+1];xx=xx+.5;yy=yy+.5
        w1=((b[1]-c[1])*(xx-c[0])+(c[0]-b[0])*(yy-c[1]))/den
        w2=((c[1]-a[1])*(xx-c[0])+(a[0]-c[0])*(yy-c[1]))/den;w3=1-w1-w2
        z=w1*a[2]+w2*b[2]+w3*c[2]
        region=depth[y0:y1+1,x0:x1+1]
        mask=(w1>=-1e-8)&(w2>=-1e-8)&(w3>=-1e-8)&(z>region)
        region[mask]=z[mask];rgb[y0:y1+1,x0:x1+1][mask]=col
    canvas.paste(Image.fromarray(rgb),(25+750*panel,110))
    draw.text((90+750*panel,85),'Component side' if panel==0 else 'Assembly: 2.0 mm total',font=small,fill=(35,50,65))
draw.text((115,800),'Photo-estimated holes and components. No pin headers or wires included.',font=small,fill=(65,80,95))
canvas.save(OUT/'preview.png')
print(json.dumps(report,indent=2))
