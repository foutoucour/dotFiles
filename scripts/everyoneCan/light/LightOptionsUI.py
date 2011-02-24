# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

from everyoneCan import CustomWidgets as cw
reload(cw)
from everyoneCan import UIs
reload(UIs)
from everyoneCan import Paths
reload(Paths)

class Gui(QtGui.QMainWindow, QtGui.QWidget, Paths.Paths):
    """
    Graphic Interface of lightOptions tool
    Discuss with control through an observer
    """
    def __init__(self, boolSelfLaunch):
        """
        @type boolSelfLaunch: int boolean
        @param boolSelfLaunch: indicate if the tool is launched as 
                stand-alone (1) or not (0)
        """        
        QtGui.QMainWindow.__init__(self)
        oCentralWidget              = QtGui.QWidget()
        oMainLayout                 = QtGui.QVBoxLayout(oCentralWidget)
        self.__setContentMargins0(oMainLayout)
        oMainLayout.addLayout(self.__addRef())
        oMainLayout.addLayout(self.__manageRef())
        oMainLayout.addLayout(self.__instance())
        if boolSelfLaunch == 1:
            oMainLayout.addWidget(self.__UIs())  
        oMainLayout.addStretch(1)
        
        self.setCentralWidget(oCentralWidget)
    
    def getMainLayout(self):
        return self.__oMainLayout
    
    def __addRef(self):
        """
        Group of widget to create references (lights, cameraShadow, blocker)
        @type oMasterLayout: Qt object
        @param oMasterLayout: Qt Layout 
        """
        oAddRefGlobalLayout = QtGui.QHBoxLayout()
        self.__setContentMargins0(oAddRefGlobalLayout)
        # Grouping
        oAddRefGrpBox = QtGui.QGroupBox(self.ADD_REF_GROUPBOX_NAME)
        oAddRefGrpBox.setCheckable(0)
        oAddRefLayout = QtGui.QVBoxLayout(oAddRefGrpBox)
        self.__setContentMargins0(oAddRefLayout)
        # Widget Creation methods
        oAddRefLayout.addLayout(self.__lightButtons())
        self.__othersButtons(oAddRefLayout)
        # Grouping
        oAddRefGlobalLayout.addWidget(oAddRefGrpBox)
        return oAddRefGlobalLayout
    
    def __manageRef(self):
        """
        Methods creating the Manage References bloc
        @type oMasterLayout: Qt object
        @param oMasterLayout: Qt Layout
        """
        def __removeButton_onClicked():
            self.emit(QtCore.SIGNAL('removeRef'))
            
        def __renameAction_onClicked():
            self.emit(QtCore.SIGNAL('renameRef'))

        def __snapAction_onClicked():
            self.emit(QtCore.SIGNAL('snapRef'))
                
        oManageRefButtonGlobalLayout = QtGui.QVBoxLayout()
        oManageRefGrpBox = QtGui.QGroupBox(self.MANAGE_REF_GROUPBOX_NAME)
        oManageRefGrpBox.setCheckable(0)
        oManageRefButtonLayouts = QtGui.QVBoxLayout(oManageRefGrpBox)
        self.__setContentMargins0(oManageRefButtonLayouts)
        
        oRenameButton = cw.AlIconPushButton(self.RENAME_ICON,
                                            self.RENAME_BUTTON_NAME)
        oRenameButton.setParent(oManageRefGrpBox)
        self.connect(oRenameButton, 
                     QtCore.SIGNAL('clicked()'),
                     __renameAction_onClicked)
        self.connect(oRenameButton, 
                         QtCore.SIGNAL('AlIconPushButton_clicked'),
                         self.__emit)
        
        oRemoveAction = QtGui.QAction(QtGui.QIcon(self.REMOVE_ICON),
                                      self.REMOVE_BUTTON_NAME,
                                      oRenameButton)
        self.connect(oRemoveAction,
                     QtCore.SIGNAL('triggered()'),
                     __removeButton_onClicked)
        self.connect(oRemoveAction, 
                     QtCore.SIGNAL('triggered()'),
                     self.__emit)
        
        oSnapAction = QtGui.QAction(QtGui.QIcon(self.SNAP_MASTER_ICON),
                                    'Snap', oRenameButton)
        self.connect(oSnapAction, QtCore.SIGNAL('triggered()'),
                     __snapAction_onClicked)
        self.connect(oSnapAction, 
                     QtCore.SIGNAL('triggered()'),
                     self.__emit)
        
        oRenameButton.addAction(oRemoveAction)
        oRenameButton.addAction(oSnapAction)
        oManageRefButtonLayouts.addWidget(oRenameButton)
        oManageRefButtonGlobalLayout.addWidget(oManageRefGrpBox)
        oManageRefButtonGlobalLayout.addStretch(1)
        return oManageRefButtonGlobalLayout
    
    def __instance(self):
        """
        Methods creating the Manage instances bloc
        @type oMasterLayout: Qt object
        @param oMasterLayout: Qt Layout
        """       
        def __instButton_onClicked():
            self.emit(QtCore.SIGNAL('instanceRef'))
            
        def __duplAction_onClicked():
            self.emit(QtCore.SIGNAL('duplicateRef'))
            
        def __unlinkAction_onClicked():
            self.emit(QtCore.SIGNAL('unlinkInstance'))
        
        def __findMasterAction_onClicked():
            self.emit(QtCore.SIGNAL('findMaster'))
            
        def __findInstanceAction_onClicked():
            self.emit(QtCore.SIGNAL('findInstance'))
            
        oInstanceRefButtonGlobalLayout = QtGui.QVBoxLayout()
        oInstanceRefGrpBox = QtGui.QGroupBox(
                                        self.INSTANCE_REF_GROUPBOX_NAME)
        oInstanceRefGrpBox.setCheckable(0)
        oInstanceRefButtonLayouts = QtGui.QVBoxLayout(oInstanceRefGrpBox)
        self.__setContentMargins0(oInstanceRefButtonLayouts)
        
        
        oDuplButton = cw.AlIconPushButton(self.DUPLICATE_ICON,
                                        self.DUPLICATE_BUTTON_NAME)
        oDuplButton.setParent(oInstanceRefGrpBox)
        self.connect(oDuplButton, QtCore.SIGNAL('clicked()'),
                     __duplAction_onClicked)
        self.connect(oDuplButton, 
                     QtCore.SIGNAL('AlIconPushButton_clicked'),
                     self.__emit)
        
        oInstAction = QtGui.QAction(QtGui.QIcon(self.INSTANCE_ICON),
                                    self.INSTANCE_BUTTON_NAME,
                                    oDuplButton)
        self.connect(oInstAction,
                     QtCore.SIGNAL('triggered()'),
                     __instButton_onClicked)
        self.connect(oInstAction, 
                     QtCore.SIGNAL('triggered()'),
                     self.__emit)

        oUnlinkAction = QtGui.QAction(QtGui.QIcon(self.UNLINK_ICON),
                                      'Unlink', 
                                      oDuplButton)
        self.connect(oUnlinkAction, QtCore.SIGNAL('triggered()'),
                     __unlinkAction_onClicked)
        self.connect(oUnlinkAction, 
                     QtCore.SIGNAL('triggered()'),
                     self.__emit)
        
        oFindMasterAction = QtGui.QAction(QtGui.QIcon(self.FIND_MASTER_ICON),
                                       'Find Master', oDuplButton)
        self.connect(oFindMasterAction, QtCore.SIGNAL('triggered()'),
                     __findMasterAction_onClicked)
        self.connect(oFindMasterAction, 
                     QtCore.SIGNAL('triggered()'),
                     self.__emit)
        
        oFindInstanceAction = QtGui.QAction(
                                        QtGui.QIcon(self.FIND_INSTANCE_ICON),
                                       'Find Instances', oDuplButton)
        self.connect(oFindInstanceAction, QtCore.SIGNAL('triggered()'),
                     __findInstanceAction_onClicked)
        self.connect(oFindInstanceAction, 
                     QtCore.SIGNAL('triggered()'),
                     self.__emit)
        
        
        oDuplButton.addAction(oInstAction)
        oDuplButton.addAction(oUnlinkAction)
        oDuplButton.addAction(oFindMasterAction)
        oDuplButton.addAction(oFindInstanceAction)

        oInstanceRefButtonLayouts.addWidget(oDuplButton)
        oInstanceRefButtonGlobalLayout.addWidget(oInstanceRefGrpBox)
        oInstanceRefButtonGlobalLayout.addStretch(1)
        return oInstanceRefButtonGlobalLayout
            
    def __UIs(self):
        """
        Methods creating the UI bloc
        @type oMasterLayout: Qt object
        @param oMasterLayout: Qt Layout
        """             
        oUIGrpBox = QtGui.QGroupBox(self.UI_GROUPBOX_NAME)
        oUILayout = QtGui.QVBoxLayout(oUIGrpBox)
        self.__setContentMargins0(oUILayout)
        oUILayout.addWidget(UIs.AllOthersUIWidget(__name__,'V'))
        return oUIGrpBox
        
    def __lightButtons(self):
        """
        Group of pushButton to create light references
        @type oMasterLayout: Qt object
        @param oMasterLayout: Qt Layout
        """
        def __pointLight():
            def __pointLightButton_onClicked():
                self.emit(QtCore.SIGNAL('pointlight'))
            
            oPointLightButton = cw.AlIconPushButton(self.POINTLIGHT_ICON,
                                            self.POINTLIGHT_BUTTON_NAME)
            self.connect(oPointLightButton, QtCore.SIGNAL('clicked()'),
                     __pointLightButton_onClicked)
            self.connect(oPointLightButton, 
                         QtCore.SIGNAL('AlIconPushButton_clicked'),
                         self.__emit)
            return oPointLightButton
        
        def __spotLight():
            def __spotLightButton_onClicked():
                self.emit(QtCore.SIGNAL('spotLight'))
                
            oSpotLightButton = cw.AlIconPushButton(self.SPOTLIGHT_ICON,
                                            self.SPOTLIGHT_BUTTON_NAME)
            self.connect(oSpotLightButton, QtCore.SIGNAL('clicked()'),
                     __spotLightButton_onClicked)
            self.connect(oSpotLightButton, 
                         QtCore.SIGNAL('AlIconPushButton_clicked'),
                         self.__emit)
            return oSpotLightButton
        
        def __ambientLight():
            def __ambientLightButton_onClicked():
                self.emit(QtCore.SIGNAL('ambientLight'))
        
            oAmbientLightButton = cw.AlIconPushButton(self.AMBIENTLIGHT_ICON,
                                            self.AMBIENTLIGHT_BUTTON_NAME)
            self.connect(oAmbientLightButton, QtCore.SIGNAL('clicked()'),
                     __ambientLightButton_onClicked)
            self.connect(oAmbientLightButton, 
                         QtCore.SIGNAL('AlIconPushButton_clicked'),
                         self.__emit)
            return oAmbientLightButton
        
        def __reflectionLight():
            def __reflectionLightButton_onClicked():
                self.emit(QtCore.SIGNAL('reflectionlight'))
            
            oReflectionLightButton = cw.AlIconPushButton(self.REFLECTIONLIGHT_ICON,
                                        self.REFLECTIONLIGHT_BUTTON_NAME)
            self.connect(oReflectionLightButton, QtCore.SIGNAL('clicked()'),
                     __reflectionLightButton_onClicked)
            self.connect(oReflectionLightButton, 
                         QtCore.SIGNAL('AlIconPushButton_clicked'),
                         self.__emit)
            return oReflectionLightButton
            
        def __occlusionLight():
            def __occluLightButton_onClicked():
                self.emit(QtCore.SIGNAL('occlusionLight'))
            
            oOccluLightButton = cw.AlIconPushButton(self.OCCLUSIONLIGHT_ICON,
                                        self.OCCLUSIONLIGHT_BUTTON_NAME)
            self.connect(oOccluLightButton, QtCore.SIGNAL('clicked()'),
                     __occluLightButton_onClicked)
            self.connect(oOccluLightButton, 
                         QtCore.SIGNAL('AlIconPushButton_clicked'),
                         self.__emit)
            return oOccluLightButton
        
        def __bakeLight():
            def __bakeLightButton_onClicked():
                self.emit(QtCore.SIGNAL('bakeLight'))
            
            oBakeLightButton = cw.AlIconPushButton(self.BAKELIGHT_ICON,
                                        self.BAKELIGHT_BUTTON_NAME)
            self.connect(oBakeLightButton, QtCore.SIGNAL('clicked()'),
                     __bakeLightButton_onClicked)
            self.connect(oBakeLightButton, 
                         QtCore.SIGNAL('AlIconPushButton_clicked'),
                         self.__emit)
            return oBakeLightButton
        
        def __magicLight():
            def __magicLightButton():
                self.emit(QtCore.SIGNAL('magicLight'))
            
            def __magicLightAddAttr():
                self.emit(QtCore.SIGNAL('magicLightAddAttr'))
            
            def __magicLightRemoveAttr():
                self.emit(QtCore.SIGNAL('magicLightRemoveAttr'))
                
            oMagicLightButton = cw.AlIconPushButton(self.MAGICLIGHT_ICON,
                                        self.MAGICLIGHT_BUTTON_NAME)
            self.connect(oMagicLightButton, QtCore.SIGNAL('clicked()'),
                     __magicLightButton)
            self.connect(oMagicLightButton, 
                         QtCore.SIGNAL('AlIconPushButton_clicked'),
                         self.__emit)
            
            oMagicLightAddAttr = QtGui.QAction(
                            QtGui.QIcon(self.MAGIC_ADD_ATTR_ICON),
                            self.MAGIC_ADD_ATTR_NAME, 
                            oMagicLightButton)
            self.connect(oMagicLightAddAttr, QtCore.SIGNAL('triggered()'),
                         __magicLightAddAttr)
            self.connect(oMagicLightAddAttr, 
                         QtCore.SIGNAL('triggered()'),
                         self.__emit)
            
            oMagicLightRemoveAttr = QtGui.QAction(
                            QtGui.QIcon(self.MAGIC_REMOVE_ATTR_ICON),
                            self.MAGIC_REMOVE_ATTR_NAME, 
                            oMagicLightButton)
            self.connect(oMagicLightRemoveAttr, QtCore.SIGNAL('triggered()'),
                         __magicLightRemoveAttr)
            self.connect(oMagicLightRemoveAttr, 
                         QtCore.SIGNAL('triggered()'),
                         self.__emit)
            
            oMagicLightButton.addAction(oMagicLightAddAttr)
            oMagicLightButton.addAction(oMagicLightRemoveAttr)
        
            return oMagicLightButton
        
        oLightGlobalLayout = QtGui.QVBoxLayout()
        oLightGlobalLayout.addWidget(__spotLight())
        oLightGlobalLayout.addWidget(__pointLight())
        oLightGlobalLayout.addWidget(__ambientLight())
        oLightGlobalLayout.addWidget(__reflectionLight())
        oLightGlobalLayout.addWidget(__occlusionLight())
        oLightGlobalLayout.addWidget(__bakeLight())
        oLightGlobalLayout.addWidget(__magicLight())
        return oLightGlobalLayout
    
    def __othersButtons(self, oMasterLayout):
        """
        Method creating create reference button other than light
        @type oMasterLayout: Qt object
        @param oMasterLayout: Qt Layout
        """
        def __blocker():
            def __blockerButton_onClicked():
                self.emit(QtCore.SIGNAL('blocker'))
                
            def __linkBlockerAction_onClicked():
                self.emit(QtCore.SIGNAL('block'))
            
            def __unlinkBlockerAction_onClicked():
                self.emit(QtCore.SIGNAL('unblock'))
                
            oBlockerButton = cw.AlIconPushButton(self.BLOCKER_ICON,
                                            self.BLOCKER_BUTTON_NAME)
            self.connect(oBlockerButton, QtCore.SIGNAL('clicked()'),
                     __blockerButton_onClicked)
            self.connect(oBlockerButton, 
                         QtCore.SIGNAL('AlIconPushButton_clicked'),
                         self.__emit)
            
            oAddLink = QtGui.QAction(
                            QtGui.QIcon(self.LINK_BLOCKER_AND_LIGHT_ICON),
                                        self.BLOCK_BUTTON_NAME, 
                                        oBlockerButton)
            self.connect(oAddLink, QtCore.SIGNAL('triggered()'),
                         __linkBlockerAction_onClicked)
            self.connect(oAddLink, 
                         QtCore.SIGNAL('triggered()'),
                         self.__emit)
            
            oRemoveLink = QtGui.QAction(
                            QtGui.QIcon(self.UNLINK_BLOCKER_AND_LIGHT_ICON),
                                        self.UNBLOCK_BUTTON_NAME, 
                                        oBlockerButton)
            self.connect(oRemoveLink, QtCore.SIGNAL('triggered()'),
                         __unlinkBlockerAction_onClicked)
            self.connect(oRemoveLink, 
                         QtCore.SIGNAL('triggered()'),
                         self.__emit)
            
            oBlockerButton.addAction(oAddLink)
            oBlockerButton.addAction(oRemoveLink)
            
            return oBlockerButton
        
        def __shdCam():
            def __shdCamButton_onClicked():
                self.emit(QtCore.SIGNAL('shadowCamera'))
                
            oShdCamButton = cw.AlIconPushButton(self.SHADOW_CAMERA_ICON,
                                                self.SHADOW_CAMERA_BUTTON_NAME)
            oShdCamButton.setDisabled(1)
            self.connect(oShdCamButton, QtCore.SIGNAL('clicked()'),
                     __shdCamButton_onClicked)
            self.connect(oShdCamButton, 
                         QtCore.SIGNAL('AlIconPushButton_clicked'),
                         self.__emit)
            return oShdCamButton
        
        oOthersButtonsLayout = QtGui.QVBoxLayout()
        oOthersButtonsLayout.addWidget(__blocker())
        oOthersButtonsLayout.addWidget(__shdCam())
        oMasterLayout.addLayout(oOthersButtonsLayout)
        
    def __setContentMargins0(self, oWidget):
        """
        Method to set the contentMargin to 0
        @type oWidget: object
        @param oWidget: Qt Widget
        @rtype: object
        @return: Qt Widget with contentMargins set to (0,0,0,0)
        """
        oWidget.setContentsMargins(0,0,0,0)
        return oWidget
    
    def __emit(self):
        self.emit(QtCore.SIGNAL('LightOptionsUI_signal'), self)
# Ni!