# -*- coding: utf-8 -*-
import sys
import os

from PyQt4 import QtGui
from PyQt4 import QtCore

from everyoneCan import CustomWidgets as cw
from everyoneCan import SharedConstants
scc                         = SharedConstants.Constants()

import lightingOutliner

class AllOthersUIWidget(QtGui.QWidget):
    """class to create a pack of buttons to launch other ec tools"""
    def __init__(self, sLauncher, sDisplay='H'):
        """
        @type sLauncher: string
        @param sLauncher: __name__ of the tool
        @type sDisplay: integer boolean
        @param sDisplay: 'H' to horizontal(default), 'V' to vertical                       
        """
        def __lightingOutliner_onClicked():
            """
            Control of the lightingOutliner push button.
            Create a new outliner with only lights 
            and blockers and shadowCameras.
            """
            lightingOutliner.Call()
            
        self.__listModules = []
        # we doesn't want to have the tool which launched
        # ec__UIs in the list so we compare with the string sLauncher
        # which is basicly the __name__ of the UI
        sLauncher = sLauncher.lower() #avoiding all syntax issue
        # ec tools are in folder upon the folder containing
        # ec__UIs
        # each folder got a file ec__"folder"Options.py which is the
        # launcher of the tool
        sCurrentDir = os.path.dirname(__file__)
        
        for sFile in os.listdir(sCurrentDir):
            if not sFile == '.svn' and not sFile in sLauncher:
                sDirFile = os.path.join(sCurrentDir, sFile)
                if os.path.isdir(sDirFile):
                    self.__listModules.append(sFile)
                    
        QtGui.QWidget.__init__(self)
        if sDisplay == 'H':
            self.__oMainLayout = QtGui.QHBoxLayout()
        else :
            self.__oMainLayout = QtGui.QVBoxLayout()
        self.__oMainLayout.setContentsMargins(0,0,0,0)
        self.__oLightingOutliner = cw.AlIconPushButton(
                                '%s/lightingOutliner.jpg' %scc.ICON_PATH, 
                                'Lighting Outliner')
        QtCore.QObject.connect(self.__oLightingOutliner,
                               QtCore.SIGNAL('clicked()'),
                               __lightingOutliner_onClicked)
        self.__oMainLayout.addWidget(self.__oLightingOutliner)
        for sModule in self.__listModules:
            self.__oPush = self.__CreatePushButton(sModule)
            self.__oMainLayout.addWidget(self.__oPush)
        self.__oMainLayout.addStretch(1)
        self.setLayout(self.__oMainLayout)
        
            
    class __CreatePushButton(cw.AlIconPushButton):
        def __init__(self,sName):
            def __pushButton_onClicked():
                # name of the module to import
                sModulePath = '%s.%s' %(self.__sModule, self.__sFile)
                # import the module
                __import__(sModulePath)
                # loading module in sys 
                oModule = sys.modules[sModulePath]
                reload(oModule)
                # main() is the function to launch all ec tools
                oModule.main()
                
            sIconPath = '%s/%sOptions.jpg' %(scc.ICON_PATH,
                                             sName.capitalize())
            self.__sModule = 'everyoneCan.'
            self.__sModule += sName
            self.__sFile = '%sOptions' %sName
            sToolTip = '%s, Everyone Can %s' %(sName,sName)
            cw.AlIconPushButton.__init__(self,
                                         sIconPath,
                                         sToolTip)
            QtCore.QObject.connect(self, 
                                   QtCore.SIGNAL('clicked()'),
                                   __pushButton_onClicked)

# Ni !