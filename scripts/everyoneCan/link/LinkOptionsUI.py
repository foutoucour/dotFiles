# -*- coding: utf-8 -*-

## @todo : search ## todo to find methods to finish 

from PyQt4 import QtGui
from PyQt4 import QtCore

from everyoneCan import UIs
reload(UIs)
from everyoneCan import CustomWidgets as cw
reload(cw)
from everyoneCan.light import lightOptions
reload(lightOptions)

from everyoneCan import SharedConstants
reload(SharedConstants)
scc                         = SharedConstants.Constants()

class Gui(QtGui.QMainWindow):
    """
    Graphic Interface of lightOptions tool
    Discuss with control through an observer
    """
    ## todo
    # all color sets should like render color
    __SET_COLOR         = [163,190,218]
    __GEO_COLOR         = [142,208,132]
    __LIGHT_COLOR       = [247,244,229]
    __SHADOW_COLOR      = [139,128,174]
    __BLOCKER_COLOR     = [142,208,132]
    
    __RENDER_COLOR          = QtGui.QColor(239,228,174)
    
    def setObserver(self, obj):
        """
        The observer will be the bridge between the controlor and the GUI
        This way, the GUI doesn't know the controlor
        
        @type object: object
        @param object: observer
        """
        ## todo
        # obsolete but remove it will broke all signals
        # dunno why.
        self.__oObserver = obj

    def setLightsViewName(self,string):
        """
        Setting the title of the listview containing lights.
        
        @type string    : string
        @param string   : name of the listview
        """
        self.__sLightsViewName = string
        
    def setBlockersViewName(self,string):
        """
        Setting the title of the listview containing blockers.
        
        @type string    : string
        @param string   : name of the listview
        """
        self.__sBlockersViewName = string
        
    def setSetsViewName(self,string):
        """
        Setting the title of the listview containing sets.
        
        @type string    : string
        @param string   : name of the listview
        """
        self.__sSetsViewName = string
    
    def setShadowCamerasViewName(self,string):
        """
        Setting the title of the listview containing shadow cameras.
        
        @type string    : string
        @param string   : name of the listview
        """
        self.__sShadowCamerasViewName = string
    
    def setShadowMapsViewName(self,string):
        """
        Setting the title of the listview containing shadow maps.
        
        @type string    : string
        @param string   : name of the listview
        """
        self.__sShadowMapsViewName = string
        
    def setPicturesViewName(self,string):
        """
        Setting the title of the listview containing pictures.
        
        @type string    : string
        @param string   : name of the listview
        """
        self.__sPicturesViewName = string
        
    def setGeometriesViewName(self,string):
        """
        Setting the title of the listview containing geometries.
        
        @type string    : string
        @param string   : name of the listview
        """
        self.__sGeometriesViewName = string

    def clearViewSelection(self, oObject):
        """
        Unselect elements
        
        @type oObject   : QListView
        @param oObject  : list view which element needs to be unselected
        """
        
        oObject.oList.clearSelection()       
        
    def __delightEveryThing(self):
        """
        Set the background color as the neutral color
        to all elements in all list views.
        """
        ## todo
        # I suspect that to be obsolete as I never append something
        # to self.__listListViews.
        for oView in self.__listListViews:
            print oView.getAllItems()
           
    def main(self):
        """
        Creation of widgets
        """
        def __contextMenu(oObject):
            """
            Signal emmitted when a contextMenu is called.
            
            @type oObject   : QObject
            @param oObject  : Emitting object
            """
            self.emit(QtCore.SIGNAL('oGui_list_contextMenu'), oObject)
        
        def __list_link(oObject, oItem, bool):
            """
            Signal emmitted when an action is called.
            
            @type oObject   : QObject
            @param oObject  : emmitting object 
            
            @type oItem     : QAction
            @param oItem    : called action
            
            @type bool      : boolean
            @param bool     : mode of the action
            """
            self.emit(QtCore.SIGNAL('oGui_list_link'), 
                      oObject, oItem, bool)
        
            
        if self.__boolSelfLaunch == 1:
            QtGui.QMainWindow.__init__(self)
            oIcon = QtGui.QIcon('%s/LinkOptions.jpg' %scc.ICON_PATH)
            self.setWindowIcon(oIcon)
        else :
            QtGui.QWidget.__init__(self)
            
        oScreen                 = QtGui.QDesktopWidget().screenGeometry()
        
        # size of the application
        self.__oWidth           = oScreen.width()*90/100
        self.__oHeight          = oScreen.height()*90/100
        self.resize(self.__oWidth,self.__oHeight)
        
        ## todo
        # obsolete I think
        self.__listListViews    = []
        
        # creation of lists and their signals
        self.oLights          = self.__lights()
        self.listViews.append(self.oLights)
        self.connect(self.oLights, QtCore.SIGNAL('list_changed'),
                        self.__selection)
        self.connect(self.oLights, QtCore.SIGNAL('list_contextMenu'),
                        __contextMenu)
        self.connect(self.oLights, QtCore.SIGNAL('oBlock_list_link'),
                        __list_link)
        
        self.oBlockers        = self.__blockers()
        self.listViews.append(self.oBlockers)
        self.connect(self.oBlockers, QtCore.SIGNAL('list_changed'),
                        self.__selection)
        self.connect(self.oBlockers, QtCore.SIGNAL('list_contextMenu'),
                        __contextMenu)
        self.connect(self.oBlockers, QtCore.SIGNAL('oBlock_list_link'),
                        __list_link)
        
        self.oShadowCameras   = self.__shadowCameras()
        self.listViews.append(self.oShadowCameras)
        self.connect(self.oShadowCameras, QtCore.SIGNAL('list_changed'),
                        self.__selection)
        self.connect(self.oShadowCameras, QtCore.SIGNAL('list_contextMenu'),
                        __contextMenu)
        self.connect(self.oShadowCameras, QtCore.SIGNAL('oBlock_list_link'),
                        __list_link)
                
        self.oPictures      = self.__pictures()
        self.listViews.append(self.oPictures)
        self.connect(self.oPictures, QtCore.SIGNAL('list_changed'),
                        self.__selection)
        self.connect(self.oPictures, QtCore.SIGNAL('list_contextMenu'),
                        __contextMenu)
        self.connect(self.oPictures, QtCore.SIGNAL('oBlock_list_link'),
                        __list_link)
        
        self.oSets            = self.__sets()
        self.listViews.append(self.oSets)
        self.connect(self.oSets, QtCore.SIGNAL('list_changed'),
                        self.__selection)
        self.connect(self.oSets, QtCore.SIGNAL('list_contextMenu'),
                        __contextMenu)
        self.connect(self.oSets, QtCore.SIGNAL('oBlock_list_link'),
                        __list_link)
        
        self.oGeometries      = self.__geometries()
        self.listViews.append(self.oGeometries)
        self.connect(self.oGeometries, QtCore.SIGNAL('list_changed'),
                        self.__selection)
        self.connect(self.oGeometries, QtCore.SIGNAL('list_contextMenu'),
                        __contextMenu)
        self.connect(self.oGeometries, QtCore.SIGNAL('oBlock_list_link'),
                        __list_link)
        
        # creation of layouts
        oCentralWidget          = QtGui.QWidget()
        oMainLayout             = QtGui.QHBoxLayout(oCentralWidget)
        oMainLayout.setContentsMargins(0,0,0,0)        
        
        oListLayout             = QtGui.QHBoxLayout()                
        oSetLayout              = QtGui.QVBoxLayout()
        oSetLayout.setContentsMargins(0,0,0,0)
        oSetLayout.addWidget(self.oSets)
        
        oListLayout.addWidget(self.oLights)
        oListLayout.addLayout(oSetLayout)
        oListLayout.addWidget(self.oGeometries)
        oListLayout.addWidget(self.oBlockers)

        oListLayout.addWidget(self.oShadowCameras)
        oListLayout.addWidget(self.oPictures)

        oListLayout.setStretchFactor(self.oLights,3)
        oListLayout.setStretchFactor(oSetLayout,2)
        oListLayout.setStretchFactor(self.oGeometries,2)
        oListLayout.setStretchFactor(self.oBlockers,2)
