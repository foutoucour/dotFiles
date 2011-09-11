import socket

from mpc.nukeSee.tcpService import TcpService

class TcpClient(TcpService):
	""" Class to set a TCP client.

		:type host: string
		:param host: Host to connect to. Default: local host
	"""
	def __init__(self, host = socket.gethostname()):
		""" ctr.
		"""
		TcpService.__init__(self, host)

	def connect(self, port):
		""" Method to connect the client to a TCP server listening the port.
			:type port: int
			:param port: port to connect to
		"""
		self._socket.connect((self._host, port))
		self.serverMessage = self._socket.recv(1024)
		self._socket.send(self.message(self.serverMessage))

	def message(self, message):
		""" Method to set the process to do before to send back the message to the server

			:type message: string or buffer
			:param message: message to process.

			:rtype: message or buffer
			:return: message to send back to the server
		"""
		return 'message from the client'


if __name__ == '__main__':
	c = ClientTCP()
	sClientMessage = c.connect(12345)
	clientMessage = eval(sClientMessage)
	c.close()
