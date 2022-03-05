from pprint import pprint

from getpatchnames import GetPatchNames
from disectpatches import CreatePatchFiles
from applypatches import ApplyPatches

def main():
    patchnames = GetPatchNames()
    CreatePatchFiles(patchnames)
    ApplyPatches()

if __name__ == "__main__":
    main()
