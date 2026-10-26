OUT=os.path.join(REPO,'generated','L7-'+time.strftime('%Y%m%d-%H%M%S'))
SOURCE=os.path.join(REPO,'03_FC传感器外壳','当前版本_L6_单件平底','FCS-L6-individual-flat-bottoms.f3d')
AX=-6.5;AZ=-8.6
NY0=Y0-2;NY1=Y1+2

def build_base(root):
    o=occ(root,'L7 Base - wider hidden glue channel');cp=o.component
    roundrect(cp,X0,NY0,-11.4,X1,NY1,2.4,2.2,NEW,'40 mm wide shell')
    roundrect(cp,-.1,NY0+2.2,-7,23.8,NY1-2.2,3,.8,CUT,'Enlarged cavity')
    capsule_x(cp,-1.1,.15,8.9,-2.55,9.4,3.7,CUT,'Original USB opening')
    for xa,xb in [(.25,2.25),(20.25,22.25)]:
        for ya,yb in [(.1,1.4),(16.4,17.7)]:
            rect(cp,xa,ya,-7.01,xb,yb,-1.02,JOIN,'PCB corner support')
    for xa,xb in [(.2,1.4),(20.5,22.5)]:
        for ya,yb in [(-.45,-.1),(17.9,18.3)]:
            rect(cp,xa,ya,-7.01,xb,yb,.1,JOIN,'PCB side locator')
    rect(cp,22.75,4,-7.01,23.6,13,.15,JOIN,'PCB tail stop')
    a=CY-4.2;b=CY+4.2
    rect(cp,24.05,a-.35,-11.5,26.1,b+.35,3,CUT,'Front hook mouth')
    rect(cp,23.25,a-1.1,-7.8,24.95,b+1.1,3,CUT,'Front hook flange channel')
    rect(cp,23.55,a-.35,-11.5,24.1,b+.35,3,CUT,'Front hook insertion clearance')
    # Keep original M3x30 screw bearing span, even though the enclosure is wider.
    for ya,yb in [(Y0,-1.7),(18.6,Y1)]:
        roundrect_y(cp,AX-4.8,-11.4,ya,1.5,-4.5,yb,.6,JOIN,'Flat fixed hinge cheek')
        if ya<0:cyl_y(cp,AX,AZ,ya-.1,yb+.1,1.7,CUT,'M3 clearance')
        else:
            cyl_y(cp,AX,AZ,18.5,24.4,1.35,CUT,'M3 plastic pilot 2.7 mm')
            cyl_y(cp,AX,AZ,18.5,19.1,1.65,CUT,'Pilot entrance')
    rect(cp,-11.2,-2.1,-5.9,-9.2,.3,-4.5,JOIN,'90 degree stop')
    # Recess below dry outer rim, opening into the internal sleeve gap.
    rect(cp,2,NY0+1.85,1.15,21,NY0+2.21,1.85,CUT,'Hidden glue reservoir left')
    rect(cp,2,NY1-2.21,1.15,21,NY1-1.85,1.85,CUT,'Hidden glue reservoir right')
    return o

def build_lid(root):
    o=occ(root,'L7 Cover - nested skirt no latches');cp=o.component
    roundrect(cp,X0,NY0,2.4,X1,NY1,4.4,2.2,NEW,'Wider lid original optical height')
    edge_round(cp,.3,'Soft lid top edge',lambda lo,hi:abs(lo[2]-4.4)<1e-4 and abs(hi[2]-4.4)<1e-4)
    light_cone(cp)
    # Build sleeve separately so hollowing it cannot erase the lid plate.
    sleeve=occ(root,'L7 TOOL sleeve');sc=sleeve.component
    roundrect(sc,.15,NY0+2.45,.9,23.55,NY1-2.45,2.41,.55,NEW,'Sleeve outside clearance 0.25')
    roundrect(sc,1.15,NY0+3.45,.8,22.55,NY1-3.45,2.5,.3,CUT,'Sleeve wall 1 mm')
    # Local relief only at front hook's flange; all other sides remain continuous.
    rect(sc,23.2,CY-5.5,.8,24,CY+5.5,2.5,CUT,'Front hook relief')
    tmp=total_union([*cp.bRepBodies,*sc.bRepBodies])
    cp.features.removeFeatures.add(cp.bRepBodies.item(0))
    native_copy(cp,tmp,'Lid and internal locating sleeve')
    sleeve.isLightBulbOn=False
    rect(cp,SX-.8,5,.25,SX-.25,14,2.41,JOIN,'Sensor USB side locator')
    rect(cp,SX+14.45,5,.25,SX+15,14,2.41,JOIN,'Sensor tail locator')
    rect(cp,20.7,3,.12,22.2,14.8,2.41,JOIN,'Opposite USB PCB hold down')
    return o

