def comment():
	###########################  goBackToMaya.py v0.8 Copyright (c) 2011 MPC ######################## 

	#Despription:
	#Go back values MD and MS intensity, ML color and intenisty to Maya light for have the same result between Nuke tweak and the new primary pass.

	#convert sRGB2Lin:
	#pow( __getAttr(nukeValue)__ , 1/2.2 )

	#Version:
	#v0.8.1
	#check if surfaceInteraction componant exist for each light
	
	#v0.8
	#Add a pulldown menu for select a differente light rig we have in Maya
	#Clean up the script a bit
	
	#v0.7
	#externalise script and create a gizmo in nuke with everything in
	#Add panel for select the Maya that will go back the value
	#add regular expression for find the tklRManSurfaceInteractionLightComponent

	#v0.6
	#integration with the "relight" node
	#Exception management and window message for problem or done

	#v0.5
	#connect the same port from Maya and Nuke for communicate

	#v0.4
	#Fix prob with instance.
	#Mathematic operation betwwen Maya values and the new Nuke values.
	#For the moment work only with one light rig.

	#v0.3
	#Bug with instance node and different node with the same name.

	#v0.2
	#Copy past values Nuke to Maya.

	#v0.1
	#First script, gather all the inforamtion to a file.
	#Prob to go in Maya
	pass



#################################### Start Script ######################################



import socket, os, re

