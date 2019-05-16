import pymel.core as pm
def solveOnModelChange3dc():
    # 获取Maya中的所有编辑器，并重置editorChanged事件
    for item in pm.lsUI(editors=True):
        if isinstance(item, pm.ui.ModelEditor):
            pm.modelEditor(item, edit=True, editorChanged="")