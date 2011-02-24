# -*- coding: utf-8 -*-
from PyQt4 import QtCore
import al_setLiquid
import maya.cmds as cmds
import maya.mel as mel
import al.fileio
import os

class Control(QtCore.QObject, al_setLiquid.setLiquid):
    """controlor of the GlobalOptions Application"""
    #==========================================================================
    # constants
    #==========================================================================
    __SET_NAME              = 'al_RenderSet'
    __RESOLUTION            = 1920
    __RESOLUTIONY           = 1080
    __FORMAT_LIST           = ['framebuffer', 'tiff', 'rib only']
    __MAYA_CAMERAS_LIST     = ['persp','front','top','side']
    
    __BUCKET_SIZE_LIST      = ['8','16','32','64']
    __GRID_SIZE_LIST        = ['64','256','1024','4096']
    __FARM_GROUP_LIST       = ['preview', 'final', 'final_night']
    __BIT_DEPTH_LIST        = ['8 bits','16 bits','32 bits']
    __INIT_NODE_NAME        = 'al_renderOptionsInit'
    #==========================================================================
    # variables
    #==========================================================================
    __sFrameValue = ''
    __sStepValue = ''
    name = __name__
    def __init__(self, oGui, oModel):
        """
        Setting of the link with Gui and the model
        GuiObserver is the handler of the Gui for the controlor 
        @type oGui: object
        @param oGui: Interface part of this GlobalOptions Application
        @type oModel: object
        @param oModel: Logic part of the GlobalOptions Application
        """
        self.__boolPrintMode    = 0
        self.__iHideUI          = 0
        self.__iHideOthers      = 0
        self.__oGui             = oGui
        self.__oModel           = oModel
        self.__oModel.setResolutionX(self.__RESOLUTION)
        self.__oModel.setResolutionY(self.__RESOLUTIONY)
        self.__RESO_LIST        = self.__oModel.makeListOfNumbers(10)
        self.__listCameras      = []
        self.__intiateValues()
        self.__oGui.main()
        self.__setValues()
        self.__signals()
    
    def __intiateValues(self):
        """
        Initiate values before the Gui is created.
        """
        self.__listCameras = self.__oModel.cameraListing()
        self.__oGui.setCameraList(self.__listCameras)
        self.__oGui.setFormatList(self.__FORMAT_LIST)
        self.__oGui.setResoList(self.__RESO_LIST)
        self.__oGui.setBucketSizeList(self.__BUCKET_SIZE_LIST)
        self.__oGui.setGridSizeList(self.__GRID_SIZE_LIST)
        self.__oGui.setFarmGroupList(self.__FARM_GROUP_LIST)
        self.__oGui.setBitDepthList(self.__BIT_DEPTH_LIST)

    def __setValues(self):
        """
        Method to set value of the GUI.
        The first time the GUI is created for a scene, 
        defauld values will be set and
        it will create a node named __INIT_NODE_NAME.
        So the second time the GUI is launched on a scene, 
        the controlor will grab values from liquid instead to set default
        values
        """
        if not cmds.objExists(self.__INIT_NODE_NAME):
            self.__setDefaultValues()
        else :
            self.__findValuesFromLiquid()
            
        if cmds.objExists('liqCropWindowViewer'):
            iValue = 2
        else :
            iValue = 0
        self.__oGui.setCropZoneState(iValue)
        iValue      = self.__oModel.clampedBool(iValue)
        iValue      = self.__oModel.invertedBool(iValue)
        self.__oGui.setCropZoneDisabled(iValue)
    
    def __setDefaultValues(self):
        self.l_set()
        self.__setCamera(self.__oModel.testForOnlyMayaCamera(
                                                    self.__listCameras))
        self.__setResolution(9)
        self.__setCurrentFrameState(2)
        self.__setFrameText('0')
        self.__setByFrameText('1')
        self.__setLazynessState(0)
        self.__setShadingRateText('1')
        self.__setPixelSampleText('2')
        self.__setBucketSize(2)
        self.__setGridSize(2)
