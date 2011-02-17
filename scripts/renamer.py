#!/usr/bin/env mpcpython


import os
import glob

import sys
sCurrentFolder = os.path.dirname( os.path.realpath( __file__ ) )

for sPath in glob.glob('%s/*tif' %sCurrentFolder):
    sDir, sFile = os.path.split(sPath)
    splitFile = sFile.split('.')

    sNewFile = '%s.%s.%s' %(splitFile[1], splitFile[0], splitFile[2])

    os.system("mv %s %s" %(sFile, sNewFile))


