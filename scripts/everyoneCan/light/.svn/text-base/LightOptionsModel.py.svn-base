import maya.cmds as cmds
from PyQt4 import QtCore
from PyQt4 import QtGui

import al.pipeline
import tactic_client_lib
import re

from everyoneCan import lightRigTypes           #class with alType types
from everyoneCan import multiLinkBlocker
from everyoneCan import al_magicLightAttr

class Model(QtGui.QWidget, lightRigTypes.TypeLister):
    """
    Model of lightOptions With all logic part of the tool
    lightRigTypes.TypeLister is where alType values are stored
    """
    #==========================================================================
    # constants
    #==========================================================================
    __LIST_ATTR             = ['translateX',
                                   'translateY',
                                   'translateZ',
                                   'rotateX',
                                   'rotateY',
                                   'rotateZ',
                                   'visibility',
                                   'color',
                                   'translate',
                                   'rotate',
                                   'SHADOW',
                                   'INTENSITY',
                                   'liquidLightShaderNode',
                                   'message'
                                   ]
    
    __INSTANCE_MASTER_ATTR  = 'alInstanceMaster'
    __TAG_OF_MASTER         = 'alTag'
    #==========================================================================
    # variables
    #==========================================================================
    
    
    def __init__(self):
        """
        """
        QtGui.QWidget.__init__(self)