#        oListLayout.setStretchFactor(self.oShadowMaps,2)
        oListLayout.setStretchFactor(self.oShadowCameras,2)
        oListLayout.setStretchFactor(self.oPictures,2)
#        oListLayout.setStretchFactor(oShadowLayout,2)
        
        
        # button to refresh the GUI
        oRefresh                = QtGui.QPushButton('Refresh')
        sColor ="QWidget { background-color: %s }" %self.__RENDER_COLOR.name()
        oRefresh.setStyleSheet(sColor)
        self.connect(oRefresh, 
                    QtCore.SIGNAL('clicked()'), 
                    self.__refresh)
        
        
        self.__oWidgetLayoutParent     = QtGui.QWidget()
        oWidgetLayout           = QtGui.QVBoxLayout(self.__oWidgetLayoutParent)
        oWidgetLayout.addWidget(oRefresh)
        oWidgetLayout.addLayout(oListLayout)
        self.__oWidgetLayoutParent.setLayout(oWidgetLayout)
        
        oLightOptionsLayout    = QtGui.QVBoxLayout()
        oLightOptionsLayout.setContentsMargins(0,0,0,0)
        oLightOptionsLayout.addWidget(self.oLightOptions)
        oLightOptionsLayout.addWidget(self.__UIs())
        oLightOptionsLayout.addStretch(1)
