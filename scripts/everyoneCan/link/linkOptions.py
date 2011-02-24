# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
#should be useless now
#from everyoneCan import TabMerger   #function class to set the methods  
#                                    #to merge the application in a Qwidget    
from everyoneCan.link import LinkOptionsUI
from everyoneCan.link import LinkOptionsCtrl
from everyoneCan.link import LinkOptionsModel
reload(LinkOptionsUI)
reload(LinkOptionsCtrl)
reload(LinkOptionsModel)
    
class LinkOptionsLauncher:
    """
    Launcher of the linkApplication
    """
    def __init__(self, boolSelfLaunch=1):
        """
        @type boolSelfLaunch: boolean
        @param boolSelfLaunch: application launched as standalone (1) or not (0)
        """
        
        self.WINDOWS_NAME   = 'link, Everyone Can link'
        self.oGui           = LinkOptionsUI.Gui(boolSelfLaunch)
        oModel              = LinkOptionsModel.Model(self.oGui)
        oCtrl               = LinkOptionsCtrl.Control(self.oGui,oModel)

        if boolSelfLaunch == 0 :
            QtGui.QMainWindow.__init__(self)
            oCentralWidget              = QtGui.QWidget()
            oMainLayout                 = QtGui.QVBoxLayout(oCentralWidget)
            oMainLayout.setContentsMargins(0,0,0,0)
            oMainLayout.addWidget(self.oGui)
            self.setCentralWidget(oCentralWidget)
        
def main(debug=1):
    """
    The main function when using qt inside maya using PumbThread
    HowTo :
    from everyoneCan.link import linkOptions
    reload(linkOptions)
    linkOptions.main()
    """
    import pumpThread
    global launcherLinkOptions, app
    #check to see if the dialog is already loaded
    if debug == 1:
        if 'launcherLinkOptions' in globals():
            del launcherLinkOptions
    if 'launcherLinkOptions' in globals():
        try:
            launcherLinkOptions.oGui.setWindowFlags(
                                            QtCore.Qt.WindowStaysOnTopHint)
            launcherLinkOptions.oGui.setWindowFlags(
                                            QtCore.Qt.WindowCancelButtonHint)
            launcherLinkOptions.oGui.setWindowState(
                                                QtCore.Qt.WindowActive)
            launcherLinkOptions.oGui.show()
            return
        except:
            del launcherLinkOptions
    pumpThread.initializePumpThread()

    app = QtGui.qApp
    app.setStyle(QtGui.QStyleFactory.create('cleanlooks'))
    app.setFont(QtGui.QFont('Bitstream Vera Sans', 8))

    launcherLinkOptions = LinkOptionsLauncher() #MAIN FUNCTION HERE
    
    
    launcherLinkOptions.oGui.setWindowTitle(
                                    launcherLinkOptions.WINDOWS_NAME)
    launcherLinkOptions.oGui.show()
    app.connect(app, QtCore.SIGNAL('lastWindowClosed()'),
                app, QtCore.SLOT('quit()'))
        
# Ni!