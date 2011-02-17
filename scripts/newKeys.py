#!/usr/bin/env mpcpython

import os
import glob

import sys
sCurrentFolder = os.getcwd()


dictKey = {
"BMP":"BUMP",
"DSPbump":"DISP1",
"DSPcreases":"DISP2",
"DSPfold":"DISP3",
"DSPgrooves":"DISP4",
"DSPlaceHoles":"DISP5",
"DSPlaceJoin":"DISP6",
"DSPlaces":"DISP7",
"DSPlarge":"DISP8",
"DSPmedium":"DISP9",
"DSPsmall":"DISP10",
"ISOborder":"ISO",
"ISObottomStrap":"ISO2",
"ISObrightAreas":"ISO3",
"ISOdirt":"ISO4",
"ISOgrooves":"ISO5",
"ISOlacing":"ISO6",
"ISOleatherScrapes":"ISO7",
"ISOseams":"ISO8",
"ISOstitching":"ISO9",
"ISOtopStrap":"ISO10",
"ISOwoodChips":"ISO11",
"SPC1":"SPEC2",
"SPC2":"SPEC3",
"SPC3":"SPEC4",
"SPEC1":"SPEC5",
"SPEC2":"SPEC6 ",
}

for sPath in glob.glob('%s/*tif' %sCurrentFolder):
    sDir, sFile = os.path.split(sPath)
    preSplit = sFile.split('.')[0]
    splitFile = preSplit.split('_')

    for split in splitFile :
        for key, value in dictKey.items():
            if split == key:
                newFile = sFile.replace(split, value)

                print sFile, newFile

                os.system("mv %s %s" %(sFile, newFile))










