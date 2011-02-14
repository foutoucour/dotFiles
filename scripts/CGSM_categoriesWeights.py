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
    "gArtist":"200",
    "gDev":"020",
    "gProd":"002",
    "gArtistDev":"110",
    "gArtistProd":"101",
    "gDevProd":"011",
    }

dictProductionProfile = {
    "Animation":dictGeneralProductionProfile["gArtist"],
    "Character":dictGeneralProductionProfile["gArtistDev"],
    "Compositing":dictGeneralProductionProfile["gArtist"],
    "Concept":dictGeneralProductionProfile["gArtist"],
    "Environment":dictGeneralProductionProfile["gArtist"],
    "FX":dictGeneralProductionProfile["gArtist"],
    "Game":dictGeneralProductionProfile["gArtist"],
    "Generalist":dictGeneralProductionProfile["gArtistDev"],
    "Interface":dictGeneralProductionProfile["gArtistDev"],
    "Layout":dictGeneralProductionProfile["gArtist"],
    "Level":dictGeneralProductionProfile["gArtistDev"],
    "Lighting":dictGeneralProductionProfile["gArtist"],
    "Matchmoving":dictGeneralProductionProfile["gArtist"],
    "Modeling":dictGeneralProductionProfile["gArtist"],
    "Motion Capture":dictGeneralProductionProfile["gArtist"],
    "Pipeline":dictGeneralProductionProfile["gDev"],
    "Pre-Vis":dictGeneralProductionProfile["gArtist"],
    "Production":dictGeneralProductionProfile["gProd"],
    #"RenderWrangler":dictGeneralProductionProfile["gDev"],
    "Rendering":dictGeneralProductionProfile["gDev"],
    "Rigging":dictGeneralProductionProfile["gArtistDev"],
    "Data":dictGeneralProductionProfile["gDev"],
    "Rotoscoping":dictGeneralProductionProfile["gArtist"],
    #"Shading":dictGeneralProductionProfile["gArtist"],
    "Shader":dictGeneralProductionProfile["gDev"],
    "Story Board":dictGeneralProductionProfile["gArtistProd"],
    "Texturing":dictGeneralProductionProfile["gArtist"],
    "Fur":dictGeneralProductionProfile["gArtist"],
    "Cloth":dictGeneralProductionProfile["gArtist"],
    "Graphic":dictGeneralProductionProfile["gArtist"],
    "Software":dictGeneralProductionProfile["gDev"],
    "Sound":dictGeneralProductionProfile["gArtist"],
    "Web":dictGeneralProductionProfile["gArtistDev"],
    "OpenGL":dictGeneralProductionProfile["gDev"],
    "RnD":dictGeneralProductionProfile["gDev"],
    "Executive":dictGeneralProductionProfile["gProd"],
    "VFX":dictGeneralProductionProfile["gArtistProd"],
    "Line":dictGeneralProductionProfile["gProd"],
    "Human Ressources":dictGeneralProductionProfile["gProd"],
    "Recruitment":dictGeneralProductionProfile["gArtistProd"],
    "Crew":dictGeneralProductionProfile["gArtistProd"],
    "Runner":dictGeneralProductionProfile["gArtistProd"],
    "Visual Development":dictGeneralProductionProfile["gArtist"],
    "Digital Matte Painting":dictGeneralProductionProfile["gArtist"],
    "System":dictGeneralProductionProfile["gDev"],
    "Database":dictGeneralProductionProfile["gDev"],
    "Technology":dictGeneralProductionProfile["gDev"],
    }

dictGeneralTypeProfiles = {
    "tArtist":"300",
    "tDeveloper":"030",
    "tProd":"003",
    "tTeacher":"210",
    "tTechnical Director":"120",
    "tWriter":"201",
    }


dictTypeProfiles = {
    "Artist":dictGeneralTypeProfiles["tArtist"],
    "Technical Director":dictGeneralTypeProfiles["tTechnical Director"],
    "Director":dictGeneralTypeProfiles["tProd"],
    "Head of Department":dictGeneralTypeProfiles["tProd"],
    "Manager":dictGeneralTypeProfiles["tProd"],
    "Supervisor":dictGeneralTypeProfiles["tProd"],
    "Technical Artist":dictGeneralTypeProfiles["tTechnical Director"],
    "Assistant TD":dictGeneralTypeProfiles["tTechnical Director"],
    "Teacher":dictGeneralTypeProfiles["tTeacher"],
    "Engineer":dictGeneralTypeProfiles["tDeveloper"],
    "Developer":dictGeneralTypeProfiles["tDeveloper"],
    "Assistant":dictGeneralTypeProfiles["tProd"],
    "Coordinator":dictGeneralTypeProfiles["tProd"],
    "Producer":dictGeneralTypeProfiles["tProd"],
    "Writer":dictGeneralTypeProfiles["tWriter"],
    "Designer":dictGeneralTypeProfiles["tArtist"],
    }

dictCategories = {}

#for dpKey in sorted(dictTypeProfiles.keys()) :
    #dpValue = dictTypeProfiles[dpKey]
    #for tpKey in sorted(dictProductionProfile.keys()) :
        #tpValue = dictProductionProfile[tpKey]
#for dpKey in sorted(dictGeneralProductionProfile.keys()) :
    #dpValue = dictGeneralProductionProfile[dpKey]
    #for tpKey in sorted(dictGeneralTypeProfiles.keys()) :
        #tpValue = dictGeneralTypeProfiles[tpKey]
        #fullname = "%s %s" %(dpKey, tpKey)
        #fullvalue = "%03d" %(int(dpValue)+int(tpValue))
        ##categorie = "%s %s" %(findCategorie(fullvalue),fullvalue)
        #categorie = findCategorie(fullvalue)

        ##print "%-40s %05s %s" %(fullname, fullvalue, categorie)

        #if not categorie in dictCategories.keys():
            #dictCategories[categorie] = []

        #dictCategories[categorie].append(fullname)

    #print ""


#for key in sorted(dictCategories.iterkeys()):
    #list = dictCategories[key]
    #list.sort()
    #print key, len(list)
    #for i in list :
        #print "\t", i
    #print ""



for key in sorted(dictTypeProfiles.iterkeys()):
    print key

