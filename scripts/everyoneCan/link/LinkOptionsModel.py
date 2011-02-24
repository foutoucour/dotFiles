# -*- coding: utf-8 -*-

## @todo : search ## todo to find methods to finish 


import maya.cmds as cmds
import maya.mel as mel

from PyQt4 import QtCore
# Once again QtGui is used for a QDialog.
# the Qdialog should be in the UI.
from PyQt4 import QtGui

# Class to manage links between lights and blockers.
from everyoneCan import multiLinkBlocker

# Class to storing different values of alType attribut
# also paths to icons or text of tooltips etc.
from everyoneCan import SharedConstants
reload(SharedConstants)

scc                         = SharedConstants.Constants()
tl                          = SharedConstants.TypeLister()

class Model:
    #==========================================================================
    # constants
    #==========================================================================
    __DEBUG = 0
    __LIST_SHADOW_CAMERA_ATTR = ['Switch',
                                 'Density',
                                 'Blur',
                                 'Samples',
                                 'Bias',
                                 'File']
    def __init__(self, oGui):
        self.__debug("__init__")
        self.__listLights       = []
        self.__listBlockers     = []
        self.__oGui             = oGui
        self.__oBlockerLinker   = multiLinkBlocker.Linker()
        self.__oBlockerMethods  = multiLinkBlocker.SharedMethods()
        
    def setListView(self, list):
        """
        @type list  : list of QWidget
        """
        self.__debug("setListView")
        self.__listViews = list
    
    #==========================================================================
    # set of name of views
    #==========================================================================
    def setLightsViewName(self,string):
        """
        @type string    : string
        @param string   : name of the view containing lights
        """
        self.__debug("setLightsViewName")
        self.__sLightsViewName = string
        
    def setBlockersViewName(self,string):
        """
        @type string : string
        @param string : name of the view containing Blocker
        """
        self.__debug("setBlockersViewName")
        self.__sBlockersViewName = string
        
    def setSetsViewName(self,string):
        """
        @type string : string
        @param string : name of the view containing Sets
        """
        self.__debug("setSetsViewName")
        self.__sSetsViewName = string
    
    def setShadowCamerasViewName(self,string):
        """
        @type string : string
        @param string : name of the view containing Shadow Cameras
        """
        self.__debug("setShadowCamerasViewName")
        self.__sShadowCamerasViewName = string
    
    def setShadowMapsViewName(self,string):
        # obsolete
        # ShadowMaps should be listed in the ListView of pictures
        """
        @type string : string
        @param string : name of the view containing Shadow Maps
        """
        self.__debug("setShadowMapsViewName")
        self.__sShadowMapsViewName = string
        
    def setPicturesViewName(self,string):
        """
        @type string : string
        @param string : name of the view containing external files
                        pictures, shadowmaps etc
        """
        self.__debug("setPicturesViewName")
        self.__sShadowSetsViewName = string
        
    def setGeometriesViewName(self,string):
        """
        @type string : string
        @param string : name of the view containing geometries
        """
        self.__debug("setGeometriesViewName")
        self.__sGeometriesViewName = string
    
    
    #==========================================================================
    # set of list of element
    #==========================================================================            
    def blockers(self):
        """
        Listing blockers.
        self.__listBlockers is initiated in getAssemblies() storing all blockers
        list contains the blocker name but also the path of the icon
        
        @rtype  : list
        @return : list [[blocker name, icon path],...]
        """
        
        self.__debug("blockers")
        list = []
        
        for blocker in self.__listBlockers:
            # Blockers are a coordinate system
            # we need to verify if the coord sys is a blocker
            # by checking the alTag
            ## can be avoid by modifying getAssembly()
            try :
                cmds.getAttr('%s.alType' %blocker)
            except:
                self.__listBlockers.remove(blocker)
                
        if len(self.__listBlockers):
            # creation of list needed by the UI
            for element in self.__listBlockers:
                list.append([element, self.__findIcon(element)])
                
        return list
                    
    def lights(self):
        """
        Listing lights.
        self.__listLights is initiated in getAssemblies() storing all lights
        list contains the lights name but also the path of the icon of the light
        
        @rtype  : list
        @return : list [[light name, icon path],...]
        """
        
        self.__debug("lights")
        list = []
        
        # checking if the light is a light with a atType attributs
        # only lights coming from rigs got this attribut
        for light in self.__listLights:
            try :
                cmds.getAttr('%s.alType' %light)
            except:
                self.__listLights.remove(light)
        
        # creation of the list needed by the UI        
        for element in self.__listLights:
            list.append([element, self.__findIcon(element)])
        
        # loop for listing magic light
        ## needs to be changed
        for key, items in self.__dictCameras.items():
            if key == tl.LIGHT :
                for item in items:
                    list.append([item, self.__findIcon(item)])
                    
        return list

    def shadowCameras(self):
        """
        Listing shadowCameras.
        __dictCameras list cameras (key = type of camera; value = name of camera)
        list contains the shadow cameras name but also the path of the icon 
        
        @rtype  : list
        @return : list [[shadow camera name, icon path],...]
        """
        
        self.__debug("shadowCameras")
        self.__listShadowCameras    = []
        list                        = []
        
        for key, items in self.__dictCameras.items():
            # we are only interested by shadow cameras
            if key == tl.SHADOW_CAMERA :
                for item in items:
                    list.append([item, scc.SHADOW_CAMERA_ICON])
                    self.__listShadowCameras.append(item)
         
        return list
    
    def shadowMaps(self):
        # tmp
        ## todo :P
        
        self.__debug("shadowMaps")
        self.__listShadowMaps = self.__fakeFill(8)
        
        return self.__listShadowMaps
    
    
    def pictures(self):
        # tmp
        ## todo
        ## this function should list all external files
        
        self.__debug("pictures")
        self.__listPictures = []
        list = []
        
        for sFile in cmds.ls(et='script'):
            try :
                cmds.getAttr('%s.alPicture' %sFile)
                list.append([sFile, scc.FILE_ICON])
                self.__listPictures.append(sFile)
            except :
                pass
        return list
    
    def sets(self):
        """
        Listing sets.
        
        @rtype  : list
        @return : list [[sets name, icon path],...]
        """
        self.__debug("sets")
        list                = []
        self.__listSets     = []
        
        # listing sets
        for sSet in cmds.ls(sets=1):
            # I cannot remember why I test if there is no parent
            if cmds.listRelatives(sSet, p=1) == None:
                if cmds.nodeType(sSet) == 'objectSet':
                    # Checking if the type of set.
                    # shadow set or light set or both.
                    sIconPath = self.setSetsIcon(sSet)
                    list.append([sSet, sIconPath])
                    self.__listSets.append(sSet)
                    
        return list
    
    def setSetsIcon(self, sSet):
        """
        There is 3 types of sets :  light set
                                    shadow set
                                    empty set
                                    
        @type sSet      : string
        @param sSet     : name of a set
        
        @rtype  : list
        @return : list [[shadow camera name, icon path],...]
        """
        self.__debug("setSetsIcon")
        sLight      = 0
        sShadow     = 0
        
        # Cheking what kind of connection is link to the set.
        if cmds.listConnections(sSet):
            for sConn in cmds.listConnections(sSet, c=1):
                try : 
                    sType = cmds.getAttr('%s.alType' %sConn)
                    if sType == tl.LIGHT:
                        sLight = 1
                    if sType == tl.SHADOW_CAMERA:
                        sShadow = 1
                except :
                    pass
        
        # Setting the path to the icon.
        sIconPath = 'scc.'
        if sLight == 1:
            sIconPath += 'LIGHT'
        if sShadow == 1:
            sIconPath += 'SHADOW'
        if sIconPath == 'scc.':
            sIconPath += 'EMPTY'
        sIconPath += '_SET_ICON'
        sIconPath = eval(sIconPath)
        
        return sIconPath
    
    def geometries(self):
        """
        Listing geometries.
        list contains the geomtry name
        
        @rtype  : list
        @return : list [[geometry name, ""],...]
        """
        
        self.__debug("geometries")
        self.__listGeometries       = []
        list                        = []
        
        # listing shapes
        for sShape in cmds.ls(g=1):
            try :
                cmds.getAttr('%s.alTag' %sShape)
            except :
                sGeometry = cmds.listRelatives(sShape, p=1)[0]
                self.__listGeometries.append(sGeometry)
                # list contains a "" to be used by the same function than
                # other lists.
                list.append([sGeometry, ''])
        return list

    def __fakeFill(self, i):
        # tmp
        # function to fill a view with fake values
        
        self.__debug("__fakeFill")
        # tmp fonction
        list = []
        a = 0
        while a < i:
            list.append([str(a), ''])
            a += 1
        return list

    def getAssemblies(self):
        """
        Listing of assemblies, then sorting them between lights and liquidCoordSys
        should be changed to list by types instead of all assemblies
        
        self.__listLights lists all lights
        self.__listBlockers list all Blockers
        """
        
        self.__debug("getAssemblies")
        self.__listLights       = []
        self.__listBlockers     = []
        
        for sSel in cmds.ls(assemblies=1):
            sShape  = cmds.listRelatives(sSel)[0]
            sType   = cmds.nodeType(sShape)
            
            if tl.LIGHT in sType:
                self.__listLights.append(sSel)
            elif sType == 'liquidCoordSys':
                self.__listBlockers.append(sSel)
        
    def getCameras(self):
        """ 
        self.__dictCameras stores all alTyped cameras
        that can be magicLights (typed light) listed as light
        or shadowCameras (typed shadowCameras) listed as shadowCamera.
        """
        
        self.__debug("getCameras")
        self.__dictCameras                     = {}
        
        for sShape in cmds.ls(cameras=1):
            # we need to check the transform group
            # as every shapes are typed shape
            sCamera = cmds.listRelatives(sShape, p=1)[0]
            try :
                sType = cmds.getAttr('%s.alType' %sCamera)
                # we create a key.
                # the value of the key is the type of camera
                # that allows to group all cameras by their type
                # without knowing types of cameras
                if not sType in self.__dictCameras.keys():
                    self.__dictCameras[sType] = []
                self.__dictCameras[sType].append(sCamera)
            except :
                # we are not interested in regular cameras
                pass
    
    def select(self, listSel):
        """
        Clear the selection and select object in listSel.
        
        @type listSel: list of strings
        @param listSel: names of objects to select
        """
        
        self.__debug("fromSelection")
        # selection of object(s) in Maya
        cmds.select(clear=1)
        
        if len(listSel)>0:
            cmds.select(listSel)
    
    def findConnections(self, listSel, sType):
        """ 
        find connections of selection
        
        @type listSel   : list
        @param listSel  : list of the current selection
        
        @type sType     : string
        @param sType    : current view name
        
        @rtype      : list
        @return     : list [[name of the view, connection],...]
        """
        
        self.__debug("findConnections")
        listConnections = []
        
        for sSel in listSel :
            if cmds.listConnections(sSel):
                for sConn in cmds.listConnections(sSel):
                    if not sConn == sSel:
                        # is in blocker list ?
                        if sConn in self.__listBlockers and \
                                not sType == self.__sBlockersViewName:
                            if not sConn in listConnections:
                                listConnections.append([self.__sBlockersViewName, 
                                                        sConn])
                                
                        # is in light list ?
                        if sConn in self.__listLights and  \
                                not sType == self.__sLightsViewName:
                            if not sConn in listConnections:
                                listConnections.append([self.__sLightsViewName, 
                                                        sConn])
                                
                        # is in shadowCamera list ?
                        if sConn in self.__listShadowCameras and \
                                not sType == self.__sShadowCamerasViewName:
                            if not sConn in listConnections:
                                listConnections.append([self.__sShadowCamerasViewName, 
                                                        sConn])

                        # is in picture list ?
                        if sConn in self.__listPictures:
                            if not sConn in listConnections:
                                listConnections.append([self.__sShadowSetsViewName, 
                                                        sConn])
                                
                        # is in set list ?
                        if sConn in self.__listSets and \
                                not sType == self.__sSetsViewName:
                            if not sConn in listConnections:
                                listConnections.append([self.__sSetsViewName, 
                                                 sConn])
                                
                        # is in geometry list ?
                        if sConn in self.__listGeometries and \
                                not sType == self.__sGeometriesViewName:
                            if not sConn in listConnections:
                                listConnections.append([self.__sGeometriesViewName, 
                                                        sConn])
                                
        return listConnections 
    
    def createSet(self):
        """
        Creation of a set, with naming by a QDialog
        """
        
        self.__debug("createSet")
        # the dialog should be in the GUI
        text, ok = QtGui.QInputDialog.getText(None,
                                              'Namer', 
                                              'Enter a name:',
                                              QtGui.QLineEdit.Normal,
                                              'set')
        
        if ok:
            cmds.sets(name=str(text), em=1)
            
    def getType(self, string):
        """
        Return the value of alType attribut
        
        @type string    : string
        @param string   : name of the object
        
        @return     : value of alType attribut
        @rtype      : string
        """
        self.__debug("getType")
        
        return self.__oBlockerMethods.getType(string)
    
    def actionGeo2Set(self, listSelection, oItem, boolMode):
        """
        Link several geometries and a set
        
        @type listSelection     : list of objects
        @param listSelection    : list of the second selection
        
        @type oItem             : object
        @param oItem            : main selection
        
        @type boolMode          : boolean
        @param boolMode         : mode add or remove second selection
        """
        
        self.__debug("actionGeo2Set")
        sSet = str(oItem.text())
        for element in listSelection:
            sSel = str(element.text())
            if boolMode ==  1:
                if cmds.sets(sSel,im=sSet) == 0:
                    self.__addGeo2Set(sSel, sSet)
            else :
                if cmds.sets(sSel,im=sSet):
                    self.__removeGeo2Set(sSel, sSet)
    
    def actionSet2Geo(self, listSelection, oItem, boolMode):
        """
        Link several sets and a geometry
        
        @type listSelection     : list of objects
        @param listSelection    : list of the second selection
        
        @type oItem             : object
        @param oItem            : main selection
        
        @type boolMode          : boolean
        @param boolMode         : mode add or remove second selection
        """
        
        self.__debug("actionSet2Geo")
        sGeo = str(oItem.text())
        for element in listSelection:
            sSel = str(element.text())
            if boolMode ==  1:
                if cmds.sets(sGeo,im=sSel) == 0:
                    self.__addGeo2Set(sGeo, sSel)
            else :
                if cmds.sets(sGeo,im=sSel):
                    self.__removeGeo2Set(sGeo, sSel)

    def actionSet2Light(self, listSelection, oItem, boolMode):
        """
        Link several sets and a light
        
        @type listSelection     : list of objects
        @param listSelection    : list of the second selection
        
        @type oItem             : object
        @param oItem            : main selection
        
        @type boolMode          : boolean
        @param boolMode         : mode add or remove second selection
        """
        
        self.__debug("actionSet2Light")
        sLight = str(oItem.text())
        sShape = cmds.listRelatives(sLight)[0]
        for element in listSelection:
            sSel = str(element.text())
            if boolMode ==  1:
                try :
                    self.__linkLight2Set(sShape, sSel)
                except :
                    pass
            else :
                try :
                    self.__unlinkLight2Set(sShape, sSel)
                except:
                    pass
    
    
    def actionLight2Set(self, listSelection, oItem, boolMode):
        """
        Link several lights and a set
        
        @type listSelection     : list of objects
        @param listSelection    : list of the second selection
        
        @type oItem             : object
        @param oItem            : main selection
        
        @type boolMode          : boolean
        @param boolMode         : mode add or remove second selection
        """
        
        self.__debug("actionLight2Set")
        sSel = str(oItem.text())
        for element in listSelection:
            sLight = str(element.text())
            sShape = cmds.listRelatives(sLight)[0]
            if boolMode ==  1:
                try :
                    self.__linkLight2Set(sShape, sSel)
                except :
                    pass
            else :
                try :
                    self.__unlinkLight2Set(sShape, sSel)
                except:
                    pass
                
    def actionLight2Blocker(self, listSelection, oItem, boolMode):
        """
        Link several lights and a blocker
        
        @type listSelection     : list of objects
        @param listSelection    : list of the second selection
        
        @type oItem             : object
        @param oItem            : main selection
        
        @type boolMode          : boolean
        @param boolMode         : mode add or remove second selection
        """
        
        self.__debug("actionLight2Blocker")
        sSel = str(oItem.text())
        for element in listSelection:
            sLight = str(element.text())
            if boolMode ==  1:
                try :
                    self.__block(sLight, sSel)
                except :
                    pass
            else :
                try :
                    self.__unblock(sLight, sSel)
                except:
                    pass
    
    def actionBlocker2Light(self, listSelection, oItem, boolMode):
        """
        Link several blockers and a light
        
        @type listSelection     : list of objects
        @param listSelection    : list of the second selection
        
        @type oItem             : object
        @param oItem            : main selection
        
        @type boolMode          : boolean
        @param boolMode         : mode add or remove second selection
        """
        
        self.__debug("actionBlocker2Light")
        sSel = str(oItem.text())
        for element in listSelection:
            sBlocker = str(element.text())
            if boolMode ==  1:
                try :
                    self.__block(sSel, sBlocker)
                except :
                    pass
            else :
                try :
                    self.__unblock(sSel, sBlocker)
                except:
                    pass
            
    def actionShadowCam2Set(self, listSelection, oItem):
        """
        Link several shadowCameras and a set
        
        @type listSelection     : list of objects
        @param listSelection    : list of the second selection
        
        @type oItem             : object
        @param oItem            : main selection
        """
        
        self.__debug("actionShadowCam2Set")
        sSel = str(oItem.text())
        for element in listSelection:
            sShadowCam = str(element.text())
            self.__shadowSetLink(sSel, sShadowCam)
    
    def actionSet2ShadowCam(self, listSelection, oItem):
        """
        Link several sets and a shadowCamera
        
        @type listSelection     : list of objects
        @param listSelection    : list of the second selection
        
        @type oItem             : object
        @param oItem            : main selection
        """
        
        self.__debug("actionShadowCam2Set")
        sSel = str(oItem.text())
        for element in listSelection:
            sSet = str(element.text())
            self.__shadowSetLink(sSet, sSel)
            
    def actionShadowCam2Light(self, listSelection, oItem, boolMode):
        """
        Link several shadow cameras and a set
        
        @type listSelection     : list of objects
        @param listSelection    : list of the second selection
        
        @type oItem             : object
        @param oItem            : main selection
        
        @type boolMode          : boolean
        @param boolMode         : mode add or remove second selection
        """
        
        self.__debug("actionShadowCam2Light")
        sSel = str(oItem.text())
        sShader = ''
        for i in cmds.listConnections(sSel):
            try:
                if cmds.getAttr('%s.alType' %i) == tl.LIQUID_LIGHT_SHADER:
                    sShader = i
                    break
            except :
                pass
            
        if not sShader == '':
            for element in listSelection:
                sShadowCam = str(element.text())
                sShadowCamShape = cmds.listRelatives(sShadowCam)[0]
                if boolMode == 1:
                    if not sShadowCamShape in cmds.listConnections(sShader):
                        self.__connectShadowCam2Shader(sShadowCam, sShader)
                else :
                    if sShadowCam in cmds.listConnections(sShader):
                        self.__disconnectShadowCam2Shader(sShadowCam, sShader)
    
    def actionLight2ShadowCamera(self, listSelection, oItem, boolMode):
        # tmp
        ## todo
        ## link a light and a shadow camera
        
        self.__debug("actionLight2ShadowCamera")
        sSel = str(oItem.text())
        print sSel
        
    def actionPicture2Light(self, listSelection, oItem, boolMode):
        # tmp
        ## todo
        
        self.__debug("actionPicture2Light")
        print listSelection, oItem.text(), boolMode
    
    def __block(self, sLight, sBlocker):
        """
        Create a link between a light and a blocker.
        
        @type sLight    : string
        @param sLight   : name of a light which has alType/alTag attributs
        
        @type sBlocker  : string
        @param sBlocker : name of a blocker
        """
        
        self.__debug("__block")
        self.__oBlockerLinker.setBlocker(sBlocker)
        self.__oBlockerLinker.setLight(sLight)
        self.__oBlockerLinker.add()

    def __unblock(self, sLight, sBlocker):
        """
        Delete a link between a light and a blocker.
        
        @type sLight    : string
        @param sLight   : name of a light which has alType/alTag attributs
        
        @type sBlocker  : string
        @param sBlocker : name of a blocker
        """
        
        self.__debug("__unblock")
        self.__oBlockerLinker.setBlocker(sBlocker)
        self.__oBlockerLinker.setLight(sLight)
        self.__oBlockerLinker.remove()
        
    def __findIcon(self, sValue):
        """
        return the path to the icon for sValue
        @type sValue    : string
        @param sValue   : name of an maya selection
        
        @rtype      : string
        @return     : path of the icon 
        """
        
        self.__debug("__findIcon")
        sTag = cmds.getAttr('%s.alTag' %sValue)
        sTag = sTag.replace('al_','')
        sTag = sTag.upper()
        
        return eval('scc.%s_ICON' %sTag)

    def __addGeo2Set(self, sGeo, sSet):
        """
        Add a geometry to a set
        
        @type sGeo  : string
        @param sGeo : name of a geometry
        
        @type sSet  : string
        @param sSet : name of a set
        """
        
        self.__debug("__addGeo2Set")
        cmds.sets(sGeo,add=sSet)
    
    def __removeGeo2Set(self, sGeo, sSet):
        """
        remove a geometry to a set
        
        @type sGeo  : string
        @param sGeo : name of a geometry
        
        @type sSet  : string
        @param sSet : name of a set
        """
        
        self.__debug("__removeGeo2Set")
        cmds.sets(sGeo,rm=sSet)
        
    def __shadowSetLink(self, sSet, sShadowCamera):
        """
        Set the liqGeometry attribut of a shadow camera.
        Create a alShadowSet attribut to the set. It will be used
        to find which shadowcamera is connected to a set
        
        @type sSet  : string
        @param sSet : name of a set
        
        @type sShadowCamera     : string
        @param sShadowCamera    : name of a shadow camera
        """
        
        self.__debug("__shadowSetLink")
        sShadowCamShape = cmds.listRelatives(sShadowCamera)[0]
        
        cmds.setAttr('%s.liqGeometrySet' %sShadowCamShape, 
                     sSet,
                     type="string")
        
        if 'alShadowSet' in cmds.listAttr(sShadowCamShape):
            cmds.deleteAttr('%s.alShadowSet' %sShadowCamShape)
        
        cmds.addAttr(sShadowCamShape, 
                            sn='alShadowSet', 
                            dataType='string', 
                            h=1)
        cmds.connectAttr('%s.message' %sSet,
                         '%s.alShadowSet' %sShadowCamShape)
        
    def __linkLight2Set(self, sLightShape, sSet):
        """
        Create a link between a set and a light
        
        @type sLightShape   : string
        @param sLightShape  : name of a light shape
        
        @type sSet  : string
        @param sSet : name of a set
        """
        
        self.__debug("__linkLight2Set")
        
        # using a mel command of Liquid
        mel.eval('LLL_link %s %s' %(sLightShape, sSet))
    
    def __unlinkLight2Set(self, sLightShape, sSet):
        """
        Delete a link between a set and a light
        
        @type sLightShape   : string
        @param sLightShape  : name of a light shape
        
        @type sSet  : string
        @param sSet : name of a set
        """
        
        self.__debug("__unlinkLight2Set")
        
        # using a mel command of Liquid
        mel.eval('LLL_unlink %s %s' %(sLightShape, sSet))

    def __getSets(self):
        """
        """
        ## todo
        # this method seems wrong. I think it is obsolete
        
        self.__debug("__getSets")
        
        listSets    = []
        
        for sSet in cmds.ls(sets=1):
            if cmds.listRelatives(sSet, p=1)    == None:
                if cmds.nodeType(sSet)          == 'objectSet':
                    try :
                        linkedLights = cmds.getAttr('%s.liqLinkedLights' %sSet)
                        if len(linkedLights[0]) == 0:
                            sIconPath = scc.EMPTY_SET_ICON
                        else :
                            sIconPath = scc.LIGHT_SET_ICON
                    except :
                        sIconPath = scc.EMPTY_SET_ICON
                    listSets.append([sSet, sIconPath])
                    
        return listSets

    def __connectShadowCam2Shader(self, sShadowCam, sShader):
        """
        Find a free shader shadowCameras slot and connect a shadow camera to it
        
        @type sShadowCam    : string
        @param sShadowCam   : name of a shadow camera
        
        @type sShader   : string
        @param sShader  : name of a shader
        """
        
        self.__debug("__connectShadowCam2Shader")
        
        a = 0
        sShadowCamShape = cmds.listRelatives(sShadowCam)[0]
        
        # we need to find a free slot for the shadow camera
        while a>-1:
            sConn = '%s.shadowCameras[%d]' %(sShader, a)
            if not sConn in cmds.listConnections(sShader, c=1):
                try:
                    for attr in self.__LIST_SHADOW_CAMERA_ATTR:
                        if attr == 'File':
                            cmds.setAttr('%s.Shadow_%s[%d]' %(sShader, attr, a),
                                    'autoshadow[%d]' %a,
                                    type='string')
                        else :
                            cmds.connectAttr('%s.%s' %(sShadowCam, attr),
                                     '%s.Shadow_%s[%d]' %(sShader, attr, a))
                            
                    mel.eval('connectExistingShadowCamera %s  -source %s;'\
                             %(sConn,sShadowCamShape))
                except:
                    pass
                break
            a+=1
    
    def __disconnectShadowCam2Shader(self, sShadowCam, sShader):
        """
        Find the connection between the shader and a shadow camera
        and delete it
        
        @type sShadowCam    : string
        @param sShadowCam   : name of a shadow camera
        
        @type sShader   : string
        @param sShader  : name of a shader
        """
        
        self.__debug("__disconnectShadowCam2Shader")
        
        a = 0
        sShadowCamShape = cmds.listRelatives(sShadowCam)[0]
        
        while a<50: # not -1 to avoid infinite loop
                    # not sure about if it is usefull but ...
            sConn = '%s.shadowCameras[%d]' %(sShader, a)
            
            if sShadowCam in cmds.listConnections(sConn, c=1):
                cmds.disconnectAttr('%s.message' %sShadowCamShape,
                                    sConn)
                for attr in self.__LIST_SHADOW_CAMERA_ATTR:
                    if attr == 'File':
                        cmds.setAttr('%s.Shadow_%s[%d]' %(sShader, attr, a),
                                    '',
                                    type='string')
                    else :
                        cmds.disconnectAttr('%s.%s' %(sShadowCam, 
                                                      attr),
                                            '%s.Shadow_%s[%d]' %(sShader, 
                                                                 attr, 
                                                                 a))
                break
            a+=1
            
    def __debug(self, string):
        """
        function to track the use of function of the class
        @type string    : string
        @param string   : name of the function to track
        """
        
        if self.__DEBUG == 1:
            print "Model.%s()" %string
            
# Ni !