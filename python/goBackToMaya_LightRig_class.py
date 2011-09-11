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
from mpc.nukeSee.messenger import Messenger

class GoBackToMaya(object):
	""" Go back values MD and MS intensity, ML color and intenisty to Maya light
		for have the same result between Nuke tweak and the new Maya primary pass.
	"""
	@staticmethod
	def getSocket():
		return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def __init__(self, host, nukeShot, job, fileIn):
		""" ctr.
		"""
		self.fileIn = fileIn
		self.host = host
		self.nukeShot = nukeShot
		self.job = job

	def listMaya(self):
		""" List form port 9700 to  9711 the differente Maya opened.
		"""

		mayaPorts = set()

		curr_port = 9700
		while curr_port < 9712 :
			try:
				s = self.getSocket()

				# the binding will error if the port is already used
				# and we know that these ports are used by Maya.
				s.bind((host, curr_port))
			except:
				mayaPorts.add(curr_port)

			curr_port += 1

		messages = []

		for port in mayaPorts :
			client = self.getSocket()
			client.connect((self.host, maya))
			client.send(message)
			client.recv(1024)
			client.close()

		print messages

		#self.listCurrMaya = set()
		#mayaInfoFile = open("/tmp/mayaInfoLightRig.shot", "r")
		#for line in mayaInfoFile.readlines():
			#self.listCurrMaya.add(line)

		return self.listCurrMaya

	def listLightRig(self):
		""" After selected port, list all the differents lightRig exist in Maya
		"""
		for i in range(5):
			mayaMessageSender = MayaMessageSender(self.host)
			mayaMessageSender.connect(self.port[0])
			message = 'python ("execfile(\'/tmp/fileLightRig.py\')");' # update this to move module into project rather than tmp
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
