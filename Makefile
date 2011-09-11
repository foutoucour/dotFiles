include ${MPCMAKE_PATH}/latest/MakeMayaModule
include ${MPCMAKE_INC}/MakeCopy
include ${MPCMAKE_INC}/MakeConfig
include ${MPCMAKE_INC}/MakePythonPackage

VERSION = 0.0.0

######################################################
# COMMON PART
######################################################
MODULE 		= nukeSee
AUTHORS 	= charles-c jordi-r
MAILTO 		= charles-c
DESCRIPTION = gizmo to make a relighting in Nuke and to communicate changes in Maya

PLATFORMS   = linux.centos5.x86_64
PLATFORM    = ${UNAME}.${DIST}.${SARCH}

######################################################
# DEFINITONS
######################################################
MAYA_MAJOR_VERSION          = 2011
MAYA_VERSION                = 2011.5
MAYA_MODULE_LOADER_VERSION  = 3.0
PYTHON_VERSION              = 2.6.4
NUKE_VERSIONS 				= 6.3v1


##################################################################
# Python.
##################################################################
python.PYTHON_ROOT 	= python
python.SOURCES 		= ${call GetFiles,python,py}

${call MakePythonPackage,python}

