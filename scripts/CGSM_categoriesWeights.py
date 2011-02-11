#!/usr/bin/python

global gTotalPoint

gTotalPoint = 5



def findCategorie(sValue):
    dict = {}

    dict["artist"] = int(sValue[0])
    dict["dev"] = int(sValue[1])
    dict["prod"] = int(sValue[2])

    minorType = ""
    multiType = ""
    for key, value in dict.items() :
        fullvalue = 0
        if value == gTotalPoint :
            return key

        for subkey, subvalue in dict.items():
            if not subkey == key :
                fullvalue += subvalue

                if value + subvalue >= gTotalPoint and subvalue >= round(gTotalPoint/2):
                    minorType = subkey

                if subvalue == value :
                    multiType = "%s+%s" %(key, subkey)

        if fullvalue < value :
            output = key
            if minorType != "" and minorType != key :
                output += " (Minor : %s)" %minorType
            return output

    return multiType

#findCategorie("410")
dictGeneralProductionProfile = {
    "Artist":"200",
    "Dev":"020",
    "Prod":"002",
    "ArtistDev":"110",
    "ArtistProd":"101",
    "DevProd":"011"
    }

dictProductionProfile = {
    "Animation":dictGeneralProductionProfile["Artist"],
    "Character":dictGeneralProductionProfile["ArtistDev"],
    "Compositing":dictGeneralProductionProfile["Artist"],
    "Concept":dictGeneralProductionProfile["Artist"],
    "Environment":dictGeneralProductionProfile["Artist"],
    "FX":dictGeneralProductionProfile["Artist"],
    "Game":dictGeneralProductionProfile["Artist"],
    "Generalist":dictGeneralProductionProfile["ArtistDev"],
    "Interface":dictGeneralProductionProfile["ArtistDev"],
    "Layout":dictGeneralProductionProfile["Artist"],
    "Level":dictGeneralProductionProfile["ArtistDev"],
    "Lighting":dictGeneralProductionProfile["Artist"],
    "Matchmoving":dictGeneralProductionProfile["Artist"],
    "Modeling":dictGeneralProductionProfile["Artist"],
    "Motion Capture":dictGeneralProductionProfile["Artist"],
    "Pipeline":dictGeneralProductionProfile["Dev"],
    "Pre-Vis":dictGeneralProductionProfile["Artist"],
    "Production":dictGeneralProductionProfile["Prod"],
    #"RenderWrangler":dictGeneralProductionProfile["Dev"],
    "Rendering":dictGeneralProductionProfile["Dev"],
    "Rigging":dictGeneralProductionProfile["ArtistDev"],
    "Data":dictGeneralProductionProfile["Dev"],
    "Rotoscoping":dictGeneralProductionProfile["Artist"],
    "Shading":dictGeneralProductionProfile["Artist"],
    "Shader":dictGeneralProductionProfile["Dev"],
    "Story Board":dictGeneralProductionProfile["ArtistProd"],
    "Texturing":dictGeneralProductionProfile["Artist"],
    "Fur":dictGeneralProductionProfile["Artist"],
    "Cloth":dictGeneralProductionProfile["Artist"],
    "Graphic":dictGeneralProductionProfile["Artist"],
    "Software":dictGeneralProductionProfile["Dev"],
    "Sound":dictGeneralProductionProfile["Artist"],
    "Web":dictGeneralProductionProfile["ArtistDev"],
    "OpenGL":dictGeneralProductionProfile["Dev"],
    "RnD":dictGeneralProductionProfile["Dev"],
    "Executive":dictGeneralProductionProfile["Prod"],
    "VFX":dictGeneralProductionProfile["ArtistProd"],
    "Line":dictGeneralProductionProfile["Prod"],
    "Human Ressources":dictGeneralProductionProfile["Prod"],
    "Recruitment":dictGeneralProductionProfile["ArtistProd"],
    "Crew":dictGeneralProductionProfile["ArtistProd"],
    "Runner":dictGeneralProductionProfile["ArtistProd"],
    "Visual Development":dictGeneralProductionProfile["Artist"],
    "Digital Matte Painting":dictGeneralProductionProfile["Artist"],
    "System":dictGeneralProductionProfile["Dev"],
    "Database":dictGeneralProductionProfile["Dev"],
    "Technology":dictGeneralProductionProfile["Dev"],
    }

dictTypeProfiles = {
    "Artist":"300",
    "Technical Director":"120",
    "Director":"003",
    "Head of Department":"003",
    "Manager":"003",
    "Supervisor":"003",
    "Technical Artist":"120",
    "Assistant TD":"120",
    "Menthor":"210",
    "Professor":"210",
    "Engineer":"030",
    "Developer":"030",
    "Assistant":"003",
    "Coordinator":"003",
    "Producer":"003",
    "Writer":"201",
    "Designer":"300",
    }

dictCategories = {}

#for dpKey in sorted(dictTypeProfiles.keys()) :
    #dpValue = dictTypeProfiles[dpKey]
    #for tpKey in sorted(dictProductionProfile.keys()) :
        #tpValue = dictProductionProfile[tpKey]
for dpKey in sorted(dictProductionProfile.keys()) :
    dpValue = dictProductionProfile[dpKey]
    for tpKey in sorted(dictTypeProfiles.keys()) :
        tpValue = dictTypeProfiles[tpKey]
        fullname = "%s %s" %(dpKey, tpKey)
        fullvalue = "%03d" %(int(dpValue)+int(tpValue))
        #categorie = "%s %s" %(findCategorie(fullvalue),fullvalue)
        categorie = findCategorie(fullvalue)

        print "%-40s %05s %s" %(fullname, fullvalue, categorie)

        if not categorie in dictCategories.keys():
            dictCategories[categorie] = []

        dictCategories[categorie].append(fullname)

    #print ""


#for key in sorted(dictCategories.iterkeys()):
    #list = dictCategories[key]
    #list.sort()
    #print key, len(list)
    #for i in list :
        #print "\t", i
    #print ""


