# -*- coding: utf-8 -*-

## @todo : search ## todo to find methods to finish

import os
import glob

import maya.cmds as cmds
import maya.mel as mel

from PyQt4 import QtGui
from PyQt4 import QtCore

# Class to storing different values of alType attribut
# also paths to icons or text of tooltips etc.
from everyoneCan import SharedConstants
reload(SharedConstants)
scc                         = SharedConstants.Constants()


class AssignerLauncher(QtGui.QMainWindow):
    WINDOWS_NAME                = 'Assign, Everyone Can Assign'
    
    # Using os.getenv methods give the choise to the user to use local
    # or production versions.
    __sShaderPath               = os.getenv('PROJECT_SOURCE_PATH')
    __sShaderPath               += '/shaders/sdl/'
    __SURFACE__PREFIX           = 'srf_al_'
    __DISPL__PREFIX             = 'dsp_al_'
    __EXTENTION                 = '.sdl'
    
    # Titles of buttons.
    __SURFACE_BUTTON            = 'Assign Surface Shader'
    __DISPLACEMENT_BUTTON       = 'Add Displacement Shader'
    
    __MINI_SIZE                 = 158
    __DEFAULT_SURFACE_SHADER    = 'general'
    
    def __init__(self):
        """
        Creation of widgets
        """
        self.__SURFACE_COLOR             = scc.GREEN_COLOR
        self.__DISPL_COLOR               = scc.YELLOW_COLOR
        
        QtGui.QMainWindow.__init__(self)
        self.__oCentralWidget       = QtGui.QWidget()
        self.__oMainLayout          = QtGui.QVBoxLayout(self.__oCentralWidget)
        self.__oMainLayout.setContentsMargins(0,0,0,0)
        
        self.__dictSurfaceShaders   = self.__getListShaders(self.__SURFACE__PREFIX)
        self.__dictDisplShaders     = self.__getListShaders(self.__DISPL__PREFIX)
        
        #======================================================================
        # Surface
        #======================================================================
        # Version combobox is fed when the index of the title combobox change
        self.__oSurfaceVersionBox = QtGui.QComboBox()
        
        self.__oSurfaceTitleBox = QtGui.QComboBox()
        self.__oSurfaceTitleBox.setMinimumWidth(self.__MINI_SIZE)
        
        self.connect(self.__oSurfaceTitleBox, 
                    QtCore.SIGNAL('currentIndexChanged(int)'),
                    self.__feedSurfaceVersionBox)
        
        self.__oSurfaceTitleBox.addItems(sorted(
                                        self.__dictSurfaceShaders.iterkeys()))
        
        # set the default value of the combobox
        oString = QtCore.QString(self.__DEFAULT_SURFACE_SHADER)
        iIndex = self.__oSurfaceTitleBox.findText(QtCore.QString(oString),
                                        QtCore.Qt.MatchExactly)
        self.__oSurfaceTitleBox.setCurrentIndex(iIndex)
        
        self.__oAssignSurfaceButton = QtGui.QPushButton(self.__SURFACE_BUTTON)
        self.__oAssignSurfaceButton.setMinimumWidth(self.__MINI_SIZE)
        sColor ="QWidget { background-color: %s }" %self.__SURFACE_COLOR.name()
        self.__oAssignSurfaceButton.setStyleSheet(sColor)
        
        self.connect(self.__oAssignSurfaceButton, 
                         QtCore.SIGNAL('clicked()'),
                         self.__assignSurfaceButton)
        
        oSurfaceLayout = QtGui.QHBoxLayout()
        oSurfaceLayout.addWidget(self.__oSurfaceTitleBox)
        oSurfaceLayout.addWidget(self.__oSurfaceVersionBox)
        oSurfaceLayout.addWidget(self.__oAssignSurfaceButton)
        
        #======================================================================
        # Displace
        #======================================================================
        def __assignDisplButton():
            self.emit(QtCore.SIGNAL('assignDisplButton'))
            
         # Version combobox is fed when the index of the title combobox change   
        self.__oDisplVersionBox = QtGui.QComboBox()
        
        self.__oDisplTitleBox = QtGui.QComboBox()
        self.__oDisplTitleBox.setMinimumWidth(self.__MINI_SIZE)
        
        self.connect(self.__oDisplTitleBox, 
                         QtCore.SIGNAL('currentIndexChanged(int)'),
                         self.__feedDisplVersionBox)
        
        self.__oDisplTitleBox.addItems(sorted(
                                        self.__dictDisplShaders.iterkeys()))
        
        self.__oAssignDisplButton = QtGui.QPushButton(self.__DISPLACEMENT_BUTTON)
        self.__oAssignDisplButton.setMinimumWidth(self.__MINI_SIZE)
        sColor ="QWidget { background-color: %s }" %self.__DISPL_COLOR.name()
        self.__oAssignDisplButton.setStyleSheet(sColor)
        
        self.connect(self.__oAssignDisplButton, 
                         QtCore.SIGNAL('clicked()'),
                         self.__assignDisplButton)
        
        oDisplLayout = QtGui.QHBoxLayout()
        oDisplLayout.addWidget(self.__oDisplTitleBox)
        oDisplLayout.addWidget(self.__oDisplVersionBox)
        oDisplLayout.addWidget(self.__oAssignDisplButton)
        
        self.__oMainLayout.addLayout(oSurfaceLayout)
        self.__oMainLayout.addLayout(oDisplLayout)
        
        self.setCentralWidget(self.__oCentralWidget)
    
                    
    def __feedSurfaceVersionBox(self):
        """
        Feeding of version combobox depending on the index of the title combo box
        """
        # Versions are stored in __dictDisplShaders dictionnary at the init
        # of the object.
        
        self.__oSurfaceVersionBox.setEnabled(1)
        self.__oSurfaceVersionBox.clear()
        
        title =  str(self.__oSurfaceTitleBox.currentText())
        
        self.__oSurfaceVersionBox.addItems(self.__dictSurfaceShaders[title])
        
        if len(self.__dictSurfaceShaders[title]) == 1:
            self.__oSurfaceVersionBox.setEnabled(0)
            
        # Set the combobox to the last version
        self.__oSurfaceVersionBox.setCurrentIndex(
                                    len(self.__dictSurfaceShaders[title])-1)
        
    def __feedDisplVersionBox(self):
        """
        Feeding of version combobox depending on the index of the title combo box
        """
        
        # Versions are stored in __dictDisplShaders dictionnary at the init
        # of the object.
        self.__oDisplVersionBox.setEnabled(1)
        self.__oDisplVersionBox.clear()
        
        title =  str(self.__oDisplTitleBox.currentText())
        
        self.__oDisplVersionBox.addItems(self.__dictDisplShaders[title])
        
        if len(self.__dictDisplShaders[title]) == 1:
            self.__oDisplVersionBox.setEnabled(0)
            
        # Set the combobox to the last version
        self.__oDisplVersionBox.setCurrentIndex(
                                    len(self.__dictDisplShaders[title])-1)
    
    #==========================================================================
    # control
    #==========================================================================
    def __getListShaders(self, sPrefix):
        """
        Check a folder and list every shader and its versions
        
        @type sPrefix   : string
        @param sPrefix  : type of shader
        
        @rtype      : dictionnary
        @return     : key : shader name, value : versions
        """
        
        dictShaders = {}
        
        sShaderFullPath = self.__sShaderPath
        sShaderFullPath += sPrefix
        
        # getting all shaders of the wanted type
        for sFile in glob.glob(sShaderFullPath+'*'+self.__EXTENTION):
            # name of the shader in the title combobox
            sTitle = sFile.replace(sShaderFullPath, '')
            sTitle = sTitle.split('_')[0]
            
            if not sTitle in dictShaders.keys():
                dictShaders[sTitle] = []
                
            sBasename = os.path.basename(sFile)
            version = sBasename.split('.')[0]
            version = version[-3:]
            dictShaders[sTitle].append(version)
            
        return dictShaders
    
    def __buildShaderPath(self, sTitle, iVersion, sPrefix):
        """
        Rebuild the path of the shader
        
        @type sTitle    : string
        @param sTitle   : name of the shader
        
        @type iVersion  : integer
        @param iVersion : version of the shader
        
        @type sPrefix   : string
        @param sPrefix  : prefix of the shader in paths
        
        @rtype      : string
        @return     : path of the shader
        """
        ## todo
        # The path should be stored in the __dictDisplShaders dictionnary
        
        sPath = self.__sShaderPath
        sPath += sPrefix
        sPath += sTitle
        sPath += '_v'
        sPath += iVersion
        sPath += self.__EXTENTION
        
        return sPath
    
    def __assignSurfaceButton(self):
        """
        Assign a new surface shader.
        Answer to clicked() on push button liked to assign 
        of surface shader.
        """
        sShaderPath = self.__buildShaderPath(self.__oSurfaceTitleBox.currentText(),
                                             self.__oSurfaceVersionBox.currentText(),
                                             self.__SURFACE__PREFIX)
        
        self.__assignShader(sShaderPath)
    
    def __assignDisplButton(self):
        """
        Add a new displacement shader to shading group.
        Answer to clicked() on push button liked to add 
        of displacement shader.
        """
        # Adding a displacement shader to a shading group can affect more than
        # the selecton.
        def message(sList, sPath):
            reply = QtGui.QMessageBox.question(self, 
                                               'Message',
                                               sList, 
                                               QtGui.QMessageBox.Yes, 
                                               QtGui.QMessageBox.Cancel)
    
            if reply == QtGui.QMessageBox.Yes:
                self.__assignDisplShader(sPath)
            else:
                pass
                
        listLinked                  = []
        self.__listSG               = []
        boolMessage                  = 0
        
        sShaderPath = self.__buildShaderPath(
                                        self.__oDisplTitleBox.currentText(),
                                        self.__oDisplVersionBox.currentText(),
                                        self.__DISPL__PREFIX)
        
        listSel = cmds.ls(sl=1)
        
        for sSel in listSel:
            sShapes = cmds.listRelatives(sSel)[0]
            
            for sConn in cmds.listConnections(sShapes):
                
                if cmds.nodeType(sConn) == 'shadingEngine':
                    
                    if not sConn in self.__listSG:
                        self.__listSG.append(sConn)
        
        
        for sSG in self.__listSG:
            
            for sConnShadingGroup in cmds.listConnections(sSG, d=0):
                
                if not cmds.nodeType(sConnShadingGroup) == 'liquidSurface':
                    
                    if not sConnShadingGroup in listLinked:
                        listLinked.append(sConnShadingGroup)
        
        
        # string listing all geometry affected by the new shader        
        sList = ''
        listLinked.sort()
        
        for element in listLinked:
            
            if not element in listSel:
                boolMessage = 1
                
                if not sList == '':
                    sList += '\n'
                sList += element
                
                
        sList += '\nwill be affected also'
        sList += '\n'
        sList += '\n'
        sList += 'Continue ?'
                
        if boolMessage == 1:        
            message(sList, sShaderPath)
        
    def __assignDisplShader(self, sPath):
        """
        Assign a displacement shder
        
        @type sPath     : string
        @param sPath    : path of the shader to assign
        """
        
        sShader = cmds.shadingNode('liquidDisplacement', asShader=1)
        cmds.setAttr('%s.rmanShaderLong' %sShader, 
                         sPath, 
                         type="string")
        
        for sSG in self.__listSG:
            cmds.connectAttr('%s.outColor' %sShader,
                             '%s.displacementShader' %sSG,
                             f=1)
        
        self.__openAttributEditor()
    
        
    def __assignShader(self, sPath):
        """
        Assign a surface shader.
        
        @type sPath     : string
        @param sPath    : path of the shader to assign
        """
        
        listSel = cmds.ls(sl=1)
        
        if len(listSel) > 0:
            sShader = cmds.shadingNode('liquidSurface', asShader=1)
            cmds.setAttr('%s.rmanShaderLong' %sShader, 
                         sPath, 
                         type="string")
            cmds.select(listSel, r=1)
            
            # Liquid function to assign the shader
            mel.eval('liquidAssignShaderToSelected %s;' %sShader)
            
            self.__openAttributEditor()

    def __openAttributEditor(self):
        mel.eval('ShowAttributeEditorOrChannelBox;')
        
