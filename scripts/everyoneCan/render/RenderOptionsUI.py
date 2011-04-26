# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from everyoneCan import CustomWidgets as cw
reload(cw)
from everyoneCan import UIs
reload(UIs)
from everyoneCan import SharedConstants

#tl                          = SharedConstants.TypeLister()
scc                         = SharedConstants.Constants()

class Gui(QtGui.QMainWindow):
    """
    Graphic Interface of lightOptions tool
    Discuss with controlor through an observer
    """
    #==========================================================================
    # variables
    #==========================================================================
    __listCameras       = []
    name                = __name__

    def __init__(self, boolSelfLaunch):
        """
        @type boolSelfLaunch: int boolean
        @param boolSelfLaunch: indicate if the tool is launched as
                standalone (1) or not (0)
        """
        self.__boolSelfLaunch = boolSelfLaunch
        QtGui.QMainWindow.__init__(self)

    def main(self):
        def __hideOthers_onClick():
            self.emit(QtCore.SIGNAL('hideOthers_onClick'))

        oCentralWidget                  = QtGui.QWidget()
        oMainLayout                     = QtGui.QVBoxLayout(oCentralWidget)
        oMainLayout.setContentsMargins(0,0,0,0)
        self.__renderButtons(oMainLayout)
        self.__oOutPutLayoutParent      = QtGui.QWidget()
        oOutputLayout                   = QtGui.QVBoxLayout(self.__oOutPutLayoutParent)
        oOutputLayout.setContentsMargins(0,0,0,0)
