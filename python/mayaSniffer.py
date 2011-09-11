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

		self.dictDetails = {
			'lightRigs': self.getLightRigs()
		}

	@staticmethod
	def toList(string):
		string = string.replace('\n\x00', '')
		string = string.replace('\t',' ')
		return string.split(' ')

	def getLightRigs(self):
		message = 'python("[ node for node in cmds.ls(type = \'transform\') if reg.search(node) ]");\n'
		self.client.send(message)
		return self.toList(self.client.recv(1024))

	def getResults(self):
		return self.dictDetails

