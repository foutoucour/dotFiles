#!/usr/bin/python

import socket

class clientTCP(object)

    def __init__(self, port, host = None):
        self.__socket = socket.socket()
        self._host = host or socket.gethostname()
        self._port = port

    def connect(self):
        self.__socket.connect((self._host, self._port))
        return s.recv(1024)

    def close(self):
        self.__socket.close()