#        self.__output(oOutputLayout)

        oHideOthersButton               = QtGui.QPushButton()
        oHideOthersButton = QtGui.QPushButton()
        oHideOthersButton.setMaximumHeight(10)
        self.connect(oHideOthersButton,
                     QtCore.SIGNAL('clicked()'),
                     __hideOthers_onClick)

        self.__output(oOutputLayout)
        oOutputLayout.addWidget(oHideOthersButton)

        self.__oOtherLayoutParent       = QtGui.QWidget()
        oOtherLayout                    = QtGui.QVBoxLayout(self.__oOtherLayoutParent)
        oOtherLayout.setContentsMargins(0,0,0,0)
        self.__animation(oOtherLayout)
        self.__image(oOtherLayout)
        self.__advanced(oOtherLayout)
        oOtherLayout.addWidget(UIs.AllOthersUIWidget(__name__))
        oOtherLayout.addWidget(self.__printMode())

        oMainLayout.addWidget(self.__oOutPutLayoutParent)
        oMainLayout.addWidget(self.__oOtherLayoutParent)
        oMainLayout.addStretch(1)
        # if the tool is launched as standalone
        # we need to set its centralWidget
        if self.__boolSelfLaunch == 1:
            self.setCentralWidget(oCentralWidget)

    def showErrorDialog(self, string):
        oDialog = QtGui.QErrorMessage(self)
        oDialog.showMessage(string)
    #==========================================================================
    # setting of list of ComboBoxes
    #==========================================================================
    def setFormatList(self, list):
        self.__listFormats = list

    def setCameraList(self, list):
        self.__listCameras = list

    def setResoList(self, list):
        self.__listResolutions = list

    def setBucketSizeList(self, list):
        self.__listBucketSizes = list

    def setGridSizeList(self, list):
        self.__listGridSizes = list

    def setFarmGroupList(self, list):
        self.__listFramGroups = list

    def setBitDepthList(self, list):
        self.__listBitDepths = list
    #==========================================================================
    # get and set methods
    #==========================================================================
    def setResolution(self, int):
        self.__oResoComboBox.setCurrentIndex(int)

    def setCurrentFrameState(self, int):
        self.__oCurrentFrame.setCheckState(int)

    def setAnimationDisabled(self, int):
        self.__oSMEPushButton.setHidden(int)
        self.__oShotTimelineButton.setHidden(int)
        self.__oGroupLabelFrame.setHidden(int)
        self.__oGroupLabelByFrame.setHidden(int)
        self.setMaximumHeight(1)

    def setFrameText(self, string):
        self.__oFrame.setText(string)

    def setByFrameText(self, string):
        self.__oByFrame.setText(string)

    def setLazynessState(self, int):
        self.__oLazynessCheckBox.setCheckState(int)

    def setCropZoneState(self, int):
        self.__oCropZoneCheckBox.setCheckState(int)

    def setCropZoneDisabled(self, int):
        self.__oCropZoneTopGroupBox.setHidden(int)
        self.__oCropZoneBottomGroupBox.setHidden(int)
        self.__oCropZoneLeftGroupBox.setHidden(int)
        self.__oCropZoneRightGroupBox.setHidden(int)
        self.setMaximumHeight(1)

    def setCropZoneTopText(self, string):
        self.__oCropZoneTopLineEdit.setText(string)

    def setCropZoneBottomText(self, string):
        self.__oCropZoneBottomLineEdit.setText(string)

    def setCropZoneLeftText(self, string):
        self.__oCropZoneLeftLineEdit.setText(string)

    def setCropZoneRightText(self, string):
        self.__oCropZoneRightLineEdit.setText(string)

    def setShadingRateText(self, string):
        self.__oShadingRate.setText(string)

    def setPixelSampleText(self, string):
        self.__oPixelSamples.setText(string)

    def setRibNameText(self, string):
        self.__oRibName.setText(string)

    def setRibNameState(self, int):
        self.__oRibNameButton.setCheckState(int)

    def setPictureFolderText(self, string):
        self.__oPictureFolder.setText(string)

    def setPictureFolderState(self, int):
        self.__oPictureFolderButton.setCheckState(int)

    def setBitDepth(self, int):
        self.__oBitDepthComboBox.setCurrentIndex(int)

    def setBucketSize(self, int):
        self.__oBucketSizeComboBox.setCurrentIndex(int)

    def setGridSize(self, int):
        self.__oGridSizeComboBox.setCurrentIndex(int)

    def setFormat(self, int):
        self.__oFormatComboBox.setCurrentIndex(int)

    def setCamera(self, int):
        self.__oCameraComboBox.setCurrentIndex(int)

    def refreshCameraList(self):
        self.__oCameraComboBox.clear()
        self.__oCameraComboBox.addItems(self.__listCameras)

    def setToFarmState(self, bool):
        self.__oToFarmBloc.setChecked(bool)

    def setFarmGroup(self, int):
        self.__oFarmGroupComboBox.setCurrentIndex(int)

    def setRayState(self, int):
        self.__oRayCheckBox.setCheckState(int)

    def setSurfaceState(self, int):
        self.__oSurfaceCheckBox.setCheckState(int)

    def setDisplacementState(self, int):
        self.__oDisplCheckBox.setCheckState(int)

    def setSubSurfaceState(self, int):
        self.__osubsurfaceCheckBox.setCheckState(int)

    def setBakeState(self, int):
        self.__oBakeCheckBox.setCheckState(int)

    def setTraceDisplacementState(self, int):
        self.__oTraceDisplCheckBox.setCheckState(int)

    def setIlluByDefaultState(self, int):
        self.__oIlluByDefaultCheckBox.setCheckState(int)

    def setPrintModeState(self, int):
        self.__oPrintMode.setCheckState(int)


    def setHideOthers(self, int):
        self.__oOtherLayoutParent.setHidden(int)

    def setHideUI(self, int):
        self.__oOutPutLayoutParent.setHidden(int)
        self.__oOtherLayoutParent.setHidden(int)

    def __animation(self, oMasterLayout):
        def __currentFrame_onClick():
                self.emit(QtCore.SIGNAL('currentFrame_onClick'),
                          self.__oCurrentFrame.checkState())

        def __frame_onChanged():
            self.emit(QtCore.SIGNAL('frame_onChanged'),
                      self.__oFrame.text())

        def __byFrame_onChanged():
            self.emit(QtCore.SIGNAL('byFrame_onChanged'),
                      self.__oByFrame.text())

        def __timeline():
            def __shotTimeline_onClick():
                self.emit(QtCore.SIGNAL('shotTimeline_onClick'),
                          'Start-End')

#            def __currentTimeline_onClick():
#                self.emit(QtCore.SIGNAL('currentTimeline_onClick'),
#                          CurrentStart-CurrentEnd)

            def __SME_onClick():
                self.emit(QtCore.SIGNAL('SME_onClick'),
                          'Start,Middle,End')

            self.__oSMEPushButton = QtGui.QPushButton('S.M.E.')
            self.connect(self.__oSMEPushButton, QtCore.SIGNAL('clicked()'),
                        __SME_onClick)
            self.__oShotTimelineButton = QtGui.QPushButton('Shot')
            self.connect(self.__oShotTimelineButton,
                         QtCore.SIGNAL('clicked()'),
                        __shotTimeline_onClick)