#        self.__oGui                 = oGui
        self.__oBlockerLinker       = multiLinkBlocker.Finder()
        self.__oServer              = tactic_client_lib.TacticServerStub()
        self.__boolCreateReference  = 0
        self.__boolCopyAttr         = 0
        self.__boolLinkAttr         = 0
        self.__sLightType           = ''
        self.__sRefPath             = ''
 
    def linkBlocker(self):
        self.__oBlockerLinker.add()
        
    def unlinkBlocker(self):
        self.__oBlockerLinker.remove()
        
    def createReference(self, sType):
        """
        Methods to create a reference.
        @type sType: string
        @param sType: Type of reference (spot, point...). Will be also used
                        as namespace before renaming
        """
        # __boolCreateReference is to indicate if we are creating a reference
        # during the __getValueAndRename method.
        self.__boolCreateReference = 1 
        self.__sLightType = sType
        self.__setReferenceName(sType)

    def renameRef(self):
        """
        Method to rename a reference. It changes the namespace.
        """
        sel = self.__getSelection()[0]
        sNamespace, sName = self.__splitReferenceName(sel)
        self.__sRefPath = self.__getPathFromSelection(sel)
        self.__setReferenceName(sNamespace)
        
    def removeRef(self):
        """
        Method to remove a reference.
        Special function for blockers
        """
        listSel = self.__getSelection()
        for sel in listSel:
            if cmds.getAttr('%s.alType' %sel) == self.blocker :
                # we need to delete some values in the shader
                # to have a proper delete
                # or we will still have for this slot the switch on
                # and a value for coordSys
                self.__unlinkBlockerAndShader(sel)
            sRefNode = self.__getPathFromSelection(sel)
            cmds.file(sRefNode, rr=1)
        
    def duplicateRef(self):
        """
        Method to duplicate a Reference.
        Duplicate means to get from pipeline the same type of 
        reference and to set the same values.
        """
        self.__boolCopyAttr = 1
        self.__listLight = []
        self.__listLight.append(self.__getSelection()[0])
        sNamespace, sName = self.__splitReferenceName(self.__listLight[0])
        sNamespace += 'Dupl'
        self.__sRefPath = self.__getPathFromSelection(self.__listLight[0])
        self.__setReferenceName(sNamespace)
    
    def instance(self):
        """
        Method to instanciate a reference
        Instanciate means to get from pipeline the same type of reference
        and to link all Attribut from the master to the instance
        """
        self.__boolLinkAttr = 1
        self.__listLight = []
        self.__listLight.append(self.__getSelection()[0])
        sNamespace, sName = self.__splitReferenceName(self.__listLight[0])
        sNamespace = '__%s' %sNamespace
        self.__sRefPath = self.__getPathFromSelection(self.__listLight[0])
        self.__setReferenceName(sNamespace)
    
    def unlink(self):
        """
        Method to unlink an instance and its master
        """
        sSel = self.__getSelection()[0]
        sMaster = self.__findMaster()
        if not sMaster == '':
            for sAttr in cmds.listAttr(sMaster):
                try:
                    cmds.disconnectAttr('%s.%s' %(sMaster, sAttr),
                        '%s.%s' %(sSel,sAttr))
                except :
                    pass
            sMaster = cmds.listRelatives(sMaster)[0]
            for sAttr in cmds.listAttr(sMaster):
                if not 'liquid' in sAttr:   #or it will break a connection with 
                                            #liquid, I can't tell which...
                    try:
                        cmds.disconnectAttr('%s.%s' %(sMaster, sAttr),
                                            '%s.%s' %(sSel,sAttr))
                    except :
                        pass
            self.__copyAttr(sMaster,sSel)
            sInstanceAttr = '%s.%s' %(sSel,self.__INSTANCE_MASTER_ATTR)
            cmds.deleteAttr(sInstanceAttr)
    
    def selectMaster(self):
        """
        Method to find and select the master of the selected instance
        """
        sMaster = self.__findMaster()
        if not sMaster == '': 
            cmds.select(sMaster)
    
    def selectInstance(self):
        """
        Method to find and select the master of the selected instance
        """
        listInstances = self.__findInstance()
        if not len(listInstances) == 0: 
            cmds.select(listInstances)
    
    def snap(self):
        """
        Method to snap 2 objects
        the second selected will snap on the first one
        """
        sel = self.__getSelection()
        a = 0
        while a < len(self.__LIST_ATTR)-6:
            cmds.setAttr('%s.%s' %(sel[1], self.__LIST_ATTR[a]), 
                         cmds.getAttr('%s.%s' %(sel[0], self.__LIST_ATTR[a])))
            a += 1
            
    def magicLightAddAttr(self):
        al_magicLightAttr.main(1)
        
    def magicLightRemoveAttr(self):
        al_magicLightAttr.main(0)
        
    #==========================================================================
    # Private methods
    #==========================================================================
    def __getSelection(self):
        """
        Method to get the selection.
        @rtype: list
        @return: list of string of current selection
        """
        return cmds.ls(sl=1)

    def __getPathFromSelection(self, string):
        """
        Method to get the path of the selected reference
        @rtype: string
        @return: file path
        """
        return cmds.referenceQuery(string,filename=True)
    
    def __setNamespace(self, string):
        sNoNumber = string
        if re.search('[0-9]\Z', sNoNumber) == None:
            sNewString = '%s01' %string
        else :
            while not re.search('[0-9]\Z', sNoNumber) == None:
                lenght = len(sNoNumber)
                sNoNumber = sNoNumber[0:lenght-1]
    
            sNumbers = string[len(sNoNumber):]
            sNextNumbers = str(1 + int(sNumbers))
            iNumberOfZero = 0
            while len(sNumbers) > len(sNextNumbers):
                sNextNumbers = '0%s' %sNextNumbers
                iNumberOfZero += 1
            sNewString = '%s%s' %(sNoNumber, sNextNumbers)
        return sNewString
        
    def __setReferenceName(self,sNamespace):
        """
        Call of an instance of ec__Namer.Naming Class.
        It allows to set a name to the reference.
        @type sNamespace: string
        @param sNamespace: current name of the reference
        """
        text, ok = QtGui.QInputDialog.getText(None,
                                              'Namer', 
                                              'Enter a name:',
                                              QtGui.QLineEdit.Normal,
                                              sNamespace)
        if ok:
            self.__getValueAndRename(str(text))
    
    def __getValueAndRename(self, sNewNamespace):
        """
        call when the ec__Namer.Naming() instance
        emit the QtCore.signal 'Naming_nameSet'
        @rtype: string
        @return: name set by the user
        """
