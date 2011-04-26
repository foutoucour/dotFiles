from PyQt4 import QtGui
from PyQt4 import QtCore


class UI(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Project')

        push = QtGui.QPushButton('Push me')
        self.connect.(push, 
                      QtCore.SIGNAL('clicked()'),
                      self.__pushEmit)


    def __pushEmit(self):
        self.emit(QtCore.SIGNAL('buttonPushed'))