#            self.__oCurrentTimelinePushButton = QtGui.QPushButton('Current')
#            self.connect(self.__oCurrentTimelinePushButton,
#                         QtCore.SIGNAL('clicked()'),
#                        __currentTimeline_onClick)
            self.__oSeveralParent = QtGui.QWidget()
            self.__oSeveralFramesLayout = QtGui.QVBoxLayout()
            self.__setContentMargins0(self.__oSeveralFramesLayout)
            self.__oSeveralFramesLayout.addWidget(
                                        self.__oSMEPushButton)
            self.__oSeveralFramesLayout.addWidget(self.__oShotTimelineButton)
            self.__oSeveralParent.setLayout(self.__oSeveralFramesLayout)
            self.__oSeveralLabel = cw.AlGroupLabel('', self.__oSeveralParent)
            return self.__oSeveralLabel

        self.__oCurrentFrame = QtGui.QCheckBox()
        self.__oCurrentFrameGroupLabel = cw.AlGroupLabel('Current frame :',
                                        self.__oCurrentFrame)
        self.connect(self.__oCurrentFrame,QtCore.SIGNAL('clicked()'),
                         __currentFrame_onClick)
        self.__oFrame = cw.AlLineEdit()
        self.__oGroupLabelFrame = cw.AlGroupLabel('Frame :',self.__oFrame)
        self.__lineEditActions(self.__oFrame,__frame_onChanged)
        self.__oByFrame = cw.AlLineEdit()
        self.__oGroupLabelByFrame = cw.AlGroupLabel('by Frame :',
                                        self.__oByFrame)
        self.__lineEditActions(self.__oByFrame,__byFrame_onChanged)
        self.__oAnimationParent = QtGui.QWidget()
        self.__oAnimationLayout = cw.AlVBoxLayout()
        self.__oAnimationLayout.setContentsMargins(0,0,0,0)
        self.__oAnimationLayout.addWidget(self.__oCurrentFrameGroupLabel)
        self.__oAnimationLayout.addWidget(__timeline())
        self.__oAnimationLayout.addWidget(self.__oGroupLabelFrame)
        self.__oAnimationLayout.addWidget(self.__oGroupLabelByFrame)
        self.__oAnimationParent.setLayout(self.__oAnimationLayout)
        self.__oAnimationBloc = cw.AlBloc(self, scc.ANIMATION_ICON,
                                     'Animation :', self.__oAnimationParent)
        oMasterLayout.addWidget(self.__oAnimationBloc)

    def __image(self, oMasterLayout):
        def __shadingRate():
            def __shadingRate_onChanged():
                self.emit(QtCore.SIGNAL('shadingRate_onChanged'),
                          self.__oShadingRate.text())

            self.__oShadingRate = cw.AlLineEdit()
            self.__oGroupLabelShadingRate = cw.AlGroupLabel(
                                            'Shading Rate :',
                                            self.__oShadingRate)
            self.__lineEditActions(self.__oShadingRate,
                                   __shadingRate_onChanged)
            return self.__oGroupLabelShadingRate

        def __pixelSamples():
            def __pixelSamples_onChanged():
                self.emit(QtCore.SIGNAL('pixelSamples_onChanged'),
                          self.__oPixelSamples.text())

            self.__oPixelSamples = cw.AlLineEdit()
            self.__oGroupLabelPixelSamples = cw.AlGroupLabel(
                                            'Pixel Samples :',
                                            self.__oPixelSamples)
            self.__lineEditActions(self.__oPixelSamples,
                                   __pixelSamples_onChanged)
            return self.__oGroupLabelPixelSamples

        def __bucketSize():
            def __bucketSize_onChanged():
                self.emit(QtCore.SIGNAL('bucketSize_onChanged'),
                          self.__oBucketSizeComboBox.currentIndex())

            self.__oBucketSizeLayout = cw.AlVBoxLayout()
            self.__oBucketSizeComboBox = cw.AlComboBox(
                                                    self.__listBucketSizes)
            self.__oBucketSizeGrpLabel = cw.AlGroupLabel('Bucket Size :',
                                                self.__oBucketSizeComboBox)
            self.connect(self.__oBucketSizeComboBox,
                         QtCore.SIGNAL('currentIndexChanged(int)'),
                         __bucketSize_onChanged)
            return self.__oBucketSizeGrpLabel

        def __gridSize():
            def __gridSize_onChanged():
                self.emit(QtCore.SIGNAL('gridSize_onChanged'),
                          self.__oGridSizeComboBox.currentIndex())

            self.__oGridSizeLayout = cw.AlVBoxLayout()
            self.__oGridSizeComboBox = cw.AlComboBox(
                                                self.__listGridSizes)
            self.__oGridSizeGrpLabel = cw.AlGroupLabel('Grid Size :',
                                                self.__oGridSizeComboBox)
            self.connect(self.__oGridSizeComboBox,
                         QtCore.SIGNAL('currentIndexChanged(int)'),
                         __gridSize_onChanged)
            return self.__oGridSizeGrpLabel

        def __ribName():
            def __ribName_onChanged():
                self.emit(QtCore.SIGNAL('ribName_onChanged'),
                          self.__oRibName.text())

            def __ribName_onClick():
                self.emit(QtCore.SIGNAL('ribName_onClick'))

            self.__oRibNameParent = QtGui.QWidget()
            self.__oRibNameLayout = QtGui.QHBoxLayout()
            self.__setContentMargins0(self.__oRibNameLayout)
            self.__oRibName = cw.AlLineEdit()
            self.__oRibName.setMinimumWidth(140)
            self.__oRibNameButton = QtGui.QPushButton('open')
            self.__oRibNameButton.setMaximumWidth(40)
            self.__oRibNameLayout.addWidget(self.__oRibName)
            self.__oRibNameLayout.addWidget(self.__oRibNameButton)
            self.__oRibNameParent.setLayout(self.__oRibNameLayout)

            self.__oGroupLabelRibName = cw.AlGroupLabel(
                                            'Rib Basename :',
                                            self.__oRibNameParent)
            self.__lineEditActions(self.__oRibName,
                                   __ribName_onChanged)
            self.connect(self.__oRibNameButton,
                         QtCore.SIGNAL('clicked()'),
                         __ribName_onClick)
            return self.__oGroupLabelRibName

        def __pictureFolder():
            def __pictureFolder_onChanged():
                self.emit(QtCore.SIGNAL('pictureFolder_onChanged'),
                          self.__oPictureFolder.text())

            def __pictureFolder_onClick():
                self.emit(QtCore.SIGNAL('pictureFolder_onClick'))

            self.__oPictureFolderParent = QtGui.QWidget()
            self.__oPictureFolderLayout = QtGui.QHBoxLayout()
            self.__setContentMargins0(self.__oPictureFolderLayout)
            self.__oPictureFolder = cw.AlLineEdit()
            self.__oPictureFolderButton = QtGui.QPushButton('open')
            self.__oPictureFolderButton.setMaximumWidth(40)
            self.__oPictureFolderLayout.addWidget(self.__oPictureFolder)
            self.__oPictureFolderLayout.addWidget(self.__oPictureFolderButton)
            self.__oPictureFolderParent.setLayout(self.__oPictureFolderLayout)

            self.__oGroupLabelPictureFolder = cw.AlGroupLabel(
                                            'Picture Folder :',
                                            self.__oPictureFolderParent)
            self.__lineEditActions(self.__oPictureFolder,
                                   __pictureFolder_onChanged)
            self.connect(self.__oPictureFolderButton,
                         QtCore.SIGNAL('clicked()'),
                         __pictureFolder_onClick)
            return self.__oGroupLabelPictureFolder

        def __bitDepth():
            def __bitDepth_onChanged():
                self.emit(QtCore.SIGNAL('bitDepth_onChanged'),
                          self.__oBitDepthComboBox.currentIndex())

            self.__oBitDepthLayout = cw.AlVBoxLayout()
            self.__oBitDepthComboBox = cw.AlComboBox(
                                                self.__listBitDepths)
            self.__oBitDepthGrpLabel = cw.AlGroupLabel('Bit Depth :',
                                                self.__oBitDepthComboBox)
            self.connect(self.__oBitDepthComboBox,
                         QtCore.SIGNAL('currentIndexChanged(int)'),
                         __bitDepth_onChanged)
            return self.__oBitDepthGrpLabel

        self.__oImageParent = QtGui.QWidget()
        self.__oImageFrame = cw.AlVBoxLayout()
        self.__oImageFrame.addWidget(__shadingRate())
        self.__oImageFrame.addWidget(__pixelSamples())
        self.__oImageFrame.addWidget(__bucketSize())
        self.__oImageFrame.addWidget(__gridSize())
        self.__oImageFrame.addWidget(__ribName())
        self.__oImageFrame.addWidget(__pictureFolder())
        self.__oImageFrame.addWidget(__bitDepth())
        self.__oImageParent.setLayout(self.__oImageFrame)
        self.__oImageBloc = cw.AlBloc(self, scc.IMAGE_ICON,
                                           'Image :',
                                           self.__oImageParent)
        oMasterLayout.addWidget(self.__oImageBloc)

    def __output(self, oMasterLayout):
        def __format():
            def __format_onChanged():
                self.emit(QtCore.SIGNAL('format_onChanged'),
                          self.__oFormatComboBox.currentIndex())

            self.__oFormatComboBox = cw.AlComboBox(self.__listFormats)
            oFormatGrpLabel = cw.AlGroupLabel('Format :',
                                                self.__oFormatComboBox)
            self.connect(self.__oFormatComboBox,
                         QtCore.SIGNAL('currentIndexChanged(int)'),
                         __format_onChanged)
            return oFormatGrpLabel

        def __toFarm():
            def __toFarmBloc_onClick():
                self.emit(QtCore.SIGNAL('toFarmBloc_onClick'),
                          self.__oToFarmBloc.isChecked())

            def __farmGroup_onChanged():
                self.emit(QtCore.SIGNAL('farmGroup_onChanged'),
                          self.__oFarmGroupComboBox.currentIndex())

            self.__oToFarmBloc = cw.AlGroupBox('ToFarm')
            self.__oToFarmBloc.setCheckable(1)
            self.__oToFarmBloc.setChecked(0)
            self.__setContentMargins10(self.__oToFarmBloc)
            self.connect(self.__oToFarmBloc,
                         QtCore.SIGNAL('clicked()'),
                        __toFarmBloc_onClick)
            oToFarmLayout = QtGui.QVBoxLayout(self.__oToFarmBloc)
            self.__oFarmGroupComboBox = cw.AlComboBox(
                                                self.__listFramGroups)
            oFarmGroupGrpLabel = cw.AlGroupLabel('Farm Group :',
                                                self.__oFarmGroupComboBox)
            self.connect(self.__oFarmGroupComboBox,
                         QtCore.SIGNAL('currentIndexChanged(int)'),
                         __farmGroup_onChanged)
            oToFarmLayout.addWidget(oFarmGroupGrpLabel)
            return self.__oToFarmBloc

        def __camera():
            def __camera_onChanged():
                self.emit(QtCore.SIGNAL('camera_onChanged'),
                          self.__oCameraComboBox.currentIndex())

            def __camera_onClick():
                self.emit(QtCore.SIGNAL('camera_onClick'))

            oCameraPushButton = QtGui.QPushButton('refresh')
            oCameraPushButton.setMaximumWidth(45)
            self.connect(oCameraPushButton,
                         QtCore.SIGNAL('clicked()'),
                         __camera_onClick)
            self.__oCameraComboBox = cw.AlComboBox(self.__listCameras)
            self.connect(self.__oCameraComboBox,
                         QtCore.SIGNAL('currentIndexChanged(int)'),
                         __camera_onChanged)
            oCameraButtonsParent = QtGui.QWidget()
            oCameraButtonsLayout = cw.AlHBoxLayout()
            oCameraButtonsLayout.addWidget(self.__oCameraComboBox)
            oCameraButtonsLayout.addWidget(oCameraPushButton)
            oCameraButtonsParent.setLayout(oCameraButtonsLayout)
            oCameraGrpLabel = cw.AlGroupLabel('Camera :',
                                              oCameraButtonsParent)

            return oCameraGrpLabel

        def __resolution():
            def __resoComboBox_onChanged():
                self.emit(QtCore.SIGNAL('resoComboBox_onChanged'),
                          self.__oResoComboBox.currentIndex())

            oResoLayout = cw.AlVBoxLayout()
            self.__oResoComboBox = cw.AlComboBox(self.__listResolutions)
            oResoGrpLabel = cw.AlGroupLabel('Resolution :',
                                            self.__oResoComboBox)
            self.connect(self.__oResoComboBox,
                         QtCore.SIGNAL('currentIndexChanged(int)'),
                         __resoComboBox_onChanged)
            return oResoGrpLabel

        def __lazyness():
            def __lazyness_onClick():
                self.emit(QtCore.SIGNAL('lazyness_onClick'),
                          self.__oLazynessCheckBox.checkState())

            self.__oLazynessCheckBox = QtGui.QCheckBox()
            oLazynessGroupLabel = cw.AlGroupLabel('Lazyness :',
                                                  self.__oLazynessCheckBox)
            self.connect(self.__oLazynessCheckBox,
                         QtCore.SIGNAL('clicked()'),
                         __lazyness_onClick)

            return oLazynessGroupLabel

        def __cropZone():
            def __cropZone_onClick():
                self.emit(QtCore.SIGNAL('cropZone_onClick'),
                          self.__oCropZoneCheckBox.checkState())

            def __cropZoneTop_onChanged():
                self.emit(QtCore.SIGNAL('cropZoneTop_onChanged'),
                          self.__oCropZoneTopLineEdit.text())

            def __cropZoneBottom_onChanged():
                self.emit(QtCore.SIGNAL('cropZoneBottom_onChanged'),
                          self.__oCropZoneBottomLineEdit.text())

            def __cropZoneLeft_onChanged():
                self.emit(QtCore.SIGNAL('cropZoneLeft_onChanged'),
                          self.__oCropZoneLeftLineEdit.text())

            def __cropZoneRight_onChanged():
                self.emit(QtCore.SIGNAL('cropZoneRight_onChanged'),
                          self.__oCropZoneRightLineEdit.text())

            self.__oCropZoneCheckBox = QtGui.QCheckBox()
            oCropZoneCheckBoxGroupLabel = cw.AlGroupLabel('Crop Zone :',
                                        self.__oCropZoneCheckBox)
            self.connect(self.__oCropZoneCheckBox,QtCore.SIGNAL('clicked()'),
                         __cropZone_onClick)
            self.__oCropZoneTopLineEdit = cw.AlWheelLineEdit(0,1)
            self.__oCropZoneTopLineEdit.setMiddleClickTrickFactor(0.01)
            self.__oCropZoneTopGroupBox = cw.AlGroupLabel('Top :',
                                            self.__oCropZoneTopLineEdit)
            self.__lineEditActions(self.__oCropZoneTopLineEdit,
                                   __cropZoneTop_onChanged)
            self.__oCropZoneBottomLineEdit = cw.AlWheelLineEdit(0,1)
            self.__oCropZoneBottomLineEdit.setMiddleClickTrickFactor(0.01)
            self.__oCropZoneBottomGroupBox = cw.AlGroupLabel('Bottom :',
                                            self.__oCropZoneBottomLineEdit)
            self.__lineEditActions(self.__oCropZoneBottomLineEdit,
                                   __cropZoneBottom_onChanged)

            self.__oCropZoneLeftLineEdit = cw.AlWheelLineEdit(0,1)
            self.__oCropZoneLeftLineEdit.setMiddleClickTrickFactor(0.01)
            self.__oCropZoneLeftGroupBox = cw.AlGroupLabel('Left :',
                                            self.__oCropZoneLeftLineEdit)
            self.__lineEditActions(self.__oCropZoneLeftLineEdit,
                                   __cropZoneLeft_onChanged)
            self.__oCropZoneRightLineEdit = cw.AlWheelLineEdit(0,1)
            self.__oCropZoneRightLineEdit.setMiddleClickTrickFactor(0.01)
            self.__oCropZoneRightGroupBox = cw.AlGroupLabel('Right :',
                                            self.__oCropZoneRightLineEdit)
            self.__lineEditActions(self.__oCropZoneRightLineEdit,
                                   __cropZoneRight_onChanged)
            oCropZoneLayout = QtGui.QVBoxLayout()
            oCropZoneLayout.addWidget(oCropZoneCheckBoxGroupLabel)
            oCropZoneLayout.addWidget(self.__oCropZoneTopGroupBox)
            oCropZoneLayout.addWidget(self.__oCropZoneBottomGroupBox)
            oCropZoneLayout.addWidget(self.__oCropZoneLeftGroupBox)
            oCropZoneLayout.addWidget(self.__oCropZoneRightGroupBox)
            return oCropZoneLayout

        oOutputParent = QtGui.QWidget()
        oOutputLayout = cw.AlVBoxLayout()