#        self.__setCameraBlurState(0)
#        self.__setDOFState(0)
#        self.__setSampleMotionState(0)
        self.__setFormat(0)
        self.__setToFarmState(1)
        self.__setFarmGroup(0)
        self.__setRayState(0)
        self.__setSurfaceState(0)
        self.__setDisplacementState(0)
        self.__setSubSurfaceState(0)
        self.__setTraceDisplacementState(0)
        self.__setIlluByDefaultState(0)
        self.__setRibNameText('')
        self.__setPictureFolderText('rmanpix' +os.sep)
        self.__setCropZoneTopText('0')
        self.__setCropZoneBottomText('1')
        self.__setCropZoneLeftText('0')
        self.__setCropZoneRightText('1')
        cmds.setAttr('liquidGlobals.xResolution', self.__RESOLUTION)
        cmds.setAttr('liquidGlobals.renderScriptFormat', 3)
        cmds.createNode('liquidGlobals', n=self.__INIT_NODE_NAME, ss=1)
    
    def __findValuesFromLiquid(self):
        iValue = 100 / (self.__RESOLUTION/(float(cmds.getAttr(
                                            'liquidGlobals.xResolution'))))
        sValue = self.__oModel.resolutionListFormat(iValue)
        sCurrentIndex   = self.__oModel.findIndex(self.__RESO_LIST, sValue)
        self.__setResolution(sCurrentIndex)
        iValue          = cmds.getAttr('liquidGlobals.doAnimation')
        iValue          = self.__oModel.invertedBool(iValue)
        iValue          = self.__oModel.double(iValue)
        self.__setCurrentFrameState(iValue)
        listFrameSeq    = self.__oModel.splitFrameValue(cmds.getAttr(
                                        'liquidGlobals.frameSequence'))         
        self.__setFrameText(listFrameSeq[0])
        self.__setByFrameText(listFrameSeq[1])
        self.__setLazynessState(self.__oModel.double(cmds.getAttr(
                                        'liquidGlobals.lazyCompute')))
        self.__setShadingRateText(str(
                    round(cmds.getAttr('liquidGlobals.shadingRate'),2)))
        self.__setPixelSampleText(str(cmds.getAttr(
                                        'liquidGlobals.pixelSamples')))
        sCurrentIndex = self.__oModel.findIndex(self.__BUCKET_SIZE_LIST, 
                        cmds.getAttr('liquidGlobals.limitsBucketXSize'))
        self.__setBucketSize(sCurrentIndex)
        sCurrentIndex = self.__oModel.findIndex(self.__GRID_SIZE_LIST, 
                        cmds.getAttr('liquidGlobals.limitsGridSize'))
        self.__setGridSize(sCurrentIndex)