#        sNewNamespace = str(self.__oNamer.getValue())
        while cmds.namespace( exists=sNewNamespace) == 1:
            sNewNamespace = self.__setNamespace(sNewNamespace)
        # __boolCreateReference allows to know if we are creating a ref
        # or if we are modifying it
        if self.__boolCreateReference == 1:
           self.__boolCreateReference = 0
           self.__create(self.__sLightType,
                                  sNewNamespace)
        else:
            # __boolCopyAttr indicates if we are copying attrs 
            if self.__boolCopyAttr == 1:
                self.__boolCopyAttr = 0
                self.__sRefPath =  self.__createReferenceFromPath(
                                                        self.__sRefPath,
                                                        sNewNamespace)
                self.__selectFromPath(self.__sRefPath)
                self.__listLight.append(cmds.ls(sl=1)[0])
                self.__copyAttr(self.__listLight[0],self.__listLight[1])
                self.__copyAttr(self.__getShape(self.__listLight[0]),
                                self.__getShape(self.__listLight[1]))
            
            # __boolLinkAttr indicates if we are linking attrs    
            elif self.__boolLinkAttr == 1:
                self.__boolLinkAttr = 0
                self.__sRefPath =  self.__createReferenceFromPath(
                                                        self.__sRefPath,
                                                        sNewNamespace)
                self.__selectFromPath(self.__sRefPath)
                self.__listLight.append(cmds.ls(sl=1)[0])                
                self.__copyAttr(self.__listLight[0],self.__listLight[1])
                self.__copyAttr(self.__getShape(self.__listLight[0]),
                                self.__getShape(self.__listLight[1]))
                self.__linkAttr(self.__listLight[0],self.__listLight[1])
                self.__linkAttr(self.__getShape(self.__listLight[0]),
                                self.__getShape(self.__listLight[1]))
                self.__selectFromPath(self.__sRefPath)
                # __INSTANCE_MASTER_ATTR is a hidden attribut to keep a link
                # with the master of links
                cmds.addAttr(sn=self.__INSTANCE_MASTER_ATTR,h=1, dt='string')
                cmds.connectAttr('%s.%s' %(self.__listLight[0],
                                 self.__TAG_OF_MASTER),
                                 '%s.%s' %(self.__listLight[1],
                                 self.__INSTANCE_MASTER_ATTR),
                                 f=1)
            # renaming 
            else:
                sel = self.__getSelection()[0]
                sRefNode = self.__getPathFromSelection(sel)
                cmds.file(str(sRefNode),e=True,ns=sNewNamespace)
        
        self.emit(QtCore.SIGNAL('LightOptionsModel_Signal'))
        return 1
    
    def __create(self, sType, sNamespace):
        """
        Method to create a Reference.
        @type sType: string
        @param sType: type of reference
        @type sNamespace: string
        @param sNamespace: namespace for the new reference
        @rtype: string
        @return: return the path of the reference if exists, or '' 
        """
        sPath = self.__getPathFromTactic(sType)
        if not sPath == 0:
            self.__createReferenceFromPath(sPath, sNamespace)
