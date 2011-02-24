# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
#from everyoneCan import TabMerger   #function class to set the methods  
#                                        #to merge the application in a Qwidget    
from everyoneCan.light import LightOptionsUI
from everyoneCan.light import LightOptionsCtrl
from everyoneCan.light import LightOptionsModel
reload(LightOptionsUI)
reload(LightOptionsCtrl)
reload(LightOptionsModel)


class LightingOptionsLauncher(QtGui.QMainWindow):
    """
    Launcher of the ReferenceApplication
    Can be launched as a standAlone 
    or from ec_Launcher (launcher of EveryoneCan GUI)
    """
    def __init__(self, boolSelfLaunch=1):
        self.WINDOWS_NAME   = 'Light, Everyone Can Light'
        self.oGui           = LightOptionsUI.Gui(boolSelfLaunch)
        self.oModel         = LightOptionsModel.Model()
        self.oCtrl          = LightOptionsCtrl.Control(self.oGui, 
                                                      self.oModel)
        if boolSelfLaunch == 0 :
            QtGui.QMainWindow.__init__(self)
            oCentralWidget              = QtGui.QWidget()
            oMainLayout                 = QtGui.QVBoxLayout(oCentralWidget)
            oMainLayout.setContentsMargins(0,0,0,0)
            oMainLayout.addWidget(self.oGui)
            self.setCentralWidget(oCentralWidget)        

def main(debug=0, boolSelfLaunch=1):
    """
    The main function when using qt inside maya using PumbThread
    HowTo :
    from everyoneCan.link import linkOptions
    reload(linkOptions)
    linkOptions.main()
    """
    import pumpThread
    global launcherLightingOptions, app
    #check to see if the dialog is already loaded
#    if debug == 1:
#        if 'launcherLinkOptions' in globals():
#            del launcherLinkOptions
    if 'launcherLightingOptions' in globals():
        try:
            launcherLightingOptions.oGui.setWindowFlags(
                                        QtCore.Qt.WindowStaysOnTopHint)
            launcherLightingOptions.oGui.setWindowFlags(
                                        QtCore.Qt.WindowCancelButtonHint)
            launcherLightingOptions.oGui.setWindowState(
                                        QtCore.Qt.WindowActive)
            launcherLightingOptions.oGui.show()
            return
        except:
            del launcherLightingOptions
    pumpThread.initializePumpThread()

    app = QtGui.qApp
    app.setStyle(QtGui.QStyleFactory.create('cleanlooks'))
    app.setFont(QtGui.QFont('Bitstream Vera Sans', 8))

    launcherLightingOptions = LightingOptionsLauncher(boolSelfLaunch) #MAIN FUNCTION HERE
    launcherLightingOptions.oGui.resize(1,1)
    launcherLightingOptions.oGui.setWindowTitle(
                                    launcherLightingOptions.WINDOWS_NAME)
    launcherLightingOptions.oGui.show()
    app.connect(app, QtCore.SIGNAL('lastWindowClosed()'),
                app, QtCore.SLOT('quit()'))
        
# Ni!