#            self.__setCameraBlurState(
#                    self.__oModel.double(cmds.getAttr('liquidGlobals.cameraBlur')))
#            self.__setDOFState(
#                    self.__oModel.double(cmds.getAttr('liquidGlobals.depthOfField')))
#            self.__setSampleMotionState(
#                    self.__oModel.double(cmds.getAttr('liquidGlobals.cameraBlur')))
        sImage         = cmds.getAttr('liquidGlobals.ddImageType[0]')
        self.__testForRibOnly(sImage)
        sCurrentIndex = self.__oModel.findIndex(self.__FORMAT_LIST, sImage)
        self.__setFormat(sCurrentIndex)
        self.__setToFarmState(cmds.getAttr(
                                    'liquidGlobals.useRenderScript'))
        sCurrentCamera = cmds.getAttr('liquidGlobals.renderCamera')
        if not sCurrentCamera == "":
            if cmds.objExists(sCurrentCamera):
                sCurrentCamera = cmds.listRelatives(sCurrentCamera, p=1)[0]
                sCurrentIndex = self.__oModel.findIndex(self.__listCameras,
                                        sCurrentCamera)
            else :
                sCurrentIndex = self.__oModel.testForOnlyMayaCamera(
                                            self.__oModel.cameraListing())
        self.__setCamera(sCurrentIndex)
        sCurrentIndex = self.__oModel.findIndex(self.__FARM_GROUP_LIST, 
                                cmds.getAttr('liquidGlobals.jobPriority'))
        self.__setFarmGroup(sCurrentIndex)
        self.__setRayState(self.__oModel.double(cmds.getAttr(
                                    'liquidGlobals.useRayTracing')))
        self.__setSurfaceState(self.__oModel.double(cmds.getAttr(
                                    'liquidGlobals.ignoreSurfaces')))
        self.__setDisplacementState(self.__oModel.double(cmds.getAttr(
                                    'liquidGlobals.ignoreDisplacements')))
        self.__setSubSurfaceState(self.__oModel.double(cmds.getAttr(
                            'liquidGlobals.ignoreSubSurfaceScattering')))
        self.__setTraceDisplacementState(self.__oModel.double(cmds.getAttr(
                                    'liquidGlobals.traceDisplacements')))
        self.__setIlluByDefaultState(self.__oModel.double(cmds.getAttr(
                                    'liquidGlobals.illuminateByDefault')))
        self.__setRibNameText(cmds.getAttr(
                                    'liquidGlobals.ribName'))
        self.__setPictureFolderText(cmds.getAttr(
                                    'liquidGlobals.pictureDirectory'))
        self.__setCropZoneTopText(str(
                    round(cmds.getAttr('liquidGlobals.cropY1'),2)))
        self.__setCropZoneBottomText(str(
                    round(cmds.getAttr('liquidGlobals.cropY2'),2)))
        self.__setCropZoneLeftText(str(
                    round(cmds.getAttr('liquidGlobals.cropX1'),2)))
        self.__setCropZoneRightText(str(
                    round(cmds.getAttr('liquidGlobals.cropX2'),2)))

    #==========================================================================
    # set Methods       
    #==========================================================================
    def __setResolution(self, iValue):
        """
        Method to set the resolution format for the GUI and for liquid
        @type iValue: integer
        @param iValue: Resolution for X
        """
        self.__oGui.setResolution(iValue)
        sValue = self.__RESO_LIST[iValue]
        sValue = sValue.split('%')[0]
        iValue = float(sValue)
        iResolution = self.__RESOLUTION*iValue/100
        iResolutionY = self.__RESOLUTIONY*iValue/100
        self.__setAttr('liquidGlobals.xResolution', iResolution)
        self.__setAttr('defaultResolution.width', iResolution)
        self.__setAttr('defaultResolution.height', iResolutionY)
               
    def __setCurrentFrameState(self, iValue):
        """
        """
        self.__oGui.setCurrentFrameState(iValue)
        iValue = self.__oModel.clampedBool(iValue)
        self.__oGui.setAnimationDisabled(iValue)        
        iValue = self.__oModel.invertedBool(iValue)
        self.__setAttr('liquidGlobals.doAnimation', iValue)
       
    def __setCropZoneState(self, iValue):
        """
        """
        self.__oGui.setCropZoneState(iValue)
        iValue = self.__oModel.clampedBool(iValue)
        iValue = self.__oModel.invertedBool(iValue)
        self.__oGui.setCropZoneDisabled(iValue) 
        mel.eval('liquidCropWindowViewer();')       
    
    def __setCropZoneTopText(self, string):
        """
        """
        fValue = float(string)
        fValue = self.__oModel.keepValueBetween0n1(fValue)
        self.__setAttr('liquidGlobals.cropY1', fValue)
        self.__oGui.setCropZoneTopText(str(fValue))
    
    def __setCropZoneBottomText(self, string):
        """
        """
        fValue = float(string)
        fValue = self.__oModel.keepValueBetween0n1(fValue)
        self.__setAttr('liquidGlobals.cropY2', fValue)
        self.__oGui.setCropZoneBottomText(str(fValue))
    
    def __setCropZoneLeftText(self, string):
        """
        """
        fValue = float(string)
        fValue = self.__oModel.keepValueBetween0n1(fValue)
        self.__setAttr('liquidGlobals.cropX1', fValue)
        self.__oGui.setCropZoneLeftText(str(fValue))
    
    def __setCropZoneRightText(self, string):
        """
        """
        fValue = float(string)
        fValue = self.__oModel.keepValueBetween0n1(fValue)
        self.__setAttr('liquidGlobals.cropX2', fValue)
        self.__oGui.setCropZoneRightText(str(fValue))
    
    def __setFrameText(self, string):
        """
        """
        self.__oGui.setFrameText(string)
        self.__sFrameValue = string
        sValue = self.__oModel.setFrameValue(self.__sFrameValue, 
                                             self.__sStepValue)
        self.__setAttr('liquidGlobals.frameSequence',sValue, sType='string')

    def __setByFrameText(self, string):
        """
        """
        self.__oGui.setByFrameText(string)
        self.__sStepValue = string
        sValue = self.__oModel.setFrameValue(self.__sFrameValue, 
                                             self.__sStepValue)
        self.__setAttr('liquidGlobals.frameSequence',sValue, sType='string')
        
    def __setLazynessState(self, iValue):
        """
        """
        self.__oGui.setLazynessState(iValue)
        self.__setAttr('liquidGlobals.lazyCompute', 
                       self.__oModel.clampedBool(iValue))
        
    def __setShadingRateText(self, string):
        """
        """
        fValue = float(string)
