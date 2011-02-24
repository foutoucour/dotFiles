# -*- coding: utf-8 -*-
from PyQt4 import QtCore

class Control(QtCore.QObject):
    """control of the lightOptions Application"""
    #==========================================================================
    # constants
    #==========================================================================
    __SPOT              = 'spot'
    __POINT             = 'point'
    __AMBIENT           = 'ambient'
    __REFLECTION        = 'reflection'
    __OCCLUSION         = 'occlusion'
    __BAKE              = 'bake'
    __BLOCKER           = 'blocker'
    __SHADOW_CAMERA     = 'ShadowCamera'
    __MAGIC             = 'magicLight'
   
    def __init__(self, oGui, oModel):
        """
        Setting of the link with Gui and the model 
        @type oGui: object
        @param oGui: Interface part of this lightOptions Application
        """
        self.__oModel = oModel
        self.__oGui = oGui
        self.__signals()        
            
    def __pointLightButton(self):
        """Control of the pointLight""" 
        self.__oModel.createReference(self.__POINT)

    def __spotLightButton(self):
        """Control of the spotLight"""
        self.__oModel.createReference(self.__SPOT)

    def __ambientLightButton(self):
        """Control of the ambientLight"""
        self.__oModel.createReference(self.__AMBIENT)
       
    def __reflectionLightButton(self):
        """Control of the reflectionLight"""
        self.__oModel.createReference(self.__REFLECTION)
        
    def __occluLightButton(self):
        """Control of the occlusionLight"""
        self.__oModel.createReference(self.__OCCLUSION)
        
    def __bakeLightButton(self):
        """Control of the bakeLight"""
        self.__oModel.createReference(self.__BAKE)
               
    def __blockerButton(self):
        """Control of the blocker"""
        self.__oModel.createReference(self.__BLOCKER)

    def __linkBlockerButton(self):
        """Control of the blocker"""
        self.__oModel.linkBlocker()
        
    def __unlinkBlockerButton(self):
        """Control of the blocker"""
        self.__oModel.unlinkBlocker()
        
    def __shdCamButton(self):
        """Control of the shadowCamera"""
        self.__oModel.createReference(self.__SHADOW_CAMERA)
   
    def __renameButton(self):
        """Control of the rename"""
        self.__oModel.renameRef()
        
    def __removeButton(self):
        """Control of the remove"""
        self.__oModel.removeRef() 
        
    def __duplButton(self):
        """Control of the duplicate"""
        self.__oModel.duplicateRef()
        
    def __instButton(self):
        """Control of the instance"""
        self.__oModel.instance()
    
    def __unlinkInstanceButton(self):
        """Control of the unlink"""
        self.__oModel.unlink()
    
    def __snapButton(self):
        """Control of the unlink"""
        self.__oModel.snap()
    
    def __findMasterButton(self):
        """Control of the unlink"""
        self.__oModel.selectMaster()
    
    def __findInstanceButton(self):
        """Control of the unlink"""
        self.__oModel.selectInstance()
    
    def __magicLightButton(self):
        """Control of the magicLight"""
        self.__oModel.createReference(self.__MAGIC)
    
    def __magicLightAddAttrButton(self):
        """Control of the magicLightAddAttr"""
        self.__oModel.magicLightAddAttr()
    
    def __magicLightRemoveAttrButton(self):
        """Control of the magicLightRemoveAttr"""
        self.__oModel.magicLightRemoveAttr()
        
    def __signals(self):
        #======================================================================
        # Ligths
        #======================================================================
        self.connect(self.__oGui, QtCore.SIGNAL('pointlight'),
                     self.__pointLightButton)
        self.connect(self.__oGui, QtCore.SIGNAL('spotLight'),
                     self.__spotLightButton)
        self.connect(self.__oGui, QtCore.SIGNAL('ambientLight'),
                     self.__ambientLightButton)
        self.connect(self.__oGui, QtCore.SIGNAL('reflectionlight'),
                     self.__reflectionLightButton)
        self.connect(self.__oGui, QtCore.SIGNAL('occlusionLight'),
                     self.__occluLightButton)
        self.connect(self.__oGui, QtCore.SIGNAL('bakeLight'),
                     self.__bakeLightButton)
        self.connect(self.__oGui, QtCore.SIGNAL('magicLight'),
                     self.__magicLightButton)
        self.connect(self.__oGui, QtCore.SIGNAL('magicLightAddAttr'),
                     self.__magicLightAddAttrButton)
        self.connect(self.__oGui, QtCore.SIGNAL('magicLightRemoveAttr'),
                     self.__magicLightRemoveAttrButton)
        #======================================================================
        # Others
        #======================================================================
        self.connect(self.__oGui, QtCore.SIGNAL('blocker'),
                     self.__blockerButton)
        self.connect(self.__oGui, QtCore.SIGNAL('block'),
                     self.__linkBlockerButton)
        self.connect(self.__oGui, QtCore.SIGNAL('unblock'),
                     self.__unlinkBlockerButton)
        self.connect(self.__oGui, QtCore.SIGNAL('shadowCamera'),
                     self.__shdCamButton)
        #======================================================================
        # Misc
        #======================================================================
        self.connect(self.__oGui, QtCore.SIGNAL('removeRef'),
                     self.__removeButton)
        self.connect(self.__oGui, QtCore.SIGNAL('renameRef'),
                     self.__renameButton)
        self.connect(self.__oGui, QtCore.SIGNAL('snapRef'),
                     self.__snapButton)
        #======================================================================
        # Instance
        #======================================================================
        self.connect(self.__oGui, QtCore.SIGNAL('instanceRef'),
                     self.__instButton)
        self.connect(self.__oGui, QtCore.SIGNAL('duplicateRef'),
                     self.__duplButton)
        self.connect(self.__oGui, QtCore.SIGNAL('unlinkInstance'),
                     self.__unlinkInstanceButton)
        self.connect(self.__oGui, QtCore.SIGNAL('findMaster'),
                     self.__findMasterButton)
        self.connect(self.__oGui, QtCore.SIGNAL('findInstance'),
                     self.__findInstanceButton)
        
# Ni!