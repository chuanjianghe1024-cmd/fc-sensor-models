"""Shared Fusion native geometry and checks for L7. Length inputs are mm."""
import adsk.core as C, adsk.fusion as F, math, json, os, traceback, time
NEW=F.FeatureOperations.NewBodyFeatureOperation
JOIN=F.FeatureOperations.JoinFeatureOperation
CUT=F.FeatureOperations.CutFeatureOperation
rounding=[]
SX=4.848; SY=-.35
CX=SX+14.2-7.277; CY=18.15-6.955
X0=-1.; X1=26.; Y0=CY-18.; Y1=CY+18.
FRONT_CY=CY; HOOK_HALF=4.2

def pt(x,y,z=0):return C.Point3D.create(x/10,y/10,z/10)

def val(mm):return C.ValueInput.createByReal(mm/10)

def trans(x=0,y=0,z=0):
    m=C.Matrix3D.create();m.translation=C.Vector3D.create(x/10,y/10,z/10);return m

def bounds(b):
    bb=b.boundingBox
    return [[v*10 for v in bb.minPoint.asArray()],[v*10 for v in bb.maxPoint.asArray()]]

def save_json(name,data):
    with open(os.path.join(OUT,name),'w',encoding='utf-8') as f:json.dump(data,f,indent=2,ensure_ascii=False)

def log(s):
    with open(os.path.join(OUT,'build-log.txt'),'a',encoding='utf-8') as f:f.write(s+'\n')

def occ(root,name):
    o=root.occurrences.addNewComponent(C.Matrix3D.create());o.component.name=name
    o.isGroundToParent=False
    return o

def sketch_at(comp,z,name):
    ip=comp.constructionPlanes.createInput();ip.setByOffset(comp.xYConstructionPlane,val(z))
    pl=comp.constructionPlanes.add(ip);pl.isLightBulbOn=False
    s=comp.sketches.add(pl);s.name=name;return s

def extrude(comp,s,length,op,name):
    inp=comp.features.extrudeFeatures.createInput(s.profiles.item(0),op)
    inp.setDistanceExtent(False,val(length))
    if op==CUT:inp.participantBodies=[b for b in comp.bRepBodies]
    ex=comp.features.extrudeFeatures.add(inp);ex.name=name;s.isVisible=False
    return ex.bodies.item(0)

def rect(comp,x0,y0,z0,x1,y1,z1,op,name):
    s=sketch_at(comp,z0,name+' sketch')
    s.sketchCurves.sketchLines.addTwoPointRectangle(pt(x0,y0),pt(x1,y1))
    return extrude(comp,s,z1-z0,op,name)

def cyl_y(comp,x,z,y0,y1,r,op,name):
    ip=comp.constructionPlanes.createInput();ip.setByOffset(comp.xZConstructionPlane,val(-y1))
    pl=comp.constructionPlanes.add(ip);pl.isLightBulbOn=False
    s=comp.sketches.add(pl);s.name=name+' sketch'
    s.sketchCurves.sketchCircles.addByCenterRadius(s.modelToSketchSpace(pt(x,y1,z)),r/10)
    return extrude(comp,s,y0-y1,op,name)

def capsule_x(comp,x0,x1,cy,cz,w,h,op,name):
    ip=comp.constructionPlanes.createInput();ip.setByOffset(comp.yZConstructionPlane,val(x0))
    pl=comp.constructionPlanes.add(ip);pl.isLightBulbOn=False
    s=comp.sketches.add(pl);s.name=name+' sketch'
    a=cy-(w-h)/2;b=cy+(w-h)/2;r=h/2
    def q(y,z):return s.modelToSketchSpace(pt(x0,y,z))
    ls=s.sketchCurves.sketchLines;ar=s.sketchCurves.sketchArcs
    ls.addByTwoPoints(q(a,cz-r),q(b,cz-r))
    ar.addByThreePoints(q(b,cz-r),q(b+r,cz),q(b,cz+r))
    ls.addByTwoPoints(q(b,cz+r),q(a,cz+r))
    ar.addByThreePoints(q(a,cz+r),q(a-r,cz),q(a,cz-r))
    return extrude(comp,s,x1-x0,op,name)

def archive(des,name):
    path=os.path.join(OUT,name+'.f3d')
    ex=des.exportManager
    ok=ex.execute(ex.createFusionArchiveExportOptions(path))
    if not ok:raise RuntimeError('Archive export failed: '+name)
    log('Saved '+path)

def camera(app,eye,target,up=(0,0,1)):
    cam=app.activeViewport.camera;cam.eye=pt(*eye);cam.target=pt(*target)
    cam.upVector=C.Vector3D.create(*up);cam.isFitView=True;cam.isSmoothTransition=False
    app.activeViewport.camera=cam;app.activeViewport.refresh()

def render(app,name):app.activeViewport.saveAsImageFile(os.path.join(OUT,name),1500,1000)

def roundrect(comp,x0,y0,z0,x1,y1,z1,r,op,name):
    s=sketch_at(comp,z0,name+' sketch');ls=s.sketchCurves.sketchLines;ar=s.sketchCurves.sketchArcs
    k=1-math.sqrt(.5)
    ls.addByTwoPoints(pt(x0+r,y0),pt(x1-r,y0))
    ar.addByThreePoints(pt(x1-r,y0),pt(x1-r*k,y0+r*k),pt(x1,y0+r))
    ls.addByTwoPoints(pt(x1,y0+r),pt(x1,y1-r))
    ar.addByThreePoints(pt(x1,y1-r),pt(x1-r*k,y1-r*k),pt(x1-r,y1))
    ls.addByTwoPoints(pt(x1-r,y1),pt(x0+r,y1))
    ar.addByThreePoints(pt(x0+r,y1),pt(x0+r*k,y1-r*k),pt(x0,y1-r))
    ls.addByTwoPoints(pt(x0,y1-r),pt(x0,y0+r))
    ar.addByThreePoints(pt(x0,y0+r),pt(x0+r*k,y0+r*k),pt(x0+r,y0))
    return extrude(comp,s,z1-z0,op,name)

def edge_round(comp,r,name,predicate):
    edges=C.ObjectCollection.create()
    for b in comp.bRepBodies:
        for e in b.edges:
            bb=e.boundingBox
            lo=[a*10 for a in bb.minPoint.asArray()];hi=[a*10 for a in bb.maxPoint.asArray()]
            if predicate(lo,hi):edges.add(e)
    if not edges.count:
        rounding.append({'name':name,'status':'no edges'});return
    fi=comp.features.filletFeatures.createInput()
    fi.edgeSetInputs.addConstantRadiusEdgeSet(edges,val(r),False)
    f=comp.features.filletFeatures.add(fi);f.name=name
    rounding.append({'name':name,'radius_mm':r,'edges':edges.count,'status':'created'})

def roundrect_y(comp,x0,z0,y0,x1,z1,y1,r,op,name):
    ip=comp.constructionPlanes.createInput();ip.setByOffset(comp.xZConstructionPlane,val(-y1))
    pl=comp.constructionPlanes.add(ip);pl.isLightBulbOn=False
    s=comp.sketches.add(pl);s.name=name+' sketch'
    def q(x,z):return s.modelToSketchSpace(pt(x,y1,z))
    ls=s.sketchCurves.sketchLines;ar=s.sketchCurves.sketchArcs;k=1-math.sqrt(.5)
    ls.addByTwoPoints(q(x0+r,z0),q(x1-r,z0))
    ar.addByThreePoints(q(x1-r,z0),q(x1-r*k,z0+r*k),q(x1,z0+r))
    ls.addByTwoPoints(q(x1,z0+r),q(x1,z1-r))
    ar.addByThreePoints(q(x1,z1-r),q(x1-r*k,z1-r*k),q(x1-r,z1))
    ls.addByTwoPoints(q(x1-r,z1),q(x0+r,z1))
    ar.addByThreePoints(q(x0+r,z1),q(x0+r*k,z1-r*k),q(x0,z1-r))
    ls.addByTwoPoints(q(x0,z1-r),q(x0,z0+r))
    ar.addByThreePoints(q(x0,z0+r),q(x0+r*k,z0+r*k),q(x0+r,z0))
    return extrude(comp,s,y0-y1,op,name)

def poly_y(cp,points,y0,y1,op,name):
    ip=cp.constructionPlanes.createInput();ip.setByOffset(cp.xZConstructionPlane,val(-y1))
    pl=cp.constructionPlanes.add(ip);pl.isLightBulbOn=False
    s=cp.sketches.add(pl);s.name=name
    ps=[s.modelToSketchSpace(pt(x,y1,z)) for x,z in points]
    for a,b in zip(ps,ps[1:]+ps[:1]):s.sketchCurves.sketchLines.addByTwoPoints(a,b)
    return extrude(cp,s,y0-y1,op,name)

def rotation(deg):
    m=C.Matrix3D.create();m.setToRotation(math.radians(deg),C.Vector3D.create(0,1,0),pt(AX,0,AZ));return m

def overlap(a,b,m=None):
    tm=F.TemporaryBRepManager.get();a=tm.copy(a);b=tm.copy(b)
    if m:tm.transform(b,m)
    if not tm.booleanOperation(a,b,F.BooleanTypes.IntersectionBooleanType):raise RuntimeError('Boolean inspection failed')
    return a.volume*1000

def appearance(des,name,rgb):
    app=C.Application.get();src=None
    for lib in app.materialLibraries:
        src=lib.appearances.itemByName('塑料 - 粗面(白色)')
        if src:break
    assert src,'White plastic appearance missing'
    a=des.appearances.addByCopy(src,name)
    props=[p for p in a.appearanceProperties if C.ColorProperty.cast(p)]
    log(name+' properties '+str([(p.id,p.name) for p in props]))
    p=next((p for p in props if p.id in ('opaque_albedo','generic_diffuse')),props[0] if props else None)
    assert p,'No editable color property'
    C.ColorProperty.cast(p).value=C.Color.create(*rgb,255)
    return a

def boolean(a,b,op):
    tm=F.TemporaryBRepManager.get();c=tm.copy(a)
    assert tm.booleanOperation(c,tm.copy(b),op),'Native Boolean failed'
    return c

def total_union(bodies):
    tm=F.TemporaryBRepManager.get();u=tm.copy(bodies[0])
    for b in bodies[1:]:assert tm.booleanOperation(u,tm.copy(b),F.BooleanTypes.UnionBooleanType)
    return u

def light_cone(cp):
    ip=cp.constructionPlanes.createInput();ip.setByOffset(cp.xZConstructionPlane,val(-CY))
    pl=cp.constructionPlanes.add(ip);pl.isLightBulbOn=False
    sk=cp.sketches.add(pl);sk.name='Optical opening 45 degree section, face-down print'
    pts=[(0,2.3),(3.2,2.3),(3.2,2.8),(4.9,4.5),(0,4.5)]
    ps=[sk.modelToSketchSpace(pt(CX+r,CY,z)) for r,z in pts]
    ls=sk.sketchCurves.sketchLines
    for a,b in zip(ps,ps[1:]):ls.addByTwoPoints(a,b)
    axis=ls.addByTwoPoints(ps[-1],ps[0])
    i=cp.features.revolveFeatures.createInput(sk.profiles.item(0),axis,CUT)
    i.setAngleExtent(False,C.ValueInput.createByString('360 deg'));i.participantBodies=list(cp.bRepBodies)
    cp.features.revolveFeatures.add(i).name='Light inlet radial narrowing equals layer height';sk.isVisible=False

