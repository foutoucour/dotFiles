####################################
''' menu.py pour avoirle gizmo
'''

#rebuild GUI of relight gizmo
import sys

def rebuild():
    sys.path.append('/usr/people/charles-c/Lighting/release/script/')
    import rebuildGUI
    rebuildGUI.RebuildUI()
        
nuke.callbacks.addKnobChanged(rebuild, args=(), kwargs={}, nodeClass='Group')


#Toolbar for light
m = nuke.toolbar("Nodes").addMenu('Lighting', icon="/usr/people/charles-c/.nuke/RenderMan.png")
m.addCommand('Relight', 'execfile("/usr/people/charles-c/Lighting/jcom/script/createRelightGizmo.py")', icon="/usr/people/charles-c/.nuke/Nuke.png")
m.addCommand('Relight Multi', 'nuke.nodePaste("/usr/people/charles-c/Lighting/jcom/template/relight_multi_gizmo.nk")', icon="/usr/people/charles-c/.nuke/Nuke.png")
m.addCommand('Connect input nodes', 'execfile("/usr/people/charles-c/Lighting/jcom/script/connectNodes.py")', icon="/usr/people/charles-c/.nuke/Nuke.png")
