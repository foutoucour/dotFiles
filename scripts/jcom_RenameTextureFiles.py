#!/usr/bin/env mpcpython
#jordi-r Tue 11 Jan 2011 10:21:11 GMT
#jordi-r Thu 13 Jan 2011 12:57:45 GMT
# Script to rename texture coming from studio according to artist requests.
#


import sys
import os

class Categorie:
    """
    Class defining the setup of a categories of files.
    """

    def replaceDictByDictNumber(self, iNumber):
        """
        Method to input the variation coming from the variant dictionary.

        @type iNumber : integer.
        @param iNumber : ID of the variation
        """
        dictTmp = eval("self.DICT_TEXTURE_TYPE%s" %str(iNumber))
        for key in dictTmp.keys():
            self.DICT_TEXTURE_TYPE[key] = dictTmp[key]

    def addStudioFile(self, sFilename):
        """
        Method to add a studio file.

        @type sFilename : string
        @param sFilename : file to add to the list
        """
        self.listStudioFiles.append(sFilename)

    def addMpcFile(self, sFilename):
        """
        Method to add a mpc file.

        @type sFilename : string
        @param sFilename : file to add to the list
        """
        self.mpcFilename = self.setMpcFilename(sFilename)
        self.listMpcFiles.append(self.mpcFilename)

    def setStudioFolder(self, sFolder):
        """
        Method to set the folder where the file will be saved.

        @type sFolder : string
        @param sFolder : path to a folder
        """
        self.studioFolder = sFolder

    def setMpcFolder(self, sFolder):
        """
        Method to set the folder where the file will be saved.

        @type sFolder : string
        @param sFolder : path to a folder
        """
        self.mpcFolder = sFolder

    def setCommandParameters(self, iLevel=0, iHeroLevel=0):
        """
        Method to set parameters of the function to set the name of created files.

        @type iLevel : integer.
        @param iLevel : level of folder in the path, this will be used to set the name
                        of the created file.
                        Using this way as name are not always the same (at least the
                        path is).

        @type iHeroLevel : integer.
        @param iHeroLevel : level of folder in the path where we can find some additional
                            informations (used for Heros or special variations eg).
        """
        self.iLevel = iLevel
        self.iHeroLevel = iHeroLevel

    def setPath(self, sPath):
        """
        Method to set the path of the categorie.

        @type sPath : string.
        @param sPath : a path.
        """
        self.sPath = sPath

    def findMpcFileFromStudioFile(self, studioFile):
        """
        Method to find the the equivalent file between the list containing studio files
        and MPC files.

        @type studioFile : string.
        @param studioFile : file from a studio folder.

        @rtyp : string
        @return : file from mpc folder.
        """
        iIndex = self.listStudioFiles.index(studioFile)
        return self.listMpcFiles[iIndex]

    def __init__(self, sName):
        """
        @type sName : string.
        @param sName : name of the categorie.
        """
        self.name = sName
        self.listStudioFiles = []
        self.listMpcFiles = []
        self.studioFolder = ""
        self.mpcFolder = ""
        self.iLevel = 0
        self.iHeroLevel = 0

    def setMpcFilename(self, sFilename):
        """
        Method to set the filename of the created file.

        @type sFilename : string
        @param sFilename : master file from which the name of the new file will set from.

        @rtype : string
        @return : name of the new file
        """
        sSlot = ""
        sType = ""

        sExt = os.path.splitext(sFilename)[-1]

        sType = self.getTextureType(sFilename)

        # For costumes and props, the filename is based on folders
        # and not on the filename.
        if self.iLevel == 0 :
            sSlot = self.getTextureSlot(sFilename)
        else :
            splitedDirs = self.sPath.split(os.sep)
            sSlot = splitedDirs[self.iLevel].lower()

            if not self.iHeroLevel == 0 :
                #sSecondPart = "%s%s" %(sPlace[0].upper(), sPlace[1:])
                firstWord = splitedDirs[self.iHeroLevel].lower()
                #sSlot += sSecondPart
                sSlot = self.camelCase(firstWord, sSlot)
            else :

                if len(splitedDirs) > 17 :
                    sAdditionalInfo = splitedDirs[len(splitedDirs)-1]
                    splitAdditionalInfo = sAdditionalInfo.split("-")
                    sAdditionalName = splitAdditionalInfo[-4].lower()
                    sSlot = self.camelCase(sAdditionalName, sSlot)

        mpcFilename = ""

        if not sSlot == "":
            mpcFilename += "%s_" %sSlot

        if not sType == "":
            mpcFilename += "%s" %sType

        if not mpcFilename == "":
            mpcFilename += "%s" %sExt
        else :
            mpcFilename = sFilename

        return mpcFilename

    def getTextureType(self, sFilename):
        """
        Method to get the type of texture.

        @type sFilename : string.
        @param sFilename : filename from which we will find the type of texture.

        @rtype : string.
        @return : type of texture.
        """
        splitedFilename = self.splitFilename(sFilename)

        for sPart in splitedFilename:

            for key in self.DICT_TEXTURE_TYPE:

                if key == sPart:
                    return self.DICT_TEXTURE_TYPE[key]

    def splitFilename(self, sFilename):
        """
        Method to split a filename by _ and -.

        @type sFilename : string.
        @param sFilename : filename to split.

        @rtype : list
        @return : list of strings
        """
        sFilename = sFilename.replace("_","-")
        return sFilename.split("-")

    def getTextureSlot(self, sFilename):
        """
        Method to get the slot of texture.

        @type sFilename : string.
        @param sFilename : filename from which we will find the slot of texture.

        @rtype : string.
        @return : slot of texture.
        """
        for key in self.DICT_TEXTURE_SLOT:

            if key in sFilename:
                return self.DICT_TEXTURE_SLOT[key]


    def camelCase(self, firstWord, secondWord):
        """
        Method to set a string composed of 2 words to camelCase.

        @type firstWord : string.
        @param firstWord : first part of the new string.

        @type secondWord : string.
        @param secondWord : second part of the new string.

        @rtype : string.
        @return : new string coming from the concatenation of the 2 inputs.
        """
        secondWord = "%s%s" %(secondWord[0].upper(), secondWord[1:])
        return "%s%s" %(firstWord, secondWord)

