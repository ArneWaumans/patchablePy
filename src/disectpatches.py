import os
import math
from copy import deepcopy

def GetPatchComps(patchfile: str):
    """
    disects a patchfile into its component parts
    """
    patchfileDir = os.getcwd() + "/patches/"
    
    componentData = []

    with open(patchfileDir + patchfile, "r") as patch:
        currentData = {
            "patchname": patchfile,
            "filename": "",
            "place": 0,
            "configlines": [0, 0],
            "codelines": [0, 0]
        }

        lineNumber = 1
        firstcommit = True
        prevdiffcount = 0

        for line in patch:

            if "diff --git" in line:
                prevdiffcount = 0

                if not firstcommit:
                    currentData["codelines"][1] = lineNumber - 1
                    componentData.append(deepcopy(currentData))
                
                firstcommit = False

                currentData["filename"] = line.split(" ")[2].split("/")[1]
                currentData["configlines"][0] = lineNumber
                currentData["configlines"][1] = lineNumber + 3

            elif "@@" in line:
                prevdiffcount += 1

                if prevdiffcount > 1:
                    currentData["codelines"][1] = lineNumber - 1
                    componentData.append(deepcopy(currentData))

                currentData["place"] = math.floor(float(line.split(" ")[1].replace('-', '').replace(',', '.')))
                currentData["codelines"][0] = lineNumber

            lineNumber += 1

        else:
            currentData["codelines"][1] = lineNumber - 1
            componentData.append(deepcopy(currentData))

    return componentData

def CreatePatchFiles(patchFiles):
    currentPath = os.getcwd() + "/patches/"
    destPath = os.getcwd() + "/patchcomps/"
    
    allCompList = []
    destFiles = []
    for patchfile in patchFiles:
        currentPatchComps = GetPatchComps(patchfile)
        
        for patch in currentPatchComps:
            allCompList.append(deepcopy(patch))
            if not any(patch["filename"] in x for x in destFiles):
                destFiles.append(patch["filename"])
    
    allOrderedCompList = []
    for destFile in destFiles:
        currentDestFileList = []

        for comp in allCompList:
            if comp["filename"] == destFile:
                currentDestFileList.append(deepcopy(comp))

        currentDestFileList.sort(key=lambda item: item.get("place"))
        for comp in currentDestFileList:
            allOrderedCompList.append(deepcopy(comp))

    patchCounter = 1
    for comp in reversed(allOrderedCompList):
        fromFile = open(currentPath + comp["patchname"], "r")
        destFile = open(destPath + str(patchCounter) + "-" + comp["filename"] + ".diff", "w")
        
        lineCounter = 0
        writeLines = []
        for line in fromFile:
            lineCounter += 1
            if (    (lineCounter >= comp["configlines"][0] and lineCounter <= comp["configlines"][1]) or
                    (lineCounter >= comp["codelines"][0]   and lineCounter <= comp["codelines"][1])):
                writeLines.append(line)
        destFile.writelines(writeLines)
 
        fromFile.close()
        destFile.close()

        print(str(patchCounter) + "-" + comp["filename"] + ".diff" + " has been created")

        patchCounter += 1