def validate(des,root,base,hook,lid,foot,c3,sensor,screw,nut,gauge):
    report={'parts':{},'intentional_thread_interference':[],'solid_collisions':[],'board_collisions':[],'motion_collisions':[],'optical_reference':[],'feature_issues':[]}
    parts=[base,hook,lid,foot,screw,nut]
    for o in parts:report['parts'][o.name]=[{'bounds_mm':bounds(b),'volume_mm3':b.volume*1000,'solid':b.isSolid} for b in o.component.bRepBodies]
    for i,a in enumerate(parts):
        for b in parts[i+1:]:
            v=sum(overlap(ba,bb) for ba in a.component.bRepBodies for bb in b.component.bRepBodies)
            if v>1e-4:
                key='intentional_thread_interference' if a==base and b==screw else 'solid_collisions'
                report[key].append({'a':a.name,'b':b.name,'mm3':v})
    tm=F.TemporaryBRepManager.get()
    refs=[]
    for b in c3.component.bRepBodies:
        t=tm.copy(b);tm.transform(t,c3.transform2);refs.append(('C3',t))
    for o in root.allOccurrences:
        if o.fullPathName.startswith(sensor.name):
            for b in o.bRepBodies:
                refs.append((o.name,b))
                if 'Optical_region' in o.name or 'BH1750_body' in o.name:report['optical_reference'].append({'name':o.name,'bounds_mm':bounds(b)})
    for name,b in refs:
        for target in [base,hook,lid,foot]:
            v=sum(overlap(t,b) for t in target.component.bRepBodies)
            if v>1e-4:
                t=tm.copy(target.component.bRepBodies.item(0));tm.booleanOperation(t,tm.copy(b),F.BooleanTypes.IntersectionBooleanType)
                report['board_collisions'].append({'ref':name,'part':target.name,'mm3':v,'intersection_bounds_mm':bounds(t)})
    for angle in range(0,121,3):
        m=rotation(angle)
        for target in [base,hook,lid,gauge]:
            v=sum(overlap(t,b,m) for t in target.component.bRepBodies for b in foot.component.bRepBodies)
            if v>1e-4:report['motion_collisions'].append({'angle':angle,'part':target.name,'mm3':v})
    for target in [base,lid,hook,screw,nut]:
        v=sum(overlap(t,b) for t in target.component.bRepBodies for b in gauge.component.bRepBodies)
        if v>1e-4:report['solid_collisions'].append({'a':target.name,'b':'USB gauge','mm3':v})
    report['feature_issues']=[{'name':f.name,'message':f.errorOrWarningMessage} for cp in des.allComponents for f in cp.features if f.healthState!=F.FeatureHealthStates.HealthyFeatureHealthState]
    save_json('validation.json',report)

def native_copy(cp,tmp,name,ap=None):
    bf=cp.features.baseFeatures.add();bf.name=name;bf.startEdit()
    b=cp.bRepBodies.add(tmp,bf);bf.finishEdit()
    for b in bf.bodies:
        b.name=name
        if ap:b.appearance=ap
    return bf.bodies.item(0)

def do_export(des,parent,name,originals,axis=None,angle=0,mono=False):
    tm=F.TemporaryBRepManager.get();ex=des.exportManager
    out=os.path.join(OUT,'print-files');os.makedirs(out,exist_ok=True)
    bodies=[tm.copy(b) for b in originals]
    if mono:bodies=[total_union(bodies)]
    if axis:
        m=C.Matrix3D.create();m.setToRotation(math.radians(angle),C.Vector3D.create(*axis),pt(0,0,0))
        for b in bodies:tm.transform(b,m)
    mins=[min(b.boundingBox.minPoint.asArray()[i] for b in bodies) for i in range(3)]
    m=C.Matrix3D.create();m.translation=C.Vector3D.create(*[-v for v in mins])
    dst=occ(parent,name)
    for i,b in enumerate(bodies):
        tm.transform(b,m);native_copy(dst.component,b,name if mono else originals[i].name,None if mono else originals[i].appearance)
    assert all(b.isSolid for b in dst.component.bRepBodies)
    assert ex.execute(ex.createSTEPExportOptions(os.path.join(out,name+'.step'),dst.component))
    opt=ex.createC3MFExportOptions(dst.component,os.path.join(out,name+'.3mf'))
    opt.sendToPrintUtility=False;opt.isOneFilePerBody=False;opt.meshRefinement=F.MeshRefinementSettings.MeshRefinementHigh;opt.surfaceDeviation=.0005
    assert ex.execute(opt)
    if mono:
        opt=ex.createSTLExportOptions(dst.component,os.path.join(out,name+'.stl'))
        opt.unitType=F.DistanceUnits.MillimeterDistanceUnits;opt.isBinaryFormat=True;opt.sendToPrintUtility=False;opt.meshRefinement=F.MeshRefinementSettings.MeshRefinementHigh
        assert ex.execute(opt)
    log('EXPORTED '+name)
    return {'name':name,'bounds_mm':[bounds(b) for b in dst.component.bRepBodies],'solid':all(b.isSolid for b in dst.component.bRepBodies),'volume_mm3':sum(b.volume*1000 for b in dst.component.bRepBodies)}