#        fValue = round(fValue, 2)
        self.__setAttr('liquidGlobals.shadingRate', fValue)
        self.__oGui.setShadingRateText(str(fValue))
    
    def __setRibNameText(self, string):
        """
        """
        self.__oGui.setRibNameText(string)
        self.__setAttr('liquidGlobals.ribName', string, sType='string')
    
    def __setPictureFolderText(self, string):
        """
        """
        self.__oGui.setPictureFolderText(string)
        self.__setAttr('liquidGlobals.pictureDirectory', string, 
                       sType='string')
        
    def __setPixelSampleText(self, string):
        """
        """
        self.__oGui.setPixelSampleText(string)
        self.__setAttr('liquidGlobals.pixelSamples', float(string))

    def __setBucketSize(self, iValue):
        """
        """
        self.__oGui.setBucketSize(iValue)
        string = self.__BUCKET_SIZE_LIST[iValue]
        self.__setAttr('liquidGlobals.limitsBucketXSize', float(string))
        self.__setAttr('liquidGlobals.limitsBucketYSize', float(string))
                       
    def __setGridSize(self, iValue):
        """
        """
        self.__oGui.setGridSize(iValue)
        string = self.__GRID_SIZE_LIST[iValue]
        self.__setAttr('liquidGlobals.limitsGridSize', float(string))        

    def __setBitDepth(self, iValue):
        """
        """
        self.__oGui.setBitDepth(iValue)
        string = self.__BIT_DEPTH_LIST[iValue]
        string = string.replace(' bits', '')
        if string == '32':
            string = '0'            
        self.__setAttr('liquidGlobals.ddBitDepth[0]', int(string))

# Canceled
#    def __setCameraBlurState(self, iValue):
#        """
#        """
#        self.__oGui.setCameraBlurState(iValue)
#        cmds.setAttr('liquidGlobals.cameraBlur', self.__oModel.clampedBool(iValue))
        
#    def __setDOFState(self, iValue):
#        """
#        """
#        self.__oGui.setDOFState(iValue)
#        cmds.setAttr('liquidGlobals.depthOfField', self.__oModel.clampedBool(iValue))
        
#    def __setSampleMotionState(self, iValue):
#        """
#        """
#        self.__oGui.setSampleMotionState(iValue)
#        cmds.setAttr('liquidGlobals.hiddenSampleMotion',
#                     self.__oModel.clampedBool(iValue))
# Canceled

    def __setFormat(self, iValue):
        """
        """
        self.__oGui.setFormat(iValue)
        string = self.__FORMAT_LIST[iValue]
        self.__setAttr('liquidGlobals.ddImageType[0]', string,
                       sType ='string')
        self.__testForRibOnly(string)

    def __setCamera(self, iValue):
        """
        """
