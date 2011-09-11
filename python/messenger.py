from mpc.nukeSee.tcpServer import TcpServerThread
from mpc.nukeSee.tcpClient import TcpClient

class Messenger(object):
	"""
	"""
	def __init__(self, port, message):
		"""
		"""
		self.__port = port
		self.__message = message

	def send(self):
		thread = TcpServerThread(
			self.__port,
			self.__message
		)

		thread.start()

		# Waiting that the server is initialised
		# then we launch the client.
		while not thread.serverInitialised:
			pass

		else :
			client = TcpClient()
			client.connect(self.__port)
			client.close()
			thread.server.close()

		return thread.received

# Ni !
