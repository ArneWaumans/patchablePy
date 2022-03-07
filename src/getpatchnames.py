import os

def GetPatchNames():
    patchDir = os.getcwd() + "/patches/";
    patchFiles = []

    for pfs in os.listdir(patchDir):
        patchFiles.append(pfs);

    return patchFiles