class CinesiteCategorie(Categorie):
    """
    Redefinition if Categorie class according to Cinesite input.
    """
    DICT_TEXTURE_SLOT = { "0_0":"face",
                        "0_1":"hair",
                        "1_0":"chest",
                        "2_0":"legs",
                        "3_0":"handsArms",
                        "4_0":"fabric",
                        "5_0":"boots",
                        "6_0":"armour",
                        }


    DICT_TEXTURE_TYPE = { "col":"COL",
                          "disp":"DISP",
                          "spec":"SPEC",
                            }

    def __init__(self, sName):
        Categorie.__init__(self, sName)

    def getTextureSlot(self, sFilename):
        """
        Method to get the slot of texture.

        @type sFilename : string.
        @param sFilename : filename from which we will find the slot of texture.

        @rtype : string.
        @return : slot of texture.
        """
        for key in self.DICT_TEXTURE_SLOT:
            sFilename = os.path.splitext(sFilename)[0]
            splitFilename = self.splitFilename(sFilename)
            slot = "%s_%s" %(splitFilename[-2], splitFilename[-1])

            if slot == key:
                return self.DICT_TEXTURE_SLOT[key]

class DnegCategorie(Categorie):
    """
    Redefinition if Categorie class according to Dneg input.
    """
    # Main dictionary of different types of textures.
    # key : dneg, value : MPC.
    DICT_TEXTURE_TYPE = { "RGB":"COL",
                            "RGB2":"COLbackPatches",
                            "RGB3":"COLblueTint",
                            "BMP":"BUMP",
                            "BMP2":"BUMPmediumDispDetail",
                            "BMP3":"BUMPmediumTuskIntegrationDetail",
                            "DSP":"DISP",
                            "DSP2":"DISPscars",
                            "SPC":"SPEC",
                            "SPC1":"SPECwet",
                            "SPC2":"SPCdetail",
                            "SPC3":"SPECsecondary",
                            "SPCR":"SPECroughness",
                            "SPCR2":"SPECbreakup",
                            "OPC":"OPAC",
                            "SSD":"SSD",
                            "SSDMask":"SSD",
                            "SSS":"SSS",
                            "MSK1":"ISOskinReveal",
                            "MSK2":"ISOsunBurn",
                            "MSK3":"ISOpaleUnder",
                            "MSK4":"ISOredTint",
                            "MSK5":"ISOfaceDarken",
                            "DRT":"DIRT",
                            "GRM":"GRIME",
                            "GRIME":"GRIME",

                            }

    # Variant #0 of type of textures.
    # key : dneg, value : MPC.
    # Havs to be public to work.
    DICT_TEXTURE_TYPE0 = {"RGB":"COL",
                            "BMP":"BUMP",
                            "BMP2":"BUMPmediumDispDetail",
                            "BMP3":"BUMPfold",
                            "DSP2":"DISPscars",
                            "SPC":"SPEC",
                            "SPC1":"SPECwet",
                            "SPC2":"SPECdetail",
                            "SPC3":"SPECsecondary",
                            "SPCR":"SPECroughness",
                            "SPCR2":"SPECbreakup",
                            "OPC":"OPAC",
                            "SSD":"SSD",
                            "SSDMask":"SSD2",
                            "SSS":"SSS",
                            "MSK1":"ISOskinReveal",
                            "MSK2":"ISOpad",
                            "DRT":"DIRT",
                            "GRM":"GRIME",
                            }

    # Dictionary of differents slots for textures.
    # key : dneg, value : MPC.
    DICT_TEXTURE_SLOT = {"1001":"face",
                            "1002":"neck",
                            "1003":"tusks",
                            "1004":"chest",
                            "1005":"back",
                            "1006":"legs",
                            "1007":"armsA",
                            "1008":"armsB",
                            "1009":"claws",
                            "1010":"mouth",
                            "1011":"teeth",
                            "1012":"eyesInnerL",
                            "1013":"eyesInnerR",
                            "1014":"eyesOuterL",
                            "1015":"eyesOuterR",
                            "1016":"belly",
                            "1017":"cheeks",
                            "1018":"mouthLower",
                            "1019":"mouthUpper",
                            "1020":"mouthIntLower",
                            "1021":"mouthIntUpper",
                            "1022":"tongue",
                            "1023":"eyes",
                            "1024":"jawLower",
                            "1025":"legsMiddle",
                            "1026":"legsFrontR",
                            "1027":"legsFrontL",
                            "1028":"legsBack",
                            "1029":"legsFrontL",
                            "1030":"legsFrontR",
                            "1031":"bone",
                            "1032":"leather",
                            "1033":"wood",
                            "1034":"arseflap",
                            "1035":"braceletul",
                            "1036":"loincloth",
                            "1037":"mantle",
                            "1038":"necklace",
                            "1039":"nails",
                            }

    def __init__(self, sName):
        Categorie.__init__(self, sName)

    def getTextureSlot(self, sFilename):
        """
        Method to get the slot of texture.

        @type sFilename : string.
        @param sFilename : filename from which we will find the slot of texture.

        @rtype : string.
        @return : slot of texture.
        """
        for key in self.DICT_TEXTURE_SLOT:

            if key in sFilename:
                return self.DICT_TEXTURE_SLOT[key]

        splitedFilename = self.splitFilename(sFilename)

        for sPart in splitedFilename:
            sPart = sPart.lower()

            for value in self.DICT_TEXTURE_SLOT.values():

                if value.lower() == sPart:

                    # This a special case.
                    if "mouthInt" in value:
                        value = value.replace("Int", "")

                    return value

