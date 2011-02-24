# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from everyoneCan import CustomWidgets as cw
    
    
class Naming(QtGui.QWidget):
    """interface to set a new value"""
    #==========================================================================
    # constants
    #==========================================================================
    __TITLE = 'Set Name'
    __NEW_NAME_LABEL = 'Name :'
    __PUSH_BUTTON_NAME = 'OK'
        
    def __init__(self, sCurrentName, parent= None):
        """
        @type sCurrentName: string
        @param sCurrentName: value of the parameter you want to change
        """
        self.__sCurrentName = sCurrentName
        QtGui.QWidget.__init__(self,parent)
        self.__oMainLayout = QtGui.QVBoxLayout()
        self.setWindowTitle(self.__TITLE)
        self.__widgets()
        self.__oMainLayout.addStretch(1)
        self.setLayout(self.__oMainLayout)
        

    def getValue(self):
        """
        Method to get the value of the interface
        @rtype: Qt String
        @requires: new value
        """
        self.deleteLater() #kill the interface
        return self.__oLineEditName.text()
                
    def __widgets(self):
        """
        Creation of the interface
        QTCore.SIGNAL : 'Naming_nameSet'
        """
        def __emitSignal():
            self.emit(QtCore.SIGNAL('Naming_nameSet'))
            
        self.__oLineEditName = QtGui.QLineEdit(self.__sCurrentName)
        self.connect(self.__oLineEditName,QtCore.SIGNAL("returnPressed()"),
                     __emitSignal)
        self.__oNewNameGrpLabel = cw.AlGroupLabel(
                                        self.__NEW_NAME_LABEL,
                                        self.__oLineEditName)
        self.__oPushButtonLayout = QtGui.QHBoxLayout()
        self.__oRenameButton = QtGui.QPushButton(self.__PUSH_BUTTON_NAME)
        self.connect(self.__oRenameButton, QtCore.SIGNAL('clicked()'),
                     __emitSignal)
        self.__oPushButtonLayout.addStretch(1)
        self.__oPushButtonLayout.addWidget(self.__oRenameButton)

        self.__oMainLayout.addWidget(self.__oNewNameGrpLabel)
        self.__oMainLayout.addLayout(self.__oPushButtonLayout)

# Ni!   