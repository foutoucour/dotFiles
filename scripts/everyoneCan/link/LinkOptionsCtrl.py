# -*- coding: utf-8 -*-

## @todo : search ## todo to find methods to finish


import maya.cmds as cmds

from PyQt4 import QtCore

# Class to storing different values of alType attribut
# also paths to icons or text of tooltips etc.
from everyoneCan import SharedConstants
tl                          = SharedConstants.TypeLister()

# import of QObject for signals method
class Control(QtCore.QObject):
    """control of the linkOptions Application"""
    #==========================================================================
    # constants
    #==========================================================================
    __DEBUG                                 = 0
    
    # Name of views
    __LIGHTS_VIEW                           = 'Lights'
    __LIGHTSETS_VIEW                        = 'LiquidSets'
    __BLOCKERS_VIEW                         = 'Blockers'
    __SHADOWCAMERAS_VIEW                    = 'ShadowCameras'
    __SHADOWMAPS_VIEW                       = 'ShadowMaps'
    __PICTURES_VIEW                         = 'Pictures'
    __GEOMETRIES_VIEW                       = 'Geometries'
    
    # number of blocker slot in shaders
    __BLOCKER_SHADER_SLOT                   = 4


    def __init__(self, oGui, oModel):
        self.__debug("__init__")
        """
        Setting of the link with Gui and the model
        
        @type oGui  : object
        @param oGui : Interface part of this linkOptions Application
        """
        
        self.__oModel           = oModel
        self.__oGui             = oGui
        
        ## todo
        # The observer is obsolete and is doing nothing
        # but if I remove it, signals are broken.
        self.__oGui.setObserver(GuiObserver(self))
        
        # linking the names set in control to the model and the GUI
        self.__oModel.setLightsViewName(self.__LIGHTS_VIEW )
        self.__oModel.setBlockersViewName(self.__BLOCKERS_VIEW)
        self.__oModel.setSetsViewName(self.__LIGHTSETS_VIEW)
        self.__oModel.setShadowCamerasViewName(self.__SHADOWCAMERAS_VIEW)
        self.__oModel.setShadowMapsViewName(self.__SHADOWMAPS_VIEW)
        self.__oModel.setPicturesViewName(self.__PICTURES_VIEW)
        self.__oModel.setGeometriesViewName(self.__GEOMETRIES_VIEW)
        self.__oGui.setLightsViewName(self.__LIGHTS_VIEW )
        self.__oGui.setBlockersViewName(self.__BLOCKERS_VIEW)
        self.__oGui.setSetsViewName(self.__LIGHTSETS_VIEW)
        self.__oGui.setShadowCamerasViewName(self.__SHADOWCAMERAS_VIEW)
        self.__oGui.setShadowMapsViewName(self.__SHADOWMAPS_VIEW)
        self.__oGui.setPicturesViewName(self.__PICTURES_VIEW)
        self.__oGui.setGeometriesViewName(self.__GEOMETRIES_VIEW)
        
        # Creation of the GUI.
        self.__oGui.main()
        
        # Initiation of signals.
        self.__signals()
        
        # Send name of listviews.
        self.__oModel.setListView(self.__oGui.listViews)
        
        # Fill listviews.
        self.__setLists()
    
    def __setLists(self):
        self.__debug("__setLists")
        """
        Fill view lists.
        """
        
        # listing cameras.
        self.__oModel.getCameras()
        
        # listing assemblies (lights and blockers).
        self.__oModel.getAssemblies()
        
        # different listing of objects for each listviews.
        self.__oGui.oLights.setList(self.__oModel.lights())
        self.__oGui.oBlockers.setList(self.__oModel.blockers())
        self.__oGui.oShadowCameras.setList(self.__oModel.shadowCameras())
        self.__oGui.oPictures.setList(self.__oModel.pictures())
        self.__oGui.oSets.setList(self.__oModel.sets())
        self.__oGui.oGeometries.setList(self.__oModel.geometries())
        
        
    def __fromSelection(self, oObject):
        self.__debug("__fromSelection")
        """
        Called when a selection is done byt the user
        
        
        @type oObject   : object(s)
        @param oObject  : object(s) selected by the user in the GUI
        """
        ## todo
        # this function is a mess and should reworked
        
        listUncommon = []
        
        self.__oCurrentObject = oObject # we keep this object as persistant
                                        # we will need it for contextMenu
                                        
        # unlight other listviews.
        self.__setOtherViews(self.__oCurrentObject)
        
        # setting mode of context menus of all listviews. 
        self.__setContextMenus(self.__oCurrentObject)
        listNames = []
        
        for element in oObject.oList.selectedItems():
            listNames.append(str(element.text()))
        
        self.__oModel.select(listNames)
        
        # actions done is the selection is coming from
        # the listviews containing shadow cameras.
        if self.__oCurrentObject.title == self.__SHADOWCAMERAS_VIEW:
            listShapes = []
            for element in listNames:
                listShapes.append(cmds.listRelatives(element)[0])
            listNames = listShapes
        
        #======================================================================
        # Blockers/ShadowCameras    
        #======================================================================
        # actions done is the selection is coming from
        # the listviews containing blocker or shadow cameras.
        if self.__oCurrentObject.title == self.__BLOCKERS_VIEW or \
            self.__oCurrentObject.title == self.__SHADOWCAMERAS_VIEW:
            list = []
            for element in cmds.listConnections(listNames):
                try :
                    if cmds.getAttr('%s.alType' %element) == tl.LIQUID_LIGHT_SHADER:
                        if not element in list:
                            listNames.append(element)
                except :
                    pass
        listConns = self.__oModel.findConnections(listNames, 
                                                  self.__oCurrentObject.title)
        
        #======================================================================
        # Lights
        #======================================================================
        # actions done is the selection is coming from
        # the listviews containing lights.
        if self.__oCurrentObject.title == self.__LIGHTS_VIEW :
            listShapes = []
            listShaders = []
            for element in listNames :
                try :
                    listShapes.append(cmds.listRelatives(element)[0])
                except :
                    pass
                for sConnection in cmds.listConnections(element):
                    if self.__oModel.getType(sConnection) == tl.LIQUID_LIGHT_SHADER:
                        sShader = sConnection
                        if not sShader in listShaders:
                            listShaders.append(sShader)
                            a = 0
                            while a < self.__BLOCKER_SHADER_SLOT:
                                try :
                                    sBlockerShape = cmds.getAttr('%s.Blocker_CoordSys[%d]' %(sShader,a))
                                    sBlocker = cmds.listRelatives(sBlockerShape, p=1)[0]
                                    listUncommon.append([self.__BLOCKERS_VIEW,
                                                         sBlocker])
                                except :
                                    pass
                                a += 1
                            for sConn in cmds.listConnections(sShader):
                                try :
                                    alType = cmds.getAttr('%s.alType' %sConn)
                                    if alType == tl.SHADOW_CAMERA:
                                        if not sConn in listUncommon:
                                            listUncommon.append([self.__SHADOWCAMERAS_VIEW,
                                                                 sConn])
                                except:
                                    pass
            listShapesConns = self.__oModel.findConnections(listShapes,
                                                            self.__oCurrentObject.title)
            for element in listShapesConns:
                listConns.append(element)
        
        
        listBoth = listConns
        if len(listUncommon) > 0 :
            listBoth += listUncommon
        listPurge = []
        for element in listBoth:
            if not element in listPurge:
                listPurge.append(element)
        listBoth = listPurge
        
        self.__enlight(listBoth, 1)
        self.__oCurrentObject.setConnections(listBoth)
        
        listSecondGenerationConn = [] 
        for Conns in listConns:
            listSecondGenerationConn.append(Conns[1])
            
        listSecondGenerationItems = self.__oModel.findConnections(
                                                    listSecondGenerationConn,
                                                    self.__oCurrentObject.title)
        listWantedSecondGenerationItems = []
        
        for items in listSecondGenerationItems :
            if not items[0] == self.__oCurrentObject.title and not items in listConns:
                if not items in listWantedSecondGenerationItems :
                    listWantedSecondGenerationItems.append(items)
        
        self.__enlight(listWantedSecondGenerationItems, 2)
    
    def __fromContextMenu(self, oObject):
        self.__debug("__fromContextMenu")
        """
        Initiating an action coming from a context menu.
        
        @type oObject   : object
        @param oObject  : Qlistview
        """
        
        for element in oObject.oList.selectedItems():
            # listDirectLinks contains the list of blocs with which 
            # connections can be done
            if self.__oCurrentObject.title in oObject.listDirectLinks:
                self.__oCurrentObject.contextMenuAction(oObject, element)
        self.__fromSelection(self.__oCurrentObject)
    
    def __setOtherViews(self, oCurrentListView):
        self.__debug("__setOtherViews")
        """
        Unselection elements of other listview
        
        @type oCurrentListView  : object
        @param oCurrentListView : QlistView
        """
        
        for element in self.__oGui.listViews:
            element.delightItems()
            if not element.title == oCurrentListView.title:
                self.__oGui.clearViewSelection(element)

    def __enlight(self, list, generation):
        self.__debug("__enlight")
        """
        Enlighting  element of listviews.
        
        @type list      : list of string
        @param list     : list of connection of the selection
        
        @type generation    : integer.
        @param generation   : level of generation of the connection
        """
        
        for conns in list:
            for element in self.__oGui.listViews:
                if conns[0] == element.title:
                    if not generation == 1 :
                        if not element.title in self.__oCurrentObject.listDirectLinks:
                            element.enlightItem(conns[1], generation)
                    else :
                        element.enlightItem(conns[1], generation)
    
    def __setContextMenus(self, oObject):
        self.__debug("__setContextMenus")
        """
        Setting context menus of every listviews depending of
        the current listview.
        
        @type oObject   : QObject
        @param oObject  : object selected by the user in the GUI
        """
        
        for element in self.__oGui.listViews:
            if element.title in self.__oCurrentObject.listDirectLinks:
                element.oMainAction.setVisible(1)
            else :
                element.oMainAction.setVisible(0)
    
    def __ContextMenuAction(self, oObject, oItem, bool):
        self.__debug("__ContextMenuAction")
        """
        Setting of different actions.
        
        @type oObject   : object(s)
        @param oObject  : object(s) selected by the user in the GUI
        
        @type oItem     : object
        @param oItem    : second selection
        
        @type bool  : boolean
        @param bool : mode (add or remove)
        """
        #======================================================================
        # Geometry
        #======================================================================
        if self.__oCurrentObject.title == self.__GEOMETRIES_VIEW:
            self.__oModel.actionGeo2Set(
                                self.__oCurrentObject.oList.selectedItems(),
                                oItem, 
                                bool)
        #======================================================================
        # Set
        #======================================================================
        if self.__oCurrentObject.title == self.__LIGHTSETS_VIEW:
            if oObject.title == self.__GEOMETRIES_VIEW:
               self.__oModel.actionSet2Geo(
                                self.__oCurrentObject.oList.selectedItems(),
                                oItem, 
                                bool) 
            if oObject.title == self.__LIGHTS_VIEW :
                self.__oModel.actionSet2Light(
                                self.__oCurrentObject.oList.selectedItems(),
                                oItem, 
                                bool)
            if oObject.title == self.__SHADOWCAMERAS_VIEW :
                self.__oModel.actionSet2ShadowCam(
                                self.__oCurrentObject.oList.selectedItems(),
                                oItem)
                 
        #======================================================================
        # Light
        #======================================================================
        if self.__oCurrentObject.title == self.__LIGHTS_VIEW :
            if oObject.title == self.__LIGHTSETS_VIEW:
                self.__oModel.actionLight2Set(
                                self.__oCurrentObject.oList.selectedItems(),
                                oItem, 
                                bool)
                
            if oObject.title == self.__BLOCKERS_VIEW:
                self.__oModel.actionLight2Blocker(
                                self.__oCurrentObject.oList.selectedItems(),
                                oItem, 
                                bool)
            if oObject.title == self.__SHADOWCAMERAS_VIEW:
                self.__oModel.actionLight2ShadowCamera(
                                self.__oCurrentObject.oList.selectedItems(),
                                oItem, 
                                bool)
        #======================================================================
        # Blocker  
        #======================================================================
        if self.__oCurrentObject.title == self.__BLOCKERS_VIEW:
            self.__oModel.actionBlocker2Light(
                                self.__oCurrentObject.oList.selectedItems(),
                                oItem, 
                                bool)
        #======================================================================
        # Picture  
        #======================================================================
        if self.__oCurrentObject.title == self.__PICTURES_VIEW:
            self.__oModel.actionPicture2Light(
                                self.__oCurrentObject.oList.selectedItems(),
                                oItem, 
                                bool)
        #======================================================================
        # ShadowCameras
        #======================================================================
        if self.__oCurrentObject.title == self.__SHADOWCAMERAS_VIEW:
            if oObject.title == self.__LIGHTSETS_VIEW:
                self.__oModel.actionShadowCam2Set(
                                self.__oCurrentObject.oList.selectedItems(),
                                oItem)
            if oObject.title == self.__LIGHTS_VIEW:
                self.__oModel.actionShadowCam2Light(
                                self.__oCurrentObject.oList.selectedItems(),
                                oItem,
                                bool)
        
    def __clearAndSetSetList(self):
        self.__debug("__clearAndSetSetList")
        """
        Clear set listview and refill it.
        """
        self.__oGui.oSets.oList.clear()
        self.__oGui.oSets.setList(self.__oModel.sets())
        
    def __clearLists(self):
        self.__debug("__clearLists")
        """
        Clear listviews.
        """
        for element in self.__oGui.listViews:
            element.oList.clear()
        
    def __refreshUI(self):
        self.__debug("__refreshUI")
        """
        Clear listviews and refill them
        """
        
        self.__clearLists()
        self.__setLists()  
          
    def __createSet(self):
        self.__debug("__createSet")
        """
        Creation of a new maya set
        """
        
        self.__oModel.createSet()
        self.__refreshUI()
               
    def __signals(self):
        self.__debug("__signals")
        """
        Setting of differents signals
        """
        self.connect(self.__oGui,
                     QtCore.SIGNAL('oGui_selection'),
                     self.__fromSelection)
        self.connect(self.__oGui,
                     QtCore.SIGNAL('oGui_list_contextMenu'),
                     self.__fromContextMenu)
        self.connect(self.__oGui,
                     QtCore.SIGNAL('oGui_list_link'),
                     self.__ContextMenuAction)
        self.connect(self.__oGui.oLightOptions.oGui,
                     QtCore.SIGNAL('LightOptionsUI_signal'),
                     self.__refreshUI)
        self.connect(self.__oGui.oLightOptions.oModel,
                     QtCore.SIGNAL('LightOptionsModel_Signal'),
                     self.__refreshUI)
        self.connect(self.__oGui,
                     QtCore.SIGNAL('oGui_refresh'),
                     self.__refreshUI)
        self.connect(self.__oGui,
                     QtCore.SIGNAL('listSet_contextMenu_createSet'),
                     self.__createSet)
    
    def __debug(self, string):
        """
        function to track the use of function of the class
        
        @type string    : string
        @param string   : name of the function to track
        """
        
        if self.__DEBUG == 1:
            print "Ctrl.%s()" %string

# Ni !

class GuiObserver:
    ## todo
    # this is obsolete but if it is revomed, signals are all broken.
    """Handler of GlobalOptions UI
    It makes the bridge between the UI and the control.
    This way, the UI doesn't need to know the control
    """
    def __init__(self, obj):
        """
        @type object: object
        @param object: lightOptions control
        """
        self.__oCtrl = obj

# Ni !