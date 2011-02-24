import maya.cmds as cmds


def main(boolMode=1):
    """
    @type boolMode: boolean
    @param boolMode: Script mode, 0 to remove, 1 to add
    """
    listAttrs = [['rmanFhasProjection',1],
                 ['rmanFmakeTransparent',0]]
    listSel = cmds.ls(sl=1)
    for sSel in listSel:        
        for element in listAttrs:
            if boolMode == 1:
                if not element[0] in cmds.listAttr(sSel):
                    cmds.addAttr(sSel, 
                                 ln=element[0], 
                                 at='bool')
                    cmds.setAttr('%s.%s' %(sSel,element[0]), 
                                 element[1], 
                                 e=1, 
                                 k=1)
            elif boolMode == 0:
                if element[0] in cmds.listAttr(sSel):
                    cmds.deleteAttr('%s.%s' %(sSel,element[0]))