def build_leg(root):
    o=occ(root,'L7 H leg - wider panel original M3 barrel');cp=o.component
    roundrect(cp,2,NY0,-15.6,26,NY1,-12.6,2.2,NEW,'Wider flat panel')
    edge_round(cp,.3,'Soft leg bottom edge',lambda lo,hi:abs(lo[2]+15.6)<1e-4 and abs(hi[2]+15.6)<1e-4)
    roundrect(cp,1.9,2.05,-15.7,7.2,14.85,-12.5,.8,CUT,'Rear cable notch')
    roundrect(cp,23.5,CY-4.65,-15.7,26.2,CY+4.65,-12.5,.4,CUT,'Front hook clearance')
    poly_y(cp,[(AX-2.7,-15.6),(AX+2.7,-15.6),(AX+2.7,AZ),(AX-2.7,AZ)],-1.6,18.5,NEW,'Flat hinge heel')
    cyl_y(cp,AX,AZ,-1.6,18.5,2.7,JOIN,'Continuous clamping barrel')
    for ya,yb in [(-1.6,2),(14.8,18.5)]:rect(cp,AX,ya,-15.6,5,yb,-12.6,JOIN,'Heel arms')
    cyl_y(cp,AX,AZ,-1.7,18.6,1.7,CUT,'Moving M3 bore')
    for ya,yb in [(NY0-.1,-1.65),(18.55,NY1+.1)]:
        rect(cp,1.9,ya,-15.7,5.3,yb,-12.5,CUT,'Fixed cheek swing clearance')
    roundrect(cp,9,CY-11,-15.7,21.8,CY+11,-15,1.2,CUT,'Recessed adhesive pad')
    return o

def partition(o,root,z0,z1,label,black,green):
    mask=occ(root,'L7 TOOL color '+label);cp=mask.component
    roundrect(cp,-1.1,NY0-.1,z0,26.1,NY1+.1,z1,2.2,NEW,'Green perimeter')
    roundrect(cp,-.15,NY0+.85,z0-.1,25.15,NY1-.85,z1+.1,1.35,CUT,'Green inner boundary')
    tmp=total_union(list(o.component.bRepBodies));cut=mask.component.bRepBodies.item(0)
    g=boolean(tmp,cut,F.BooleanTypes.IntersectionBooleanType)
    k=boolean(tmp,cut,F.BooleanTypes.DifferenceBooleanType)
    for b in list(o.component.bRepBodies):o.component.features.removeFeatures.add(b)
    native_copy(o.component,k,'Black_'+label,black);native_copy(o.component,g,'Green_edge_'+label,green)
    mask.isLightBulbOn=False