#        oMainLayout.addWidget(oHideListButton)
        oMainLayout.addLayout(oLightOptionsLayout)
        oMainLayout.addWidget(self.__oWidgetLayoutParent)
        oMainLayout.setStretchFactor(oLightOptionsLayout,0)
        oMainLayout.setStretchFactor(self.__oWidgetLayoutParent,10)
        # if the tool is launched as standalone
        # we need to set its centralWidget
        if self.__boolSelfLaunch == 1:
            self.setCentralWidget(oCentralWidget)
        
        # Setting of links.
        # Direct links are used to know with which other lists
        # a list can act.
        self.__setDirectLinks()
    
    def __UIs(self):
        """
        Methods creating the UI bloc
        @type oMasterLayout: Qt object
        @param oMasterLayout: Qt Layout
        """             
        oUIGrpBox = QtGui.QGroupBox(scc.UI_GROUPBOX_NAME)
        oUILayout = QtGui.QVBoxLayout(oUIGrpBox)
        oUILayout.setContentsMargins(0,0,0,0)
        oUILayout.addWidget(UIs.AllOthersUIWidget(__name__,'V'))
        return oUIGrpBox
    
    def __init__(self, boolSelfLaunch):
        """
        @type boolSelfLaunch: int boolean
        @param boolSelfLaunch: indicate if the tool is launched as 
                standalone (1) or not (0)
        """
        self.__boolWidgetHide   = 0
        self.__boolSelfLaunch   = boolSelfLaunch
        # List with all QlistViews
        self.listViews          = []
        self.oLightOptions      = lightOptions.LightingOptionsLauncher(0)
    
    def __setDirectLinks(self):
        """
        Setting of Direct links.
        Direct links are used to know with which other lists
        a list can act.
        """
        # blocker Block
        self.oBlockers.setDirectLink(self.oLights.title)
        # light Block
        self.oLights.setDirectLink(self.oBlockers.title)
        self.oLights.setDirectLink(self.oSets.title)
        self.oLights.setDirectLink(self.oShadowCameras.title)
        self.oLights.setDirectLink(self.oPictures.title)
        # set Block
        self.oSets.setDirectLink(self.oLights.title)
        self.oSets.setDirectLink(self.oGeometries.title)
        self.oSets.setDirectLink(self.oShadowCameras.title)
        # geometry Block
        self.oGeometries.setDirectLink(self.oSets.title)
        # shadow camera Block
        self.oShadowCameras.setDirectLink(self.oLights.title)
#        self.oShadowCameras.setDirectLink(self.oShadowMaps.title)
        self.oShadowCameras.setDirectLink(self.oSets.title)
        # shadow map Block
