import socket

import os
import re

class MayaSniffer(object):
	""" Class to find and extract details of maya light rigs.
	"""
	def __init__(self, host, port):
		"""
		"""
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect((host, port))

		self.client.send('python("import maya.cmds as cmds");\n')
		self.client.send('python("import re");\n')
		self.client.send('python("reg = re.compile(\'lightRig\')");\n')

		self.dictDetails = { }
		self.getLightRigs()

	def getLightRigs(self):
		message = 'string $rig[] = python("[ node for node in cmds.ls(type = \'transform\') if reg.search(node) ]");\n'
		self.client.send(message)
		self.lightRigs = self.client.recv(1024)

	def getResults(self):
		return {'lightRigs':self.lightRigs}