def run(context):
    app=C.Application.get();os.makedirs(OUT,exist_ok=True)
    try:
        log('L7 start '+time.strftime('%Y-%m-%d %H:%M:%S'))
        app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(SOURCE))
        des=F.Design.cast(app.activeProduct);root=des.rootComponent
        app.activeDocument.name='FCS L7 - wider nested glue lid'
        get=lambda p:next(o for o in root.occurrences if o.name.startswith(p))
        hook=get('L11');accent=get('L10');c3=get('01 ');sensor=get('02 ');screw=get('L6 M3');gauge=get('QA USB');nut=get('NO NUT')
        for o in root.occurrences:o.isLightBulbOn=False
        for o in [hook,accent,c3,sensor]:o.isLightBulbOn=True
        for n,v in [('case_width',40),('lid_thickness',2)]:
            p=des.userParameters.itemByName(n)
            if p:p.value=v/10
        for n,v in [('L7_side_widening',2),('L7_skirt_clearance',.25),('L7_skirt_depth',1.5),('L7_glue_recess_depth',.35),('L7_dry_rim_height',.55)]:
            des.userParameters.add(n,val(v),'mm','L7 nominal prototype dimensions; print fit still required')
        base=build_base(root);log('BASE built')
        lid=build_lid(root);log('LID built')
        foot=build_leg(root);log('LEG built')
        black=appearance(des,'L7 black PLA',(22,24,28));green=appearance(des,'L7 green PLA',(45,205,85))
        # Reuse the proven FC and wave inlay without moving its optical center.
        tmp=total_union(list(lid.component.bRepBodies))
        for b in accent.component.bRepBodies:tmp=boolean(tmp,b,F.BooleanTypes.DifferenceBooleanType)
        for b in list(lid.component.bRepBodies):lid.component.features.removeFeatures.add(b)
        native_copy(lid.component,tmp,'Black lid with flush transparent inlay',black)
        for b in base.component.bRepBodies:b.appearance=black
        partition(lid,root,3.8,4.5,'top',black,green)
        partition(foot,root,-15.7,-15,'bottom',black,green)
        des.computeAll()
        log('VALIDATING')
        validate(des,root,base,hook,lid,foot,c3,sensor,screw,nut,gauge)
        report=json.load(open(os.path.join(OUT,'validation.json'),encoding='utf-8'))
        report['beyond_stop_collisions']=[i for i in report['motion_collisions'] if i['angle']>90]
        report['motion_collisions']=[i for i in report['motion_collisions'] if i['angle']<=90]
        insert=[]
        for dz in [0,.2,.5,1,1.5,2,4,8]:
            for target in [base,hook]:
                vol=sum(overlap(a,b,trans(0,0,dz)) for a in target.component.bRepBodies for b in lid.component.bRepBodies)
                if vol>1e-4:insert.append({'dz':dz,'target':target.name,'mm3':vol})
        report['lid_insertion_collisions']=insert
        report['design']={'case_width_mm':40,'old_width_mm':36,'skirt_depth_mm':1.5,'skirt_clearance_per_side_mm':.25,'glue_recess_depth_mm':.35,'dry_rim_height_mm':.55,'optical_center_mm':[CX,CY],'sensor_to_lid_inner_gap_mm':.42,'screw':'M3x30 socket head, direct plastic, no nut','pilot_mm':2.7,'effective_thread_engagement_mm':Y0+30-19.1}
        save_json('validation.json',report)
        for cp in des.allComponents:
            for s in cp.sketches:s.isVisible=False
            for p in cp.constructionPlanes:p.isLightBulbOn=False
            cp.isOriginFolderLightBulbOn=False
        camera(app,(57,47,38),(10,CY,-5));render(app,'L7-closed.png')
        archive(des,'FCS-L7-hidden-glue-candidate')
        assert not any(report[k] for k in ['solid_collisions','board_collisions','motion_collisions','feature_issues','lid_insertion_collisions']),report
        exports=occ(root,'L7 EXPORT oriented print parts');records=[]
        for name,src,axis,angle in [('01_Base',[base],None,0),('02_Front_hook',[hook],(0,1,0),90),('03_H_leg',[foot],None,0),('04_Lid',[lid,accent],(1,0,0),180)]:
            bs=[b for o in src for b in o.component.bRepBodies]
            records.append(do_export(des,exports.component,name+'_single',bs,axis,angle,True))
            if name in ['03_H_leg','04_Lid']:records.append(do_export(des,exports.component,name+'_color',bs,axis,angle,False))
        exports.isLightBulbOn=False
        save_json('export-check.json',records)
        lid.isLightBulbOn=False;accent.isLightBulbOn=False
        camera(app,(42,40,55),(10,CY,-3));render(app,'L7-internal-supports.png')
        lid.isLightBulbOn=True;accent.isLightBulbOn=True
        lid.transform2=trans(0,0,9);accent.transform2=trans(0,0,9)
        camera(app,(-40,-50,20),(10,CY,-1));render(app,'L7-exploded-skirt.png')
        lid.transform2=C.Matrix3D.create();accent.transform2=C.Matrix3D.create()
        foot.transform2=rotation(65)
        camera(app,(-49,-56,30),(10,CY,-5));render(app,'L7-open.png')
        foot.transform2=C.Matrix3D.create()
        if des.snapshots.hasPendingSnapshot:des.snapshots.add()
        camera(app,(57,47,38),(10,CY,-5))
        archive(des,'FCS-L7-hidden-glue-assembly')
        log('L7 DONE')
    except:log(traceback.format_exc())