class Studio:
    """
    Class defining a studio
    """
    name = ""

    TEXTURE_FOLDER = "TEXTURE"

    LIST_CHARACTER_USING_DIFFERENT_TYPES = [ ]

    LIST_CATEGORIES = [ ]

    def __init__(self, sRootFolder):
        """
        @type sRootFolder : string
        @param sRootFolder : Path to the folder where the script start from.
        """
        # Dynamic creation of categories.
        self.listCategories = []
        for listCat in self.LIST_CATEGORIES:
            oCategorie = self.createCategorie(listCat[0])

            if len(listCat) > 1 :

                for sAdditonalParameter in listCat[1]:
                    eval("oCategorie.%s" %sAdditonalParameter)

            self.listCategories.append(oCategorie)

        # The path is checked to set the dictionary of type.
        for sCharacterType in self.LIST_CHARACTER_USING_DIFFERENT_TYPES:
            sCharacter = sCharacterType[0]

            if sCharacter.lower() in sRootFolder.lower():
                iIndex = self.LIST_CHARACTER_USING_DIFFERENT_TYPES.index(sCharacterType)

                for oCategorie in self.listCategories:
                    oCategorie.replaceDictByDictNumber(iIndex)

    def createCategorie(self, sName=""):
        """
        Creation of a categorie instance.
        The type of categorie depends on the studio.

        @type sName : string
        @param sName : Name of the categorie.

        @rtype : instance
        @return : instance of Categorie object will some specific parameters
                    depending of the needs of the studio.
        """
        return Categorie(sName)

class Cinesite(Studio):
    """
    Redefinition of Studio class according to Cinesite inputs.
    """
    name = "Cinesite"

    LIST_CHARACTER_USING_DIFFERENT_TYPES = [ ]

    LIST_CATEGORIES = [["BODY"]
                      ]

    def __init__(self, sRootFolder):
        """
        @type sRootFolder : string
        @param sRootFolder : Path to the folder where the script start from.
        """
        Studio.__init__(self, sRootFolder)

    def createCategorie(self, sName=""):
        """
        Creation of a categorie instance.
        The type of categorie depends on the studio.

        @type sName : string
        @param sName : Name of the categorie.

        @rtype : instance
        @return : instance of Categorie object will some specific parameters
                    depending of the needs of the studio.
        """
        return CinesiteCategorie(sName)

class Dneg(Studio):
    """
    Redefinition of Studio class according to Dneg inputs.
    """
    name = "Dneg"

    LIST_CHARACTER_USING_DIFFERENT_TYPES = [["Woola"], ]

    LIST_CATEGORIES = [["BODY"],
                      ["COSTUME", ["setCommandParameters(14)"]],
                      ["PROPS", ["setCommandParameters(-3,-4)"]],
                      ]

    def __init__(self, sRootFolder):
        """
        @type sRootFolder : string
        @param sRootFolder : Path to the folder where the script start from.
        """
        Studio.__init__(self, sRootFolder)

    def createCategorie(self, sName=""):
        """
        Creation of a categorie instance.
        The type of categorie depends on the studio.

        @type sName : string
        @param sName : Name of the categorie.

        @rtype : instance
        @return : instance of Categorie object will some specific parameters
                    depending of the needs of the studio.
        """
        return DnegCategorie(sName)

class TextureRenamer:
    """
    Class to rename files coming from another studio.
    Used for jcom show.
    """
    # List of formats of files the script will consider.
    LIST_FILE_FORMATS = [".tif"]

    # self.dictFiles[Folder] = [list of files in this folder].
    dictFiles = {}

    def setFileList(self, sFolder):
        """
        Recursive method to set the list of files that the script will consider.
        It returns nothing, but it feed self.dictFiles dictionary as :
            self.dictFiles[Folder] = [list of files in this folder].

        @type sFolder : string
        @param sFolder : Path to a folder where files will be searched in.
        """
        for path, listDirs, listFiles in os.walk(sFolder):

            if not path in self.dictFiles.keys():
                self.dictFiles[path] = []

            for sFile in listFiles:

                if not sFile in self.dictFiles[path]:
                    self.dictFiles[path].append(sFile)

            # Going further.
            # To infinite and beyond !
            for sDir in listDirs :
                fullPath = os.path.join(path, sDir)
                self.setFileList(fullPath)

    def __init__(self, sStudio="", sRootFolder=""):
        """
        @type sStudio = string.
        @param sStudio = Studio where textures come from.

        @type sRootFolder = string.
        @param sRootFolder = Where textures are.
        """
        # Formating the sStudio string, just in case.
        sStudio = "%s%s" %(sStudio[0].upper(), sStudio[1:].lower())

        # Dynamic setting of the studio object.
        oStudio = eval("%s('%s')" %(sStudio, sRootFolder))

        # Listing of characters that are not using the regular dictionary of types.
        # The index of the list is used to set dynamicly the new dictionary.
        #LIST_CHARACTER_USING_DIFFERENT_TYPES = oStudio.LIST_CATEGORIES

        self.MPC_TEXTURE_FOLDER = "%s_MPC" %oStudio.TEXTURE_FOLDER

        # Here is the main loop.
        for sFolder in os.listdir(sRootFolder):

            sFolder = os.path.join(sRootFolder, sFolder)

            if os.path.isdir(sFolder):
                listFolders = os.listdir(sFolder)

                # Checking is oStudio.TEXTURE_FOLDER is in the path.
                # If it is, create the MPC folder at where the studio folder lives.
                if oStudio.TEXTURE_FOLDER in listFolders:
                    sTextureFolder = os.path.join(sFolder, oStudio.TEXTURE_FOLDER)
                    sMpcTextureFolder = os.path.join(sFolder, self.MPC_TEXTURE_FOLDER)

                    if not os.path.exists(sMpcTextureFolder):
                        os.mkdir(sMpcTextureFolder)

                    # Goes in the studio folder (sTextureFolder) to find every pictures
                    # in it or in subfolders. Then rename each one and copy directly
                    # in the MPC folder (sMpcTextureFolder) without creating any subfolder.

                    self.setFileList(sTextureFolder)

                    for key, listFiles in self.dictFiles.items():

                        for sFilename  in listFiles :
                            # We only care about some kind of files.
                            sExt = os.path.splitext(sFilename)[1]

                            if sExt in self.LIST_FILE_FORMATS:

                                for oCategorie in oStudio.listCategories:

                                    # Setting of the object.
                                    if oCategorie.name in key :
                                        oCategorie.setPath(key)

                                        oCategorie.addStudioFile(sFilename)
                                        oCategorie.addMpcFile(sFilename)

                                        oCategorie.setStudioFolder(sTextureFolder)
                                        oCategorie.setMpcFolder(sMpcTextureFolder)

                                        # Settin of the command.
                                        cmd = "cp "
                                        cmd += oCategorie.sPath
                                        cmd += os.sep
                                        cmd += sFilename
                                        cmd += " "
                                        cmd += oCategorie.mpcFolder
                                        cmd += os.sep
                                        cmd += oCategorie.mpcFilename
                                        print cmd
                                        #os.system(cmd)


        # Writing files to keep the connection between studio files and
        # the new created files.
        # Upon request of artists.
        for oCategorie in oStudio.listCategories:
            listStudio = []
            listMpc = []

            if len(oCategorie.listStudioFiles) > 0 :

                for studioFile in oCategorie.listStudioFiles:

                    mpcFile = oCategorie.findMpcFileFromStudioFile(studioFile)
                    listStudio.append('%-90s%-40s\r' %(studioFile, mpcFile))
                    listMpc.append('%-60s%-40s\r' %(mpcFile, studioFile))

                sFile = "%s/%s2mpc.txt" %(oCategorie.studioFolder, oStudio.name.lower())
                listStudio.sort()
                open(sFile, "w").writelines(listStudio)

                listMpc.sort()
                sFile = "%s/mpc2%s.txt" %(oCategorie.mpcFolder, oStudio.name.lower())
                open(sFile, "w").writelines(listMpc)



















