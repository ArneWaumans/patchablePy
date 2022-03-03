import os
import math
from pprint import pprint

def GetPatchCode(patchfile: str) -> list[dict]:
    """
    disects a patchfile into its component parts
    """
    patchfileDir = os.path.dirname(os.getcwd()) + "/patches/"
    
    componentData = []

    with open(patchfileDir + patchfile, "r") as patch:
        currentData = {
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
                    componentData.append(currentData.copy())
                    pprint(currentData)
                
                firstcommit = False

                currentData["filename"] = line.split(" ")[2].split("/")[1]
                currentData["configlines"][0] = lineNumber
                currentData["configlines"][1] = lineNumber + 3

            elif "@@" in line:
                prevdiffcount += 1

                if prevdiffcount > 1:
                    currentData["codelines"][1] = lineNumber - 1
                    componentData.append(currentData.copy())
                    pprint(currentData)

                currentData["place"] = math.floor(float(line.split(" ")[1].replace('-', '').replace(',', '.')))
                currentData["codelines"][0] = lineNumber

            lineNumber += 1
        else:
            currentData["codelines"][1] = lineNumber - 1
            componentData.append(currentData.copy())
            pprint(currentData)

    return componentData

def CreatePatchFiles(componentFiles: list[str]):
    pass
