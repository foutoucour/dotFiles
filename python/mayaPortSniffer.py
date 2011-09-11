import os
import re
import maya.cmds as cmds
import maya.mel as mel
import cPickle

class MayaLightRigSniffer(object):
    """ Class to find and extract details of maya light rigs.
    """
    __reg = re.compile('lightRig')
    _filenamePatern = '/tmp/mayaInfoLightRig.shot.'


    def getFilename(sessionID):
        """
        """
        return '%s.%s' %(self.__filename, str(sessionID))

    def __init__(self, port, sessionID):
        """
        """
        self.__port = port
        self._sessionID = sessionID
        self._filename = self.getFilename(self._sessionID)
        self.shotMaya = os.getenv('SHOT')
        self.lightRigGroups = [ node for node in cmds.ls(type = 'transform') if self.__reg.search(node) ]

    def writeFile(self):
        """
        """
        myFile = open(self._filename, 'w')

        dictDetails = {
            'session':self._sessionID,
            'port':self.__port,
            'shot':self.shotMaya,
            'lightRigs':self.lightRigGroups
        }

        cPickle.dump(dictDetails, myFile)


