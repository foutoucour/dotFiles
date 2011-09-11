import threading
import socket
import sys
sys.path.append("/Users/jordiriera/Documents/nukeLight")
from clientTCP import ClientTCP

class ThreadClass(threading.Thread):
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
        s = ServerTcp(self._port)
        self.serverInitialised = True
        s.sendMessage(self._message)

class ServerTcp(object):
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
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._host = host
        self._port = port

        self.bufferSize = 1024
        self.__socket.bind((self._host, self._port))
        self.__socket.listen(5)

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
            client, address = self.__socket.accept()
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
            self.__socket.close()

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

if __name__ == '__main__':
    # Launching a server in a thread.
    t = ThreadClass(12345, 'on')
    t.start()

    # Waiting that the server is initialised
    # then we launch the client.
    while not t.serverInitialised:
        pass
    else :
        import time
        print 'sleeping'
        time.sleep(5)
        print 'go'
        c = ClientTCP()
        c.connect(t._port)
        c.close()


