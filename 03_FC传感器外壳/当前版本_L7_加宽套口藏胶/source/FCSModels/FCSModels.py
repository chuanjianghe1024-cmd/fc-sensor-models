import os
def run(context):
    source=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    repo=os.path.abspath(os.path.join(source,'..','..','..'))
    ns={'REPO':repo}
    for name in ['fusion_helpers.py','build.py']:
        path=os.path.join(source,name)
        exec(compile(open(path,encoding='utf-8').read(),path,'exec'),ns)
    ns['run'](context)