def main(debug=0):
    """
    The main function when using qt inside maya using PumbThread
    HowTo :
    from everyoneCan.assign import assignOptions
    reload(lazy)
    assignOptions.main()
    
    @type debug     : boolean
    @param debug    : del the application each time (1) or not (0)
    """
    import pumpThread
    global launcherLazy, app
    #check to see if the dialog is already loaded
    if debug == 1:
        if 'launcherLazy' in globals():
            del launcherLazy
    if 'launcherLazy' in globals():
        try:
            launcherLazy.oGui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            launcherLazy.oGui.setWindowFlags(QtCore.Qt.WindowCancelButtonHint)
            launcherLazy.oGui.setWindowState(QtCore.Qt.WindowActive)
            launcherLazy.oGui.show()
            return
        except:
            del launcherLazy
    pumpThread.initializePumpThread()

    app = QtGui.qApp
    app.setStyle(QtGui.QStyleFactory.create('cleanlooks'))
    app.setFont(QtGui.QFont('Bitstream Vera Sans', 8))

    launcherLazy = AssignerLauncher() #MAIN FUNCTION HERE
        
    launcherLazy.setWindowTitle(launcherLazy.WINDOWS_NAME)
    launcherLazy.show()
    app.connect(app, QtCore.SIGNAL('lastWindowClosed()'),
                app, QtCore.SLOT('quit()'))
        
# Ni!