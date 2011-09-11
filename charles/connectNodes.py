import nuke,re

nAOV = {}
nameFile = []
multiDiffuseAOV = []
relightGrp = nuke.toNode('relight')

currSelect = nuke.selectedNodes()
for item in currSelect:
    findRelightRgx = re.compile('(\w)*'+'relight'+'(\w)*')
    findRelightCorr = findRelightRgx.search(item.name())
    if findRelightCorr:
        print item.name()
        currSelect.remove(item)
        relightGrp = nuke.toNode(item.name())

print currSelect

#nuke.invertSelection()
#allNodes = nuke.selectedNodes()

shot = os.environ['SHOT'].split('/')[1]


for item in currSelect:

    try:
        nameFile = nuke.toNode(item.name()).knob('pass').value()
    except:
        nameFile =  item.knob('file').value().split("/")[-1].split(".")[0]
    nameNode = item.name()
    print nameFile
    
    count = 0
    while (count < 10):
        multiDiffuseRgx = re.compile('(\w)*'+'(md|m(ulti)?(d|D)iff(use)?)'+str(count)+'(\w)*')
        multiDiffuseCorr = multiDiffuseRgx.search(nameFile)
        if multiDiffuseCorr:
            nAOV['MULTIDIFFUSE'+str(count)] = nameNode

        multiSpecularRgx = re.compile('(\w)*'+'(ms|m(ulti)?(s|S)pec(ular)?)'+str(count)+'(\w)*')
        multiSpecularCorr = multiSpecularRgx.search(nameFile)
        if multiSpecularCorr:
            nAOV['MULTISPECULAR'+str(count)] = nameNode

        multiLightRgx = re.compile('(\w)*'+'(ml|ML|m(ulti)?(l|L)ight(s)?)'+str(count)+'(\w)*')
        multiLightCorr = multiLightRgx.search(nameFile)
        if multiLightCorr:
            nAOV['MULTILIGHTS'+str(count)] = nameNode

        multiPrimaryRgx = re.compile('(\w)*'+'(prim|(p|P)rim(ary)?)'+'(\w)*')
        multiPrimaryCorr = multiPrimaryRgx.search(nameFile)
        if multiPrimaryCorr:
            nAOV['PRIMARY'] = nameNode

        multiPrimaryRgx = re.compile('(\w)*'+'(bounce|diffuseIndirect)'+'(\w)*')
        multiPrimaryCorr = multiPrimaryRgx.search(nameFile)
        if multiPrimaryCorr:
            nAOV['BOUNCE'] = nameNode

        multiPrimaryRgx = re.compile('(\w)*'+'(color)'+'(\w)*')
        multiPrimaryCorr = multiPrimaryRgx.search(nameFile)
        if multiPrimaryCorr:
            nAOV['COLOR'] = nameNode

        bgRgx = re.compile('N/A')
        bgCorr = bgRgx.search(nameFile)
        if bgCorr:
            nAOV['BG'] = nameNode

        holdoutRgx = re.compile('(\w)*'+'(id1|(h|H)old(out)?)'+'(\w)*')
        holdoutCorr = holdoutRgx.search(nameFile)
        if holdoutCorr:
            nAOV['HOLDOUT'] = nameNode

        count = count + 1


nameAOV = nAOV.keys()

#relightGrp = nuke.toNode(nuke.selectedNodes()[0].name())
print relightGrp.xpos()

currXpos = relightGrp.xpos()
currpos = relightGrp.xpos()

for nameAOV,nodeAOV in nAOV.items():
        
    if nameAOV == 'MULTIDIFFUSE0':
        relightGrp.setInput(10, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()-400)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)


    if nameAOV == 'MULTISPECULAR0':
        relightGrp.setInput(11, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()-300)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)
 

    if nameAOV == 'MULTIDIFFUSE1':
        relightGrp.setInput(9, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()-200)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)

    if nameAOV == 'MULTISPECULAR1':
        relightGrp.setInput(8, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()-100)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)

    if nameAOV == 'MULTIDIFFUSE2':
        relightGrp.setInput(7, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos())
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)

    if nameAOV == 'MULTISPECULAR2':
        relightGrp.setInput(6, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()+100)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)

    if nameAOV == 'MULTIDIFFUSE3':
        relightGrp.setInput(5, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()+200)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)

    if nameAOV == 'MULTISPECULAR3':
        relightGrp.setInput(4, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()+300)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)

    if nameAOV == 'MULTIDIFFUSE4':
        relightGrp.setInput(3, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()+400)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)

    if nameAOV == 'MULTISPECULAR4':
        relightGrp.setInput(2, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()+500)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)

    if nameAOV == 'MULTIDIFFUSE5': 
        relightGrp.setInput(13, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()+600)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)

    if nameAOV == 'MULTISPECULAR5': 
        relightGrp.setInput(14, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()+700)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)

    if nameAOV == 'MULTIDIFFUSE6': 
        relightGrp.setInput(15, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()+800)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)

    if nameAOV == 'MULTISPECULAR6': 
        relightGrp.setInput(16, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()+900)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)

    if nameAOV == 'MULTIDIFFUSE7': 
        relightGrp.setInput(17, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()+1000)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)

    if nameAOV == 'MULTISPECULAR7': 
        relightGrp.setInput(18, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()+1100)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-200)

    if nameAOV == 'HOLDOUT': 
        relightGrp.setInput(19, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()-200)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()+65)

    if nameAOV == 'PRIMARY': 
        relightGrp.setInput(1, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()-200)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-35)

    if nameAOV == 'BG': 
        relightGrp.setInput(12, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()+200)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-35)

    if nameAOV == 'BOUNCE': 
        relightGrp.setInput(0, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()+150)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-100)

    if nameAOV == 'COLOR': 
        relightGrp.setInput(12, nuke.toNode(nodeAOV))
        nuke.toNode(nodeAOV).setXpos(relightGrp.xpos()+250)
        nuke.toNode(nodeAOV).setYpos(relightGrp.ypos()-100)

