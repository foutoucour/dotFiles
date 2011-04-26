# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

class Model:
    __MAYA_CAMERAS_LIST     = ['persp','front','top','side']
    name                    = __name__

    def __init__(self):
        self.__listCameras  = self.__MAYA_CAMERAS_LIST
        self.__sStepValue   = 0


    def setResolutionX(self, iValue):
        self.__iResolution = iValue

    def setResolutionY(self, iValue):
        self.__iResolutionY = iValue

    def refreshCameraList(self, listCameras):
        """
        """
        listOldCameras = listCameras
        listNewCameras = self.cameraListing()
        if len(listOldCameras) == len(listNewCameras):
            for sCamera in listNewCameras :
                if not sCamera in listOldCameras:
                    self.__setCamera(self.__testForOnlyMayaCamera())
                    self.__oGui.refreshCameraList()
                    return sCamera
        else :
            self.__setCamera(self.__testForOnlyMayaCamera())
            self.__oGui.refreshCameraList()

    def cameraListing(self):
        """
        Listing of Camera of the scene.
        This listing needs to exclude shadow cameras
        Shadow cameras got the alTag and alType tag
        """
        listCameras = []
        for sCamera in  cmds.ls(cameras=1):
            sType = ''
            try :
                cmds.getAttr('%s.alType' %sCamera)
                sCamera = cmds.listRelatives(sCamera, p=1)[0]
                sType = cmds.getAttr('%s.alType' %sCamera)
                # If the alType is equal to Light that means
                # The camera is part of the magicLight Rig
                # And we want to add it to the list
                if sType == 'Light':
                    listCameras.append(sCamera)
            except :
                try :
                    for sConn in cmds.listConnections(sCamera):
                        try :
                            sType = cmds.getAttr('%s.alType' %sConn)
                        except:
                            pass
                except :
                    pass
                if not sType == 'Light':
                    sCamera = cmds.listRelatives(sCamera, p=1)[0]
                    listCameras.append(sCamera)
        listCameras.sort()
        return listCameras

    def testForOnlyMayaCamera(self, listCameras):
        if len(listCameras) == 4:
            for sCamera in self.__MAYA_CAMERAS_LIST:
                if not sCamera in self.__listCameras:
                    return 0
            return listCameras.index('persp')
        return 0

    def splitFrameValue(self, sValue):
        return sValue.split('x')

    def text2Bool(self,string):
        if string == 'True':
            return 1
        else :
            return 0

    def clampedBool(self,int):
        if int > 1:
            int = 1
        return int

    def invertedBool(self, int):
        return 1-int

    def double(self,string):
        return 2*int(string)

    def findIndex(self, list, variable):
        try :
            return list.index(str(variable))
        except :
            return 0

    def keepValueBetween0n1(self, value):
        """
        keep a value between 0 and 1
        @type value: number (interger, long, float)
        @param value: value to modify
        """
        if value < 0:value = 0
        elif value > 1:value = 1
        return value

    def setFrameValue(self, sFrameValue, sStepValue):
        sValue = self.splitFrameValue(sFrameValue)[0]
        sValue += 'x'
        if sStepValue == '0' or sStepValue == '':
            sStepValue= '1'
        sValue += sStepValue
        return sValue


    def makeListOfNumbers(self, iStep):
        listNumbers = []
        iNumber = 0
        while iNumber <=(200-iStep) :
            iNumber += iStep
            listNumbers.append(self.resolutionListFormat(iNumber))
        return listNumbers

    def resolutionListFormat(self, iValue):
        iValue = int(iValue)
        iResoX = int(self.__iResolution * iValue /100)
        iResoY = int(self.__iResolutionY * iValue /100)
        return str(iValue)+'% ('+str(iResoX)+'/'+str(iResoY)+')'

    def __workfolder(self):
        return  cmds.workspace( q=True, o=True )

    def getPath(self, liquidParameter):
        sPath = self.__workfolder()
        try :
            sPath += cmds.getAttr(liquidParameter)
        except :
            pass
        return sPath

    def openFolder(self, sPath):
        if not os.system('gnome-open %s' %sPath) == 0:
            i=0
            sNewPath = ''
            listPathSplit = sPath.split(os.sep)
            while i < len(listPathSplit)-2:
                sNewPath += listPathSplit[i]
                sNewPath += os.sep
                i+=1
            self.openFolder(sNewPath)

# Ni !
