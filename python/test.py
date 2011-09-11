import socket
from telnetlib import Telnet
import os

from mpc.nukeSee.mayaSniffer import MayaSniffer
#from mpc.nukeSee.messenger import Messenger

def listing():
	host = os.getenv('HOSTNAME')


	mayaPorts = 11
	curr_port = 9700

	mayas = []
	while curr_port < 9712 :
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			s.bind((host, curr_port))
		except :
			mayas.append(curr_port)
		s.close()
		curr_port += 1



	for maya in mayas:

		mayaSniffer = MayaSniffer(host, maya)
		print mayaSniffer.getResults()
		#print client.recv(1024)

		#client.send('python("cmds.sphere()");')
		#print client.recv(1024)
		#client.send('python("import os;os.name");')
		#print client.recv(1024)

		#client.send('python("import os;os.getenv(\'USER\')");')
		#print client.recv(1024)

listing()