#        self.__oFormatComboBox = cw.AlComboBox(self.__listFormats)
#        self.__oFormatGrpLabel = cw.AlGroupLabel('Format :',
#                                            self.__oFormatComboBox)
#        self.connect(self.__oFormatComboBox,
#                     QtCore.SIGNAL('currentIndexChanged(int)'),
#                     __format_onChanged)

        oOutputLayout.addWidget(__lazyness())
        oOutputLayout.addWidget(__toFarm())
        oOutputLayout.addWidget(__camera())
        oOutputLayout.addWidget(__format())
        oOutputLayout.addWidget(__resolution())
        oOutputLayout.addLayout(__cropZone())
        oOutputParent.setLayout(oOutputLayout)
        oOutputBlock = cw.AlBloc(self,
                                 scc.OUTPUT_ICON,
                                 'Output :',
                                 oOutputParent)

        oMasterLayout.addWidget(oOutputBlock)

    def __advanced(self, oMasterLayout):
        def __ray_onClick():
            self.emit(QtCore.SIGNAL('ray_onClick'),
                      self.__oRayCheckBox.checkState())

        def __surface_onClick():
            self.emit(QtCore.SIGNAL('surface_onClick'),
                      self.__oSurfaceCheckBox.checkState())

        def __displacement_onClick():
            self.emit(QtCore.SIGNAL('displacement_onClick'),
                      self.__oDisplCheckBox.checkState())

        def __subsurface_onClick():
            self.emit(QtCore.SIGNAL('subsurface_onClick'),
                      self.__osubsurfaceCheckBox.checkState())

        def __bake():
            def __bake_onClick():
                self.emit(QtCore.SIGNAL('bake_onClick'),
                          self.__oBakeCheckBox.checkState())

            self.__oBakeCheckBox = QtGui.QCheckBox()
            self.__oBakeGroupLabel = cw.AlGroupLabel('set for Baking :',
                                                  self.__oBakeCheckBox)
            self.connect(self.__oBakeCheckBox, QtCore.SIGNAL('clicked()'),
                         __bake_onClick)
            return self.__oBakeGroupLabel

        def __traceDispl():
            def __traceDispl_onClick():
                self.emit(QtCore.SIGNAL('traceDispl_onClick'),
                          self.__oTraceDisplCheckBox.checkState())

            self.__oTraceDisplCheckBox      = QtGui.QCheckBox()
            self.__oTraceDisplGroupLabel    = cw.AlGroupLabel('Trace Displ. :',
                                                  self.__oTraceDisplCheckBox)
            self.connect(self.__oTraceDisplCheckBox, QtCore.SIGNAL('clicked()'),
                         __traceDispl_onClick)
            return self.__oTraceDisplGroupLabel

        def __illuByDefault():
            def __illuByDefault_onClick():
                self.emit(QtCore.SIGNAL('illuByDefault_onClick'),
                          self.__oIlluByDefaultCheckBox.checkState())

            self.__oIlluByDefaultCheckBox = QtGui.QCheckBox()
            self.__oIlluByDefaultGroupLabel = cw.AlGroupLabel('Illu by Default:',
                                                  self.__oIlluByDefaultCheckBox)
            self.connect(self.__oIlluByDefaultCheckBox, QtCore.SIGNAL('clicked()'),
                         __illuByDefault_onClick)
            return self.__oIlluByDefaultGroupLabel


        self.__oRayCheckBox = QtGui.QCheckBox()
        self.__oRayGroupLabel = cw.AlGroupLabel('raytracing :',
                                                    self.__oRayCheckBox)
        self.connect(self.__oRayCheckBox,QtCore.SIGNAL('clicked()'),
                         __ray_onClick)
        self.__oSurfaceCheckBox = QtGui.QCheckBox()
        self.__oSurfaceGroupLabel = cw.AlGroupLabel('no surface :',
                                             self.__oSurfaceCheckBox)
        self.connect(self.__oSurfaceCheckBox, QtCore.SIGNAL('clicked()'),
                         __surface_onClick)
        self.__oDisplCheckBox = QtGui.QCheckBox()
        self.__oDisplGroupLabel = cw.AlGroupLabel('no displacement :',
                                      self.__oDisplCheckBox)
        self.connect(self.__oDisplCheckBox,QtCore.SIGNAL('clicked()'),
                         __displacement_onClick)
        self.__osubsurfaceCheckBox = QtGui.QCheckBox()
        self.__osubsurfaceGroupLabel = cw.AlGroupLabel('no subSurface :',
                                        self.__osubsurfaceCheckBox)
        self.connect(self.__osubsurfaceCheckBox, QtCore.SIGNAL('clicked()'),
                         __subsurface_onClick)

        self.__oAdvancedParent = QtGui.QWidget()
        self.__oAdvancedLayout = cw.AlVBoxLayout()
