from pprint import pprint
import os

from getpatchnames import GetPatchNames
from disectpatches import CreatePatchFiles
from applypatches import ApplyPatches

def setupfolders():
    os.mkdir(os.path.join(os.getcwd(), "patchcomps"))

def main():
    patchnames = GetPatchNames()
    setupfolders()
    CreatePatchFiles(patchnames)
    ApplyPatches()

if __name__ == "__main__":
    main()