#        self.__oGui.setCameraList(self.__listCameras)
#        self.__oGui.refreshCameraList()
        self.__oGui.setCamera(iValue)
        string = self.__listCameras[iValue]
        string = cmds.listRelatives(string)[0]
        self.__setAttr('liquidGlobals.renderCamera', string, sType='string')

    def __setToFarmState(self, iValue):
        """
        """
        self.__oGui.setToFarmState(iValue)
        self.__setAttr('liquidGlobals.useRenderScript', iValue)
        iValue = self.__oModel.text2Bool(str(iValue))*3
        self.__setAttr('liquidGlobals.renderScriptFormat', iValue)
        
    def __setFarmGroup(self, iValue):
        """
        """
        self.__oGui.setFarmGroup(iValue)
        string = self.__FARM_GROUP_LIST[iValue]
        self.__setAttr('liquidGlobals.jobPriority', string, sType='string')
       
    def __setRayState(self, iValue):
        """
        """
        self.__oGui.setRayState(iValue)
        self.__setAttr('liquidGlobals.useRayTracing', 
                       self.__oModel.clampedBool(iValue))
       
    def __setSurfaceState(self, iValue):
        """
        """
        self.__oGui.setSurfaceState(iValue)
        self.__setAttr('liquidGlobals.ignoreSurfaces', 
                       self.__oModel.clampedBool(iValue))
        
    def __setDisplacementState(self, iValue):
        """
        """
        self.__oGui.setDisplacementState(iValue)
        self.__setAttr('liquidGlobals.ignoreDisplacements', 
                       self.__oModel.clampedBool(iValue))
        
    def __setSubSurfaceState(self, iValue):
        """
        """
        self.__oGui.setSubSurfaceState(iValue)
        self.__setAttr('liquidGlobals.ignoreSubSurfaceScattering', 
                       self.__oModel.clampedBool(iValue))
    
    def __setBakeState(self, iValue):
        """
        """
        self.__oGui.setBakeState(iValue)
        iClampedValue = self.__oModel.clampedBool(iValue)
        iClampedValue = self.__oModel.invertedBool(iClampedValue)
        self.__setAttr('liquidGlobals.bakeCullHidden',iClampedValue)
        self.__setAttr('liquidGlobals.bakeCullBackface',iClampedValue)
        self.__setAttr('liquidGlobals.bakeRasterOrient',iClampedValue)
        
    def __setTraceDisplacementState(self, iValue):
        """
        """
        self.__oGui.setTraceDisplacementState(iValue)
        self.__setAttr('liquidGlobals.traceDisplacements', 
                       self.__oModel.clampedBool(iValue))
        
    def __setIlluByDefaultState(self, iValue):
        """
        """
        self.__oGui.setIlluByDefaultState(iValue)
        iValue = self.__oModel.clampedBool(iValue)
        self.__setAttr('liquidGlobals.illuminateByDefault',iValue)
        self.__setAttr('liquidGlobals.liquidSetLightLinking',
                       self.__oModel.invertedBool(iValue))
        
    def __setPrintModeState(self, iValue):
        """
        """
        self.__oGui.setPrintModeState(iValue)
        self.__boolPrintMode = self.__oModel.clampedBool(iValue)
    #==========================================================================
    # Answers to QtCore.SIGNALs
    #==========================================================================
    def __ribName_onClick(self):
        """
        """
        sPath = self.__oModel.getPath('')
        sPath += os.sep
        sPath += 'rib'
        self.__oModel.openFolder(sPath)

    def __pictureFolder_onClick(self):
        """
        """
        sPath = self.__oModel.getPath('liquidGlobals.pictureDirectory')
        self.__oModel.openFolder(sPath)
                              
    def __camera_onClick(self):
        self.__listCameras = self.__oModel.cameraListing()
        self.__oGui.setCameraList(self.__listCameras)
        self.__oGui.refreshCameraList()