#            self.__selectFromPath(sPath)
            self.__selectFromNamespace(sNamespace)
            return sPath
        else :
            return 0
    
    def __getPathFromTactic(self, sAsset):
        """
        Method to get from Tactic the path of the last file of the reference.
        @type sAsset: string
        @param sAsset: name of the asset
        @rtype: string
        @return: path of the file if exists, '' if not 
        """
        oAsset = al.pipeline.getAssets(project='plants',
                                              assets=[sAsset]
                                              )[0]
        dictSnapShot =  self.__oServer.get_snapshot(
                                       oAsset.searchKey,
                                         context='lightrig_fine')
        listPaths = self.__oServer.get_all_paths_from_snapshot(
                                                    dictSnapShot['code'])
        for sPath in listPaths:
            if 'fine.mb' in sPath :
                return sPath
        return ''
        
    def __copyAttr(self, sSource, sTarget):
        """
        Method to copy attr between two objects.
        @type sSource: string
        @param sSource: name of the object giving values
        @type sTarget: string
        @param sTarget: name of the object receiving values
        """
        for sAttr in cmds.listAttr(sSource):
            try :
                AttrValue = cmds.getAttr('%s.%s' %(sSource, sAttr))
                command = '%s.%s,' %(sTarget, sAttr)
                command += AttrValue
                cmds.setAttr(command)
            except:
                try : 
                    command += ",type='string'"
                    cmds.setAttr('%s.%s' %(sTarget, sAttr), AttrValue,)
                except:
                    pass
        return
                
    def __linkAttr(self,sSource, sTarget):
        """
        Method to link attrs of two objects.
        @type sSource: string
        @param sSource: name of the object giving values
        @type sTarget: string
        @param sTarget: name of the object receiving values
        """
        for sAttr in cmds.listAttr(sSource):
            if not sAttr in self.__LIST_ATTR:
                try:
                    cmds.connectAttr('%s.%s' %(sSource, sAttr),
                                     '%s.%s' %(sTarget,sAttr), f=1)
                except:
                    pass
        return

    def __selectFromPath(self, sPath):
        """
        Method to select a reference from the path of a file.
        @type sPath: string
        @param sPath: path of a file
        """
        cmds.select(cl=1)
        cmds.file(str(sPath), sa=1)
        cmds.select(self.__getSelection()[0])
        return
    
    def __selectFromNamespace(self, sNamespace):
        cmds.select(cl=1)
        sel = cmds.ls('%s:al_*' %sNamespace, shapes=1)[0]
        sel = cmds.listRelatives(sel, p=1)
        cmds.select(sel)
    
    def __createReferenceFromPath(self, sPath, sNamespace):
        """
        Method to create a reference from the path of a file.
        @type sPath: string
        @param sPath: path of a file
        @type sNamespace: string
        @param sNamespace: name of the reference namespace
        @rtype: string
        @return: file path
        """
        return cmds.file( sPath, r=1, 
                   ns=str(sNamespace), type='mayaBinary')
        
    def __splitReferenceName(self, sRefName):
        """
        Method to split namespace and name of a reference.
        @type sRefName: string
        @param sRefName: name of a reference
        @rtype: string list
        @return: [namespace, name] 
        """
        return sRefName.split(':')

    def __getShape(self, sObject):
        """
        Method to get the shape of an object.
        @type sObject: string
        @param sObject: name of object
        @rtype: string
        @return: name of shape
        """
        return cmds.listRelatives(sObject)[0]
        
    def __findMaster(self):
        """
        Method to get the master of an selected instance.
        @requires: need a seleted instance
        @rtype: string
        @return: name of the master, or '' if no master
        """
        sSel = self.__getSelection()[0]
        sAttr = '%s.%s' %(sSel,self.__INSTANCE_MASTER_ATTR)
        try :
            sMaster = cmds.connectionInfo(sAttr, sfd=1)
            sMaster = sMaster.split('.')[0]
        except :
            sMaster = ''
        return sMaster
    
    def __findInstance(self):
        """
        Method to get the master of an selected instance.
        @requires: need a seleted instance
        @rtype: string
        @return: name of the master, or '' if no master
        """
        sSel = self.__getSelection()[0]
        listInstances = []
        sAttr = '%s.%s' %(sSel,self.__TAG_OF_MASTER)
        for sConn in  cmds.connectionInfo(sAttr, dfs=1):
            if self.__INSTANCE_MASTER_ATTR in sConn:
                listInstances.append(sConn.split('.')[0])
        return listInstances
    
    def __unlinkBlockerAndShader(self, sBlocker):
        """
        Method to set some value on shaders linked to a blocker.
        @type sBlocker: string
        @param sBlocker: name of a blocker
        """
        sBlockerShape = self.__getShape(sBlocker)
        sAttr = '%s.BlurX' %sBlocker
        for sConn in cmds.connectionInfo(sAttr, dfs=1):
            sConn = sConn.split('.')[0]
            try :
                if cmds.getAttr('%s.alType' %sConn) == 'LiquidLightShader':
                    a = 0
                    while a < 4:
                        if cmds.getAttr('%s.Blocker_CoordSys[%d]' %(
                                                sConn,a))==sBlockerShape :
                            break
                        a+=1
                    cmds.setAttr('%s.Blocker_CoordSys[%d]' %(
                                                sConn,a), '', type='string')
                    cmds.setAttr('%s.Blocker_Switch[%d]' %(
                                                sConn,a), 0)
            except :
                pass
        return sBlockerShape
    
# Ni !