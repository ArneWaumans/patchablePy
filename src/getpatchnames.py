import os

def GetPatchNames(patchNames: list) -> list[str]:
    patchDir = os.path.dirname(os.getcwd()) + "/patches/";
    patchFiles = []

    for pfs in os.listdir(patchDir):
        match = False

        for patchName in patchNames:
            if pfs.startswith(patchName):
                match = True

        if match and os.path.isfile(patchDir + pfs):
            patchFiles.append(pfs);

    return patchFiles