#        self.__setCamera(self.__oModel.testForOnlyMayaCamera(
#                                                    self.__listCameras))    
    def __renderButton_onClick(self, iValue):
        self.__setToFarmState(iValue)
        mel.eval('liquidRender;')
        
    def __renderSelectionButton_onClick(self):
        if cmds.ls(sl=1):
            mel.eval('liquidRenderSelected;')
        else :
            self.__oGui.showErrorDialog('No Selection')
    
    def __add2SetButton_onClick(self):
        if cmds.objExists(self.__SET_NAME):
            cmds.sets(cmds.ls(sl=1), add=self.__SET_NAME)
        else:
            cmds.sets(n=self.__SET_NAME)
       
    def __remove2SetButton_onClick(self):
        if cmds.objExists(self.__SET_NAME):
            cmds.sets(cmds.ls(sl=1), remove=self.__SET_NAME) 
    
    def __clearSetButton_onClick(self):
        if cmds.objExists(self.__SET_NAME):
            cmds.sets(cl=self.__SET_NAME)
            
    def __renderSet_onClick(self):
        if cmds.objExists(self.__SET_NAME):
            listCurrentSel = cmds.ls(sl=1)
            cmds.select(self.__SET_NAME, r=1)
            mel.eval('liquidRenderSelected;')
            cmds.select(listCurrentSel, r=1)
        else :
            self.__oGui.showErrorDialog('Set Not Found')
    
    def __liquid_onClick(self):
        self.__setValues()
    
    def __liquidGlobals_onClick(self):
        mel.eval('unifiedRenderGlobalsWindow;')
    
    def __hideOthers_onClick(self):
        if self.__iHideOthers == 0:
            self.__iHideOthers = 1
        else :
            self.__iHideOthers = 0
        self.__oGui.setHideOthers(self.__iHideOthers)
    
    def __hide_onClick(self):
        if self.__iHideUI == 0:
            self.__iHideUI = 1
        else :
            self.__iHideUI = 0
        self.__oGui.setHideUI(self.__iHideUI)
    #==========================================================================
    # private methods    
    #==========================================================================
    def __testForRibOnly(self, string):
        if 'rib' in string :
            self.__setAttr('liquidGlobals.justRib',1)
        else :
            self.__setAttr('liquidGlobals.justRib',0)
    
    def __printAttr(self, string):
        print string, cmds.getAttr(string), '\n'
        
    def __setAttr(self, sAttr, value, sType=''):
        if sType == '':
            cmds.setAttr(sAttr, value)
        else :
            cmds.setAttr(sAttr, value, type=sType)
        if self.__boolPrintMode == 1:
            self.__printAttr(sAttr)

    #==========================================================================
    # SIGNALS
    #==========================================================================
    def __signals(self):
        
        self.connect(self.__oGui, QtCore.SIGNAL('currentFrame_onClick'),
                     self.__setCurrentFrameState)
        self.connect(self.__oGui, QtCore.SIGNAL('frame_onChanged'),
                     self.__setFrameText)
        self.connect(self.__oGui, QtCore.SIGNAL('byFrame_onChanged'),
                     self.__setByFrameText)
        '''
        sWorkFolder = self.__workfolder()
        print sWorkFolder
        getTaskFromPath() << gimme the task from the project folder
        oServer.query(searchType, filter=(('id', search_id), )
        '''
        self.connect(self.__oGui, QtCore.SIGNAL('SME_onClick'),
                     self.__setFrameText)
        self.connect(self.__oGui, QtCore.SIGNAL('shotTimeline_onClick'),
                     self.__setFrameText)  
        self.connect(self.__oGui, QtCore.SIGNAL('shadingRate_onChanged'),
                     self.__setShadingRateText)
        self.connect(self.__oGui, QtCore.SIGNAL('pixelSamples_onChanged'),
                     self.__setPixelSampleText)
        self.connect(self.__oGui, QtCore.SIGNAL('ribName_onChanged'),
                     self.__setRibNameText)
        self.connect(self.__oGui, QtCore.SIGNAL('ribName_onClick'),
                     self.__ribName_onClick)
        self.connect(self.__oGui, QtCore.SIGNAL('pictureFolder_onChanged'),
                     self.__setPictureFolderText)
        self.connect(self.__oGui, QtCore.SIGNAL('pictureFolder_onClick'),
                     self.__pictureFolder_onClick)
        self.connect(self.__oGui, QtCore.SIGNAL('bitDepth_onChanged'),
                     self.__setBitDepth)