class GoBackToMaya:
	
	def __init__(self, host, nukeShot, job, fileIn):
		#import class for dev
		#execfile('/usr/people/charles-c/Lighting/release/script/MayaLightDev_dev.py')
		#mld = MayaLightDev()

		self.fileIn = fileIn
		self.host = host
		self.nukeShot = nukeShot
		self.job = job
		
	def launcher(self):
		if os.path.exists('/tmp/mayaInfoLightRig.shot'):
			self.maya()
		else:
			pass
	

	def regExp(self,pattern, items):
		
		matchPattern= []
		for item in items:
			rgx = re.compile(pattern)
			corr = rgx.search(item)
			if corr:
				matchPattern.append(corr.group(0))
		return matchPattern		
		
	def listMaya(self):
		

		#list form port 9700 to  9711 the differente Maya opened
		for curr_port in range(9700, 9711):
			try:
				maya = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				maya.connect((self.host, curr_port))
				message = 'python ("execfile(\'/usr/people/charles-c/Lighting/release/script/knowMayaPortLightRigShots.py\')");'
				maya.send(message)
				maya.close()
			except:
				pass

		mayaInfoFile = open("/tmp/mayaInfoLightRig.shot", "r")
		self.listCurrMaya = mayaInfoFile.readlines()

		return self.listCurrMaya

		
		
	def listLightRig(self):
		
		#list form port selected  the differente lightRig exist
		for i in range(5):
			mayaa = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			mayaa.connect((self.host, int(self.port[0])))
			messagee = 'python ("execfile(\'/tmp/fileLightRig.py\')");'
			mayaa.send(messagee)
			mayaa.close()
			
			lightRigInfoFile = open("/tmp/knowLightRig.py", "r")
			self.listCurrLightRig = lightRigInfoFile.readlines()
		return self.listCurrLightRig 

		
	def maya(self):

		self.listMaya()
		#self.listLightRig()
		#self.port = listMaya()[0]
		#print self.port 

		#replace the - by a space for have the correct structure for the pulldown menu
		mayaList = ''
		for item in self.listCurrMaya:
			#print item
			mayaList += item.replace(' ', '-')#.split(' ')[0:1]
			#mayaList += mayaList.split(' ' )[0:1]
		mayaList[:-1]
		print mayaList
		
		
		askPanel = nuke.Panel('Select a Maya')
		askPanel.addEnumerationPulldown("send to: ", mayaList)
		val = askPanel.show()
		
		if val:
			self.port = askPanel.value("send to: ").split('-')[1]
			self.lightRig = askPanel.value("send to: ").split('-')[2:]

			#self.cleanFiles
			
		else:
			return askPanel.value(str(0))
			self.cleanFiles()
			
		
		if len(self.lightRig) != 1:
			chooseLightRig = ' '.join(str(item) for item in self.lightRig)
			askPanelLightRig = nuke.Panel('Select a lightRig')
			askPanelLightRig.addEnumerationPulldown("lightRig: ", chooseLightRig )
			valLightRig = askPanelLightRig.show()
			
			if valLightRig:
				self.curr_lightRig = askPanelLightRig.value("lightRig: ")
				#print 'current light rig choosed: ' + self.curr_lightRig
				
			else:
				print 'cancel'
				self.cleanFiles()
				
		else:
			self.curr_lightRig = self.lightRig[0]
			#print 'current light rig by default is: ' + self.lightRig[0]
				

			
		print 'current light rig choosed: ' + self.curr_lightRig			
		print 'current port used: ' + self.port
		
		self.goBackToMaya()
		#self.cleanFiles()
		'''
		for item in self.listCurrMaya:
			print item.split(' ')[2:]
		'''
		#print self.listLightRig()


	def goBackToMaya(self):
		
		#port = listMayaShotsPorts()[0]
		maya = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		maya.connect((self.host,int(self.port)))
		relightGrp = nuke.thisNode()
		currSelect = nuke.allNodes(group=relightGrp)
		currSelectName = [item.name() for item in currSelect]

		#list MultiLIght in Maya
		nLight = self.regExp('ML' + '(\d){1}' +'_intensity'+'(\w+)?', currSelectName)

		#list MultiLIght in Maya
		fileW = open(self.fileIn, "w")
		fileW.write("import maya.cmds as cmds\n")
		fileW.write("def goBackToMayaCore4():\n")
		fileW.write("    curr_lightRig = '"+ self.curr_lightRig +"'\n")
		fileW.write("    cmds.select(curr_lightRig)\n")
		fileW.write("    list =  cmds.listRelatives(cmds.ls(sl=1), ad=True)\n")
		fileW.write("    listTickleLight = [cmds.listRelatives(node, p = True) for node in list if cmds.nodeType(node) in ['tklInfiniteAreaLight', 'tklDistantLight', 'tklSpotLight','tklAreaLight']]\n")
		fileW.write("    listTickleLightShape = [node for node in list if cmds.nodeType(node) in ['tklInfiniteAreaLight', 'tklDistantLight', 'tklSpotLight','tklAreaLight']]\n")
		fileW.write("    listTickleSurfInter = [cmds.listRelatives(node, p = True) for node in listTickleLight if cmds.nodeType(node) in ['tklRManSurfaceInteractionLightComponent']]\n")
		fileW.write("    detectSurfInter = []\n")
		fileW.write("    for node in listTickleLight:\n")
		fileW.write("        for item in cmds.listRelatives(node, ad = True):\n")
		fileW.write("    		if cmds.nodeType(item) == 'tklRManSurfaceInteractionLightComponent':\n")
		fileW.write("    			detectSurfInter.append('noExist')\n")
		fileW.write("    if len(detectSurfInter) != len(listTickleLight):\n")
		fileW.write("    	cmds.confirmDialog( title='surfInterComponent Problem', message='STOP. No changes have been made as I was unable to tweak the diffuse and spec for some/all of your lights. Please add surface interaction components to all of your lights and try again.', button=['OK'], defaultButton='Yes', cancelButton='No', dismissString='No' )\n")
		fileW.write("    else:\n")
		fileW.write("        for node in listTickleLight: \n")
		fileW.write("            nodeShape = cmds.listRelatives(node)[0]\n")
		fileW.write("            MLcategorie = cmds.getAttr(nodeShape + '.tklParmSaovCategory')\n")
		fileW.write("            for component in cmds.listRelatives(node):\n")
		fileW.write("                componentShape = cmds.listRelatives(component)\n")
		fileW.write("                print componentShape\n")
		fileW.write("                try:\n")
		fileW.write("                    if cmds.nodeType(componentShape) == 'tklRManSurfaceInteractionLightComponent':\n")
		fileW.write("                        surfInteractLightComp = componentShape\n")
		fileW.write("                except:\n")
		fileW.write("                    if cmds.nodeType(componentShape) == 'tklRManSurfaceInteractionLightComponent1':\n")
		fileW.write("                        surfInteractLightComp = componentShape\n")


		#Mathematical operation, addtition or subtration, between the current value and the new value for each
		#That pick up the current version in maya and addition or subtract the difference between Maya and Nuke
		for ML_n in range(len(nLight)):
			fileW.write("            if MLcategorie == \"multilight"+ str(ML_n)+"\":\n")

		#Diffuse and  Specularity intensity
			try:
				if str(nuke.toNode(relightGrp.name()+'.MD'+str(ML_n)+'_intensity').knob('value').value()) is not None:
					fileW.write("                cmds.setAttr(surfInteractLightComp[0] + '.tklParmFdiffuseStrength', (cmds.getAttr(surfInteractLightComp[0] + '.tklParmFdiffuseStrength'))*"+str(nuke.toNode(relightGrp.name()+'.MD'+str(ML_n)+'_intensity').knob('value').value())+")\n")
			except:
				pass

			try:
				if str(nuke.toNode(relightGrp.name()+'.MS'+str(ML_n)+'_intensity').knob('value').value()) is not None:
					fileW.write("                cmds.setAttr(surfInteractLightComp[0] + '.tklParmFspecularStrength', (cmds.getAttr(surfInteractLightComp[0] + '.tklParmFspecularStrength'))*"+str(nuke.toNode(relightGrp.name()+'.MS'+str(ML_n)+'_intensity').knob('value').value())+")\n")
			except:
				pass

		#MultiLight intensity
			try:
				if str(nuke.toNode(relightGrp.name()+'.ML'+str(ML_n)+'_intensity').knob('red').value()) is not None:
					fileW.write("                cmds.setAttr(nodeShape + '.tklParmFexposure', cmds.getAttr(nodeShape + '.tklParmFexposure')" +"+"+str(nuke.toNode(relightGrp.name()+'.ML'+str(ML_n)+'_intensity').knob('red').value())+")\n")
			except:
				pass

			#MultiLight color
			try:
				if str(nuke.toNode(relightGrp.name()+'.ML'+str(ML_n)+'_color').knob('value').value()[1]) is not None:
					fileW.write("                try:\n")
					fileW.write("                    cmds.setAttr(nodeShape + '.tklParmCtintAdjust', (cmds.getAttr(nodeShape + '.tklParmCtintAdjust')[0][0])*"+str(nuke.toNode(relightGrp.name()+'.ML'+str(ML_n)+'_color').knob('value').value()[0])+", (cmds.getAttr(nodeShape + '.tklParmCtintAdjust')[0][1])*"+str(nuke.toNode(relightGrp.name()+'.ML'+str(ML_n)+'_color').knob('value').value()[1])+", (cmds.getAttr(nodeShape + '.tklParmCtintAdjust')[0][2])*"+str(nuke.toNode(relightGrp.name()+'.ML'+str(ML_n)+'_color').knob('value').value()[2])+", type='double3')\n")
					fileW.write("                except:\n")
					fileW.write("                    cmds.setAttr(nodeShape + '.tklParmClightColor', (cmds.getAttr(nodeShape + '.tklParmClightColor')[0][0])*"+str(nuke.toNode(relightGrp.name()+'.ML'+str(ML_n)+'_color').knob('value').value()[0])+", (cmds.getAttr(nodeShape + '.tklParmClightColor')[0][1])*"+str(nuke.toNode(relightGrp.name()+'.ML'+str(ML_n)+'_color').knob('value').value()[1])+", (cmds.getAttr(nodeShape + '.tklParmClightColor')[0][2])*"+str(nuke.toNode(relightGrp.name()+'.ML'+str(ML_n)+'_color').knob('value').value()[2])+", type='double3')\n")
			except:
				pass

		fileW.write("goBackToMayaCore4()\n")

		#close write file
		#execution of the script in Maya
		message = 'python ("execfile(\''+self.fileIn+'\')");'

		maya.send(message)
		maya.close()

		#nuke.message("All values was go back into Maya")
		
		#delete the file with the listPort of Maya
		#os.system('rm /tmp/mayaInfo.shot')
		

	def cleanFiles(self):
		
		print 'function cleanFiles'

		try:
			os.system('rm /tmp/mayaInfoLightRig.shot')
		except:
			print 'pouet'


	'''
	try:
		port = listMayaShotsPorts()[0]
		maya = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		maya.connect((host,int(port)))
		print port
		goBackToMaya()
		os.system('rm /tmp/mayaInfo.shot')
	except:
		os.system('rm /tmp/mayaInfo.shot')
		pass
		#raise TypeError('User cancel')

		
	try:
		os.system('rm /tmp/mayaInfoLightRig.shot')
	except:
		pass
	'''
	
#goBackToMaya = GoBackToMaya(host = os.environ['HOSTNAME'], nukeShot = os.environ['SHOT'], job = os.environ['JOB'], fileIn = '/tmp/fileToMaya.py')
#goBackToMaya.maya()

try:
	goBackToMaya = GoBackToMaya(host = os.environ['HOSTNAME'], nukeShot = os.environ['SHOT'], job = os.environ['JOB'], fileIn = '/tmp/fileToMaya.py')
	goBackToMaya.maya()
	os.system('rm /tmp/mayaInfoLightRig.shot')
except:
	os.system('rm /tmp/mayaInfoLightRig.shot')
	nuke.message('Please try again...')
