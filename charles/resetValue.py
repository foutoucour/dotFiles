import socket
import os
import re

matchPattern = []
nLight = []
relightGrp = nuke.thisNode()

currSelect = nuke.allNodes(group=relightGrp)
nLight = []
for x in currSelect:
    rgx = re.compile('ML' + '(\d){1}' +'_intensity'+'(\w+)?')
    corr = rgx.search(x.name())
    if corr:
        nLight.append(corr.group(0))



#nLight = list(set(nLight))

for ML_n in range(8):
	try:
		nuke.toNode(relightGrp.name()+'.MD'+str(ML_n)+'_intensity').knob('value').setValue(1)
	except:
		pass
	try:
		nuke.toNode(relightGrp.name()+'.MS'+str(ML_n)+'_intensity').knob('value').setValue(1)
	except:
		pass
	try:
		nuke.toNode(relightGrp.name()+'.ML'+str(ML_n)+'_color').knob('value').setValue([1,1,1,1])
	except:
		pass
	try:
		nuke.toNode(relightGrp.name()+'.ML'+str(ML_n)+'_intensity').knob('red').setValue(0)
	except:
		pass
	try:
		nuke.toNode(relightGrp.name()+'.ML'+str(ML_n)+'_intensity').knob('green').setValue(0)
	except:
		pass
	try:
		nuke.toNode(relightGrp.name()+'.ML'+str(ML_n)+'_intensity').knob('blue').setValue(0)
	except:
		pass


#nuke.thisNode().knob("relightStatus").setValue("<FONT COLOR=\"#00FF00\">lighting updated!<\FONT>")
#node["cacheStatus"].setValue("<FONT COLOR=\"#00FF00\">Cache updated!<\FONT>")

for curr_number in range(8):
	nuke.thisNode().knob("ml" + str(curr_number) + "_initial").setValue(0)
	nuke.thisNode().knob("MD" + str(curr_number) + "_neutral").setValue(0)
	nuke.thisNode().knob("MS" + str(curr_number) + "_neutral").setValue(0)
	nuke.thisNode().knob("MC" + str(curr_number) + "_neutral").setValue(0)
	nuke.thisNode().knob("ME" + str(curr_number) + "_neutral").setValue(0)