#        self.oShadowMaps.setDirectLink(self.oLights.title)
        # picture Bloc
        self.oPictures.setDirectLink(self.oLights.title)
    
    
    def __lights(self, list=[]):
        """
        Creation of the list for Lights
        
        @type list  : list of string
        @param list : element to add to the list
        """
        oListView = self.__LinkBloc(self.__sLightsViewName, list, self)
        oListView.setColor(self.__LIGHT_COLOR[0],self.__LIGHT_COLOR[1],
                                                    self.__LIGHT_COLOR[2])
        return oListView
    
    def __sets(self, list=[]):
        """
        Creation of the list for sets
        
        @type list  : list of string
        @param list : element to add to the list
        """
        
        def __createSet():
            self.emit(QtCore.SIGNAL('listSet_contextMenu_createSet'))
            
        self.__oListView = self.__LinkBloc(self.__sSetsViewName, list, self)
        self.__oListView.setColor(self.__SET_COLOR[0],
                                  self.__SET_COLOR[1],
                                  self.__SET_COLOR[2])
        oCreateAction     = QtGui.QAction('Create Set', self)
        self.connect(oCreateAction, 
                     QtCore.SIGNAL('triggered()'), 
                     __createSet)
        self.__oListView.oList.addAction(oCreateAction)
        self.__oListView.setIconSize(35)
        return self.__oListView
    
    def __blockers(self, list=[]):
        """
        Creation of the list for blockers
        
        @type list  : list of string
        @param list : element to add to the list
        """
        oListView = self.__LinkBloc(self.__sBlockersViewName, list, self)
        oListView.setColor(self.__BLOCKER_COLOR[0],self.__BLOCKER_COLOR[1],
                                                    self.__BLOCKER_COLOR[2])
        return oListView
    
    def __geometries(self, list=[]):
        """
        Creation of the list for geometries
        
        @type list  : list of string
        @param list : element to add to the list
        """
        oListView = self.__LinkBloc(self.__sGeometriesViewName, list, self)
        oListView.setColor(self.__GEO_COLOR[0],self.__GEO_COLOR[1],
                                                    self.__GEO_COLOR[2])
        return oListView

    def __shadowCameras(self, list=[]):
        """
        Creation of the list for shadow cameras
        
        @type list  : list of string
        @param list : element to add to the list
        """
        oListView = self.__LinkBloc(self.__sShadowCamerasViewName, list, self)
        oListView.setColor(self.__SHADOW_COLOR[0],self.__SHADOW_COLOR[1],
                                                    self.__SHADOW_COLOR[2])
        return oListView
    
    def __pictures(self, list=[]):
        """
        Creation of the list for pictures
        
        @type list  : list of string
        @param list : element to add to the list
        """
        oListView = self.__LinkBloc(self.__sPicturesViewName, list, self)
        oListView.setEnabled(0)
        oListView.setColor(self.__BLOCKER_COLOR[0],self.__BLOCKER_COLOR[1],
                                                    self.__BLOCKER_COLOR[2])
        return oListView

    def __selection(self, oObject):
        """
        Set the background as neutral for everything
        and emit the "oGui_selection" signal
        
        @type oObject   : QObject
        @param oObject  : object emitting
        """
        # set the background as neutral for everything
        for element in self.listViews:
            element.delightItems()
        self.emit(QtCore.SIGNAL('oGui_selection'), oObject)
    
    def __refresh(self):
        """
        Emitting "oGui_refresh" signal
        """
        self.emit(QtCore.SIGNAL('oGui_refresh'))
        
    class __LinkBloc(cw.AlItemView):
        """
        Customing the AlItemView for this application.
        Adding direct links methods/property and connection Methods/property
        """
        
        __MAIN_ACTION_TITLE = 'link to selection'
        
        def __init__(self, title, list, parent):
            """
            @type title: string
            @param title: name of the widget
            @type list: list of string
            @param list: names of elements to add
            @type parent: object
            @param parent: parent of the widget
            """
            self.listDirectLinks = []
            self.listConnections = []
            cw.AlItemView.__init__(self, title, list, parent)
            self.oMainAction     = QtGui.QAction(self.__MAIN_ACTION_TITLE,
                                                    self)
            self.oMainAction.setVisible(0)
            
            self.connect(self.oMainAction, 
                         QtCore.SIGNAL('triggered()'), 
                         self.__unlink)
            self.oList.addAction(self.oMainAction)
            self.oList.addSeparator()
            
        def __unlink(self):
            """
            Emitting "list_contextMenu" signal
            """
            self.emit(QtCore.SIGNAL('list_contextMenu'),
                      self)
        
        def setDirectLink(self, sName):
            """
            Append a string to the list
            @type sName: string
            @param sName: name of a block
            """
            self.listDirectLinks.append(sName)
        
        def removeDirectLink(self, sName):
            """
            remove the string from the list
            @type sName: string
            @param sName: name of a block
            """
            self.listDirectLinks.remove(sName)
        
        def setConnections(self, list):
            """
            Setting the list of connections
            
            @type list  : list of string
            @param list : name of connections
            """
            self.listConnections = list
        
        def contextMenuAction(self, oObject, oItem):
            """
            Emitting "oBlock_list_link" signal
            
            @type oObject   : QObject
            @param oObject  : Emitting object
            
            @type oItem     : QAction
            @param oItem    : Called action
            """
            self.emit(QtCore.SIGNAL('oBlock_list_link'),
                      oObject, oItem, self.__testConnection(oItem) )
                
        def __testConnection(self, oItem):
            """
            @type oItem: QItem
            
            @rtype: integer
            @return: 0 if we need to unlink, 1 to link
            """
            for element in self.listConnections:
                if oItem.text() == element[1]:
                    return 0   
            return 1

# Ni !