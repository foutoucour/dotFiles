import socket

class TcpService(object):
	""" Definition of a tcp Service.

		:type host: string
		:param host: Host to connect to.
	"""
	def __init__(self, host):
		""" ctr.
		"""
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._host = host

	def close(self):
		""" Method to close the TCP client.
		"""
		self._socket.close()


# Ni !