#        self.__oAdvancedLayout.addWidget(__lazyness())
#        self.__oAdvancedLayout.addWidget(__cameraBlur())
#        self.__oAdvancedLayout.addWidget(__sampleMotionOptions())
#        self.__oAdvancedLayout.addWidget(__depthOfField())
        self.__oAdvancedLayout.addWidget(self.__oRayGroupLabel)
        self.__oAdvancedLayout.addWidget(__traceDispl())
        self.__oAdvancedLayout.addWidget(self.__oSurfaceGroupLabel)
        self.__oAdvancedLayout.addWidget(self.__oDisplGroupLabel)
        self.__oAdvancedLayout.addWidget(self.__osubsurfaceGroupLabel)
        self.__oAdvancedLayout.addWidget(__bake())
        self.__oAdvancedLayout.addWidget(__illuByDefault())
        self.__oAdvancedParent.setLayout(self.__oAdvancedLayout)
        self.__oAdvancedBloc = cw.AlBloc(self, scc.ADVANCED_ICON,
                                         'Advanced :',
                                         self.__oAdvancedParent)
        self.__oAdvancedBloc.setHidden()
        oMasterLayout.addWidget(self.__oAdvancedBloc)

    def __renderButtons(self,oMasterLayout):
        def __liquid_onClick():
            self.emit(QtCore.SIGNAL('liquid_onClick'))

        def __liquidGlobals_onClick():
            self.emit(QtCore.SIGNAL('liquidGlobals_onClick'))

        def __renderButton_onClick():
            self.emit(QtCore.SIGNAL('renderButton_onClick'),
                      self.__oToFarmBloc.isChecked())

        def __renderSelectionButton_onClick():
            self.emit(QtCore.SIGNAL('renderSelectionButton_onClick'))

        def __renderSet_onClick():
            self.emit(QtCore.SIGNAL('renderSet_onClick'))

        def __hide_onClick():
            self.emit(QtCore.SIGNAL('hide_onClick'))

        def __manageRenderSet():
            def __add2SetButton_onClick():
                    self.emit(QtCore.SIGNAL('add2SetButton_onClick'))

            def __remove2SetButton_onClick():
                    self.emit(QtCore.SIGNAL('remove2SetButton_onClick'))

            def __clearSetButton_onClick():
                    self.emit(QtCore.SIGNAL('clearSetButton_onClick'))

            sizeButton = 20
            self.__oAdd2SetButton = QtGui.QPushButton('A')
            self.__oAdd2SetButton.setMaximumWidth(sizeButton)
            self.connect(self.__oAdd2SetButton,
                             QtCore.SIGNAL('clicked()'),
                             __add2SetButton_onClick)
            self.__oRemove2SetButton = QtGui.QPushButton('R')
            self.__oRemove2SetButton.setMaximumWidth(sizeButton)
            self.connect(self.__oRemove2SetButton,
                             QtCore.SIGNAL('clicked()'),
                             __remove2SetButton_onClick)
            self.__oClearSetButton = QtGui.QPushButton('C')
            self.__oClearSetButton.setMaximumWidth(sizeButton)
            self.connect(self.__oClearSetButton,
                             QtCore.SIGNAL('clicked()'),
                             __clearSetButton_onClick)

            oSetManagerLayout = cw.AlHBoxLayout()
            self.__setContentMargins0(oSetManagerLayout)
            oSetManagerLayout.addWidget(self.__oAdd2SetButton)
            oSetManagerLayout.addWidget(self.__oRemove2SetButton)
            oSetManagerLayout.addWidget(self.__oClearSetButton)
            return oSetManagerLayout


        self.__oLiquidButton = QtGui.QPushButton('set to\nLiquid')
        self.__oLiquidButton.setMaximumWidth(50)
        self.connect(self.__oLiquidButton, QtCore.SIGNAL('clicked()'),
                         __liquid_onClick)

        self.__oRenderButton = QtGui.QPushButton('R E N D E R\n')
        sColor ="QWidget { background-color: %s }" %scc.GREEN_COLOR.name()
        self.__oRenderButton.setStyleSheet(sColor)
        self.connect(self.__oRenderButton, QtCore.SIGNAL('clicked()'),
                         __renderButton_onClick)

        self.__oLiquidGlobalsButton = QtGui.QPushButton('Render\nSettings')
        self.__oLiquidGlobalsButton.setMaximumWidth(50)
        self.connect(self.__oLiquidGlobalsButton, QtCore.SIGNAL('clicked()'),
                         __liquidGlobals_onClick)

        self.__oRenderSelectionButton = QtGui.QPushButton('Render Selection')
        sColor = "QWidget { background-color: %s }" %scc.YELLOW_COLOR.name()
        self.__oRenderSelectionButton.setStyleSheet(sColor)
        self.connect(self.__oRenderSelectionButton, QtCore.SIGNAL('clicked()'),
                         __renderSelectionButton_onClick)

        self.__oRenderSetButton = QtGui.QPushButton('Render the Set')
        sColor = "QWidget { background-color: %s }" %scc.BLUE_COLOR.name()
        self.__oRenderSetButton.setStyleSheet(sColor)
        self.connect(self.__oRenderSetButton, QtCore.SIGNAL('clicked()'),
                         __renderSet_onClick)

        self.__oHideButton = QtGui.QPushButton()
        self.__oHideButton.setMaximumHeight(10)
        self.connect(self.__oHideButton, QtCore.SIGNAL('clicked()'),
                             __hide_onClick)

        oRenderGlobalLayout = QtGui.QVBoxLayout()
        oRenderGlobalLayout.setContentsMargins(0,0,0,0)
        oRenderLayout = QtGui.QHBoxLayout()
        oRenderLayout.setContentsMargins(0,0,0,0)
        oRenderLayout.addWidget(self.__oLiquidButton)
        oRenderLayout.addWidget(self.__oRenderButton)
        oRenderLayout.addWidget(self.__oLiquidGlobalsButton)
        oRenderSelectionLayout = QtGui.QHBoxLayout()
        oRenderSelectionLayout.setContentsMargins(0,0,0,0)
        oRenderSelectionLayout.addWidget(self.__oRenderSetButton)
        oRenderSelectionLayout.addLayout(__manageRenderSet())
        oRenderSelectionLayout.addStretch(1)
        oRenderSelectionLayout.addWidget(self.__oRenderSelectionButton)
        oRenderGlobalLayout.addLayout(oRenderLayout)
        oRenderGlobalLayout.addLayout(oRenderSelectionLayout)
        oRenderGlobalLayout.addWidget(self.__oHideButton)
        oMasterLayout.addLayout(oRenderGlobalLayout)

    def __printMode(self):
        def __printMode_onClick():
            self.emit(QtCore.SIGNAL('printMode_onClick'),
                      self.__oPrintMode.checkState())

        self.__oPrintMode = QtGui.QCheckBox('Print Mode')
        self.connect(self.__oPrintMode,QtCore.SIGNAL('clicked()'),
                     __printMode_onClick)
        return self.__oPrintMode

    def __lineEditActions(self, oIn, func):
        self.connect(oIn, QtCore.SIGNAL('returnPressed()'), func)
        self.connect(oIn, QtCore.SIGNAL('editingFinished()'), func)

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

    def __setContentMargins10(self, oWidget):
        """
        Method to set the contentMargin to 0,10,0,0
        @type oWidget: object
        @param oWidget: Qt Widget
        @rtype: object
        @return: Qt Widget with contentMargins set to (0,10,0,0)
        """
        oWidget.setContentsMargins(0,10,0,0)
        return oWidget
# Ni!

