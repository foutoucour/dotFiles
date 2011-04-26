# inly core 
from PyQt4 import QtCore


class Control:
    def __init__(self, oGui ):
        self.Gui = oGui
        self.__signals()
        self.__checkLineEditStates()
        self.Gui.show()

    def __signals(self):
        QtCore.QObject.connect(self.Gui,
                                QtCore.SIGNAL('buttonPush'),
                                self.__setFromSelection)

