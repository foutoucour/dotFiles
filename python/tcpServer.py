import threading
import socket

from mpc.nukeSee.tcpService import TcpService
from mpc.nukeSee.tcpClient import TcpClient

class TcpServerThread(threading.Thread):
	""" Class to launch a TCP server in a thread.

		:type port: int
		:param port: port to connect to.
		:type message: string or buffer
		:param message: message to send to the client
	"""
	def __init__(self, port, message):
		""" ctr.
		"""
		# Variable to check the state of the server.
		self.serverInitialised = False

		self._message = message
		self._port = port
		threading.Thread.__init__(self)

	def run(self):
		""" Method running the server.
		"""
		s = TcpServer(self._port)
		self.serverInitialised = True
		s.sendMessage(self._message)

class TcpServer(TcpService):
	""" Class to set a TCP server.
		The server will open a port,

		:type port: int
		:param port: port to connect to
		:type host: string
		:param host: Host to connect to. Default: local host
	"""
	def __init__(self, port, host = socket.gethostname()):
		""" ctr.
		"""
		TcpService.__init__(self, host)
		self._port = port

		self.bufferSize = 1024
		self._socket.bind((self._host, self._port))
		self._socket.listen(5)

	def sendMessage(self, message, backlog=5):
		""" Method looping while waiting for a client to connect.
			Once connected, the server send to the client a message
			and then wait for the client to send back a message.

			:type message: string or buffer
			:param message: message to send.
			:type backlog: int
			:param backlog: number to client to wait for at max. Default 5
			:rtype: string or buffer
			:return: message fron the client we connect to.
		"""
		# We are here waiting for the client to get us a message back
		# in answer to our message.
		clientMessage = ''
		loopCounter = 0

		while not clientMessage:
			# Checking for a client connected to the port.
			# If there is no client, we just loop again and again.
			client, address = self._socket.accept()
			print 'Got connection from', address

			# sending to the connected client the message we want it to process
			client.send(message)
			print 'sent', message

			# Getting the message from the client.
			clientMessage = client.recv(1024)

			# And closing it.
			client.close()
		else :
			print 'received', clientMessage
			self.close()

		return clientMessage

class Message(object):
	@staticmethod
	def getInstance():
		return '__import__("serverTcp").Message()'

	def __init__(self):
		self.dict = {
			'start' : 'begin'
		}

	def getStringDict(self):
		return str(self.dict)

def main():
	# Launching a server in a thread.
	t = TcpServerThread(12345, 'Server')
	t.start()

	# Waiting that the server is initialised
	# then we launch the client.
	while not t.serverInitialised:
		pass
	else :
		c = TcpClient()
		c.connect(t._port)
		c.close()

if __name__ == '__main__':
	main()

