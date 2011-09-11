""" ###################################  goBackToMaya.py v0.8.1 Copyright (c) 2011 MPC #################################
	Despription:
	Go back values MD and MS intensity, ML color and intenisty to Maya light for have the same result between Nuke tweak and the new Maya primary pass.

	convert sRGB2Lin:
	pow( __getAttr(nukeValue)__ , 1/2.2 )

	Version:
	v0.8.1
	check if surfaceInteraction componant exist for each light

	v0.8
	Add a pulldown menu for select a differente light rig we have in Maya
	Clean up the script a bit

	v0.7
	externalise script and create a gizmo in nuke with everything in
	Add panel for select the Maya that will go back the value
	add regular expression for find the tklRManSurfaceInteractionLightComponent

	v0.6
	integration with the "relight" node
	Exception management and window message for problem or done

	v0.5
	connect the same port from Maya and Nuke for communicate

	v0.4
	Fix prob with instance.
	Mathematic operation betwwen Maya values and the new Nuke values.
	For the moment work only with one light rig.

	v0.3
	Bug with instance node and different node with the same name.

	v0.2
	Copy past values Nuke to Maya.

	v0.1
	First script, gather all the inforamtion to a file.
	Prob to go in Maya
"""

# TODO :
	# - need to figure out how to share the number of channels. : should be stored in
	# mayaValueUpdater ?

import os
import re
import socket
class MayaMessageSender(object):
	""" Class to send a message to Maya.

		:type host: string
		:param host: name of the machine hosting.
	"""
	def __init__(self, host):
		""" ctr.
		"""
		self.host = host
		#listing all maya
		self.maya = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#~ self.connect(self.port)

	def connect(self, port):
		""" Method to connect maya to a port.

			:type port: int
			:param port: number of the port you to want to connect to
		"""
		self.maya.connect((self.host, port))

	def send(self, message):
		""" Method to send a message to maya.

			:type message: string
			:param message: TODO

			:rtype: object
			:return: the maya you sent the message to.
		"""
		self.maya.send(message)

	def close(self):
		""" Method to close maya.
		"""
		self.maya.close()

class MayaValueUpdater(object):
	""" Class to update value in Maya from Nuke

		:type host: string
		:param host: name of the machine hosting.
	"""
	__noSurfaceInteractionWarning = 'STOP. No changes have been made as I was unable to tweak the diffuse and spec for some/all of your lights.'
	__noSurfaceInteractionWarning += 'Please add surface interaction components to all of your lights and try again.'

	__surfaceInteractionLightComponent ='tklRManSurfaceInteractionLightComponent'
	__surfaceInteractionLightComponents = [
		__surfaceInteractionLightComponent,
		'%s1' %__surfaceInteractionLightComponent
	]

	__tickleLightTypes = [
		'tklInfiniteAreaLight',
		'tklDistantLight',
		'tklSpotLight',
		'tklAreaLight'
	]

	_dictTickleParms = {
		'diffuse' : 'tklParmFdiffuseStrength',
		'specular' : 'tklParmFspecularStrength',
		'exposure' : 'tklParmFexposure',
		'tint' : 'tklParmCtintAdjust',
		'color' : 'tklParmClightColor',
	}



	@staticmethod
	def message(dictValues, lightRig):
		message = 'mayaValueUpdater = MayaValueUpdater(%s, %s);' %(dictValues or '', lightRig)
		message += 'mayaValueUpdater.updateValues()'
		message += '");'
		return message

	def __init__(self, dictValues, lightRig):
		""" ctr.
		"""
		self.__dictValues = dictValues
		self.__lightRig = lightRig

		self.__dictComponentFunctions = {
			'diffuse' : self.__diffuse,
			'specular' : self.__specular,
			'exposure' : self.__exposure,
			'tint' : self.__tint,
			'color' : self.__tint
		}

	def updateValues(self):
		"""
		"""
		import maya.cmds as cmds

		cmds.select(self.__lightRig)

		# what is this list ?
		list =  cmds.listRelatives(cmds.ls(sl=1), ad=True)

		listTickleLight = [cmds.listRelatives(node, p = True) for node in list if cmds.nodeType(node) in self.__tickleLightTypes]
		listTickleLightShape = [node for node in list if cmds.nodeType(node) in self.__tickleLightTypes]
		listTickleSurfInter = [cmds.listRelatives(node, p = True) for node in listTickleLight if cmds.nodeType(node) == self.__surfaceInteractionLightComponent ]


		detectSurfInter = []

		for node in listTickleLight:

			for item in cmds.listRelatives(node, ad = True):

				if cmds.nodeType(item) == self.__surfaceInteractionLightComponent:
					cmds.confirmDialog(
						title='surfInterComponent Problem',
						message=self.__noSurfaceInteractionWarning,
						button=['OK'],
						defaultButton='Yes',
						cancelButton='No',
						dismissString='No'
					)

		for node in listTickleLight:
			nodeShape = cmds.listRelatives(node)[0]
			MLcategorie = cmds.getAttr(nodeShape + '.tklParmSaovCategory')

			for component in cmds.listRelatives(node):
				componentShape = cmds.listRelatives(component)

				if cmds.nodeType(componentShape) in self.__surfaceInteractionLightComponents:
					surfInteractLightComp = componentShape[0]
					break

				# TODO : is that at the good indentation level ???

				#Mathematical operation, addtition or subtration, between the current value and the new value for each
				#That pick up the current version in maya and addition or subtract the difference between Maya and Nuke

				channel = 0
				while channel < 8 : # onlu 8 channels available.

					if MLcategorie == "multilight%s" %str(channel):
						for key, param in self._dictTickleParms.items():
							function = self.__dictComponentFunctions[key]

							if key in self.__dictValues.keys() :
								function(
									componentShape = componentShape,
									nodeShape = nodeShape,
									attribut = param,
									value = self.__dictValues[key]
								)


	def __diffuse(self, **kwargs):
		""" Method to set the diffuse tickle parameter.
			Needed keys :
				- componentShape
				- attribut
				- value

			:rtype: bool
			:return: True if the new value was set to the attribut, False otherwise.

			:raise: KeyError if missing key in kwargs
		"""
		return self.__multiply(
			kwargs['componentShape'],
			kwargs['attribut'],
			kwargs['value']
		)

	def __specular(self, **kwargs):
		""" Method to set the specular tickle parameter.
			Needed keys :
				- componentShape
				- attribut
				- value

			:rtype: bool
			:return: True if the new value was set to the attribut, False otherwise.

			:raise: KeyError if missing key in kwargs
		"""
		return self.__multiply(
			kwargs['componentShape'],
			kwargs['attribut'],
			kwargs['value']
		)

	def __exposure(self, **kwargs):
		""" Method to set the exposure tickle parameter.
			Needed keys :
				- nodeShape
				- attribut
				- value

			:rtype: bool
			:return: True if the new value was set to the attribut, False otherwise.

			:raise: KeyError if missing key in kwargs
		"""
		return self.__add(
			kwargs['nodeShape'],
			kwargs['attribut'],
			kwargs['value']
		)

	def __tint(self, **kwargs):
		""" Method to set the new values to the tint or color.
			The attribut needs to be a double3.
			Needed keys :
				- nodeShape
				- attribut
				- value : value here has to be a tuple !


			:rtype: bool
			:return: True if the new value was set to the attribut, False otherwise.
		"""
		attr = '%s.%s' %(
			kwargs['nodeShape'],
			kwargs['attribut']
		)
		values = kwargs['value']

		if cmds.objExists(attr):
			cmds.setAttr(
				attr,
				(cmds.getAttr(attr)[0][0]) * values[0],
				(cmds.getAttr(attr)[0][1]) * values[1],
				(cmds.getAttr(attr)[0][2]) * values[2],
				type = 'double3'
			)
			return True

		else :
			return False

	def __add(self, shape, attribut, value):
		""" Method to add the default value of the attribut and the value.
			The method will also set the result of the multiplication to the attribut.

			:type shape: string
			:param shape: name of the shape to work on.
			:type attribut: string
			:param attribut: name of the attribut to work on.
			:type value: int
			:param value: value to multiply with.

			:rtype: bool
			:return: True if the add and the set ran well, otherwise False
		"""
		attr = '%s.%s' %( shape, attribut)

		if cmds.objExists(attr):
			defaultValue = cmds.getAttr(attr)
			cmds.setAttr(attr, (defaultValue + value))
			return True

		else :
			return False

	def __multiply(self, shape, attribut, value):
		""" Method to multiply the default value of the attribut and the value.
			The method will also set the result of the multiplication to the attribut.

			:type shape: string
			:param shape: name of the shape to work on.
			:type attribut: string
			:param attribut: name of the attribut to work on.
			:type value: int
			:param value: value to multiply with.

			:rtype: bool
			:return: True if the multiplication and the set ran well, otherwise False
		"""
		attr = '%s.%s' %( shape, attribut)

		if cmds.objExists(attr):
			defaultValue = cmds.getAttr(attr)
			cmds.setAttr(attr, (defaultValue * value))
			return True

		else :
			return False

class GoBackToMaya(object):
	""" Go back values MD and MS intensity, ML color and intenisty to Maya light
		for have the same result between Nuke tweak and the new Maya primary pass.
	"""
	def __init__(self, host, nukeShot, job, fileIn):
		""" ctr.
		"""
		self.fileIn = fileIn
		self.host = host
		self.nukeShot = nukeShot
		self.job = job

		#~ self.__mayaMessageSender = MayaMessageSender(self.host)

	def listMaya(self):
		"""
		"""
		#list form port 9700 to  9711 the differente Maya opened

		mayaPorts = 11
		curr_port = 9700
		while curr_port < 9712 :
			try:
				mayaMessageSender = MayaMessageSender(self.host)
				mayaMessageSender.connect(curr_port)
				#~ message = 'python ("'
				#~ message += 'import mpc.maya.lightingTools.getFromMaya;'
				#~ message += 'getFromMaya.getLightingInformation()'
				#~ message += '")'

				message = 'python ("execfile(\'/usr/people/charles-c/Lighting/release/script/knowMayaPortLightRigShots.py\')");'
				mayaMessageSender.send(message)
				mayaMessageSender.close()

			except:
				mayaPorts -= 1

			curr_port += 1

		import time

		time.sleep(mayaPorts)

		self.listCurrMaya = set()
		mayaInfoFile = open("/tmp/mayaInfoLightRig.shot", "r")
		for line in mayaInfoFile.readlines():
			self.listCurrMaya.add(line)

		return self.listCurrMaya


	def listLightRig(self):
		""" After selected port, list all the differents lightRig exist in Maya
		"""
		for i in range(5):
			mayaMessageSender = MayaMessageSender(self.host)
			mayaMessageSender.connect(self.port[0])
			messagee = 'python ("execfile(\'/tmp/fileLightRig.py\')");' # update this to move module into project rather than tmp
			mayaMessageSender.send(message)
			mayaMessageSender.close()
			# why are you maya all the time ?
			#maya.close()
			# parce que probleme connection

			lightRigInfoFile = open("/tmp/knowLightRig.py", "r")
			self.listCurrLightRig = lightRigInfoFile.readlines()

		return self.listCurrLightRig

	def maya(self):
		"""
		"""
		self.listMaya()

		mayaInfoFile = open("/tmp/mayaInfoLightRig.shot", "r")
		self.listCurrMaya = mayaInfoFile.readlines()

		#replace the - by a space for have the correct structure for the pulldown menu in Nuke
		mayaList = ''
		for item in self.listCurrMaya:
			mayaList += item.replace(' ', '-')

		askPanel = nuke.Panel('Select a Maya')
		askPanel.addEnumerationPulldown("send to: ", mayaList)
		val = askPanel.show()

		if val:
			self.port = int(askPanel.value("send to: ").split('-')[1])
			self.lightRig = askPanel.value("send to: ").split('-')[2:]

		else:
			return askPanel.value(str(0))
			self.cleanFiles()



		# when there is only one light rig, we autoselect it,
		# and when there is several light rigs, we allow the use to select the light rig he wants

		# TODO : When there is no light rig, we should avoid to goBackToMaya.
		if len(self.lightRig) == 1:
			self.curr_lightRig = self.lightRig[0]

		elif len(self.lightRig) != 1:
			chooseLightRig = ' '.join(str(item) for item in self.lightRig)
			askPanelLightRig = nuke.Panel('Select a lightRig')
			askPanelLightRig.addEnumerationPulldown("lightRig: ", chooseLightRig )
			valLightRig = askPanelLightRig.show()

			if valLightRig:
				self.curr_lightRig = askPanelLightRig.value("lightRig: ")

			else:
				print 'cancel'
				self.cleanFiles()
		else :
			pass


		self.goBackToMaya()

	def goBackToMaya(self):
		"""
		"""
		mayaMessageSender = MayaMessageSender(self.host)
		mayaMessageSender.connect(self.port)

		mayaMessageSender.send(
			MayaValueUpdater.message(
				self.__listValues(),
				self.curr_lightRig
			)
		)

		mayaMessageSender.close()

	def __getMultiDiffuseIntensity(self, name, channel):
		"""
		"""
		return str(nuke.toNode('%s.MD%s_intensity' %(name, str(channel))).knob('value').value())

	def __getMultiSpecularIntensity(self, name, channel):
		"""
		"""
		return str(nuke.toNode('%s.MS%s_intensity' %(name, str(channel))).knob('value').value())

	def __getMultiExposureIntensity(self, name, channel):
		"""
		"""
		# TODO : why red ?

		return str(nuke.toNode('%s.ML%s_intensity' %(name, str(channel))).knob('red').value())

	def __getTints(self, name, channel):
		"""
		"""
		knob = nuke.toNode('%s.ML%s_color' %(name, str(channel))).knob('value')
		return (
			str(knob.value()[0]),
			str(knob.value()[1]),
			str(knob.value()[2])
		)


	def __listValues(self):
		"""
		"""
		relightGrp = nuke.thisNode()
		currSelect = nuke.allNodes(group=relightGrp)
		name = relightGrp.name()

		# what happen if several nodes are selected ?
		currSelectName = [item.name() for item in currSelect]

		dictValues = {}

		dictTickleParms = MayaValueUpdater._dictTickleParms

		channel = 0
		while channel < 8 :
			tints = self.__getTints(name, channel)

			dictValues[channel] = {
				dictTickleParms['diffuse'] : self.__getMultiDiffuseIntensity(name, channel),
				dictTickleParms['specular'] : self.__getMultiSpecularIntensity(name, channel),
				dictTickleParms['exposure'] : self.__getMultiExposureIntensity(name, channel),
				dictTickleParms['tint'] : tints,
				dictTickleParms['color'] : tints,

			}

			channel += 1

		return dictValues

	def cleanFiles(self):
		"""
		"""
		if os.path.exists('/tmp/mayaInfoLightRig.shot'):
			os.remove('/tmp/mayaInfoLightRig.shot')
			return True

		else :
			return False

def fetchLightRigs():
	""" Fetch the light rigs from maya
	"""
	# need comment !!!
	mayaFile = "/tmp/mayaInfoLightRig.shot"
	if not os.path.exists(mayaFile):
		mayaFile = open("/tmp/mayaInfoLightRig.shot", "w")

	goBackToMaya = GoBackToMaya(
		host = os.environ['HOSTNAME'],
		nukeShot = os.environ['SHOT'],
		job = os.environ['JOB'],
		fileIn = '/tmp/fileToMaya.py'
	)

	goBackToMaya.maya()
	os.remove('/tmp/mayaInfoLightRig.shot')


fetchLightRigs()
