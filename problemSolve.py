import pymel.core as pm
def solveOnModelChange3dc():
    # ��ȡMaya�е����б༭����������editorChanged�¼�
    for item in pm.lsUI(editors=True):
        if isinstance(item, pm.ui.ModelEditor):
            pm.modelEditor(item, edit=True, editorChanged="")