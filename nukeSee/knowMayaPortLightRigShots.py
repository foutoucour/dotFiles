import os
import maya.cmds as cmds
import maya.mel as mel

shotMaya = os.environ['SHOT']
portMaya = str(mel.eval("int $test = $mpcPortId;"))
listGroup = [node for node in cmds.ls() if cmds.nodeType(node) in ['transform']]
	
def regExp(pattern, items):
	matchPattern= []
	for item in items:
		rgx = re.compile(pattern, re.IGNORECASE)
		corr = rgx.search(item)
		if corr:
			matchPattern.append(corr.group(0))
	return matchPattern
	
listLightRig = regExp('(\w+)?lightrig(\w+)*', listGroup)
'''
fileInLightRig = '/tmp/knowLightRig.py'
fileY = open(fileInLightRig, "w")
for item in listLightRig:
    fileY.write(item+"\n")         
    print item
'''

text = shotMaya + " " + portMaya + ' ' + ' '.join(str(item) for item in listLightRig)


os.system('echo "'+ text +'">>/tmp/mayaInfoLightRig.shot')