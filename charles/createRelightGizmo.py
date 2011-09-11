n = nuke.selectedNodes()
if len(n) != 0:
    nodeRelight = nuke.nodePaste("/usr/people/charles-c/Lighting/jcom/template/relight_gizmo.nk")
    n.append(nodeRelight)
    nuke.extractSelected()
    n = [item.name() for item in n]
    for currItem in n:
        nuke.toNode(currItem)['selected'].setValue(True)
    execfile("/usr/people/charles-c/Lighting/jcom/script/connectNodes.py")
else:
    nuke.nodePaste("/usr/people/charles-c/Lighting/jcom/template/relight_gizmo.nk")
