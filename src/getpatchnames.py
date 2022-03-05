import os

def GetPatchNames() -> list[str]:
    patchDir = os.getcwd() + "/patches/";
    patchFiles = []

    for pfs in os.listdir(patchDir):
        patchFiles.append(pfs);

    return patchFiles