# Canceled
#        self.connect(self.__oGui,
#                     QtCore.SIGNAL('camBlur_onClick'),
#                     self.__camBlur_onClick)
#        self.connect(self.__oGui,
#                     QtCore.SIGNAL('DOF_onClick'),
#                     self.__DOF_onClick)
#        self.connect(self.__oGui,
#                     QtCore.SIGNAL('sampleMotionOptions_onClick'),
#                     self.__sampleMotionOptions_onClick)
# Canceled
        self.connect(self.__oGui, QtCore.SIGNAL('bucketSize_onChanged'),
                     self.__setBucketSize)
        self.connect(self.__oGui, QtCore.SIGNAL('gridSize_onChanged'),
                     self.__setGridSize)
        
        #======================================================================
        # Output
        #======================================================================
        self.connect(self.__oGui, QtCore.SIGNAL('cropZone_onClick'),
                     self.__setCropZoneState)
        self.connect(self.__oGui, QtCore.SIGNAL('cropZoneTop_onChanged'),
                     self.__setCropZoneTopText)
        self.connect(self.__oGui, QtCore.SIGNAL('cropZoneBottom_onChanged'),
                     self.__setCropZoneBottomText)
        self.connect(self.__oGui, QtCore.SIGNAL('cropZoneLeft_onChanged'),
                     self.__setCropZoneLeftText)
        self.connect(self.__oGui, QtCore.SIGNAL('cropZoneRight_onChanged'),
                     self.__setCropZoneRightText)
        self.connect(self.__oGui, QtCore.SIGNAL('lazyness_onClick'),
                     self.__setLazynessState)
        self.connect(self.__oGui, QtCore.SIGNAL('resoComboBox_onChanged'),
                     self.__setResolution)
        self.connect(self.__oGui, QtCore.SIGNAL('camera_onChanged'),
                     self.__setCamera)
        self.connect(self.__oGui, QtCore.SIGNAL('camera_onClick'),
                     self.__camera_onClick)
        self.connect(self.__oGui, QtCore.SIGNAL('format_onChanged'),
                     self.__setFormat)
        self.connect(self.__oGui, QtCore.SIGNAL('toFarmBloc_onClick'),
                     self.__setToFarmState)
        self.connect(self.__oGui, QtCore.SIGNAL('farmGroup_onChanged'),
                     self.__setFarmGroup)
        #======================================================================
        # Advanced
        #======================================================================
        self.connect(self.__oGui, QtCore.SIGNAL('ray_onClick'),
                     self.__setRayState)
        self.connect(self.__oGui, QtCore.SIGNAL('surface_onClick'),
                     self.__setSurfaceState)
        self.connect(self.__oGui, QtCore.SIGNAL('displacement_onClick'),
                     self.__setDisplacementState)
        self.connect(self.__oGui, QtCore.SIGNAL('subsurface_onClick'),
                     self.__setSubSurfaceState)
        self.connect(self.__oGui, QtCore.SIGNAL('bake_onClick'),
                     self.__setBakeState)
        self.connect(self.__oGui, QtCore.SIGNAL('traceDispl_onClick'),
                     self.__setTraceDisplacementState)
        self.connect(self.__oGui, QtCore.SIGNAL('illuByDefault_onClick'),
                     self.__setIlluByDefaultState)
        #======================================================================
        # print Mode
        #======================================================================
        self.connect(self.__oGui, QtCore.SIGNAL('printMode_onClick'),
                     self.__setPrintModeState)
        #======================================================================
        # Buttons
        #======================================================================
        self.connect(self.__oGui, QtCore.SIGNAL('renderButton_onClick'),
                     self.__renderButton_onClick)
        self.connect(self.__oGui, 
                     QtCore.SIGNAL('renderSelectionButton_onClick'),
                     self.__renderSelectionButton_onClick)
        self.connect(self.__oGui, QtCore.SIGNAL('add2SetButton_onClick'),
                     self.__add2SetButton_onClick)
        self.connect(self.__oGui, QtCore.SIGNAL('remove2SetButton_onClick'),
                     self.__remove2SetButton_onClick)
        self.connect(self.__oGui, QtCore.SIGNAL('clearSetButton_onClick'),
                     self.__clearSetButton_onClick)
        self.connect(self.__oGui, QtCore.SIGNAL('renderSet_onClick'),
                     self.__renderSet_onClick)
        self.connect(self.__oGui, QtCore.SIGNAL('liquid_onClick'),
                     self.__liquid_onClick)
        self.connect(self.__oGui, QtCore.SIGNAL('liquidGlobals_onClick'),
                     self.__liquidGlobals_onClick)
        self.connect(self.__oGui, QtCore.SIGNAL('hide_onClick'),
                     self.__hide_onClick)
        self.connect(self.__oGui, QtCore.SIGNAL('hideOthers_onClick'),
                     self.__hideOthers_onClick)
# Ni!
