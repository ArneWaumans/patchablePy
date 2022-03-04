from pprint import pprint

from parseconf import ParsePatches
from getpatchnames import GetPatchNames
from disectpatches import CreatePatchFiles
from applypatches import ApplyPatches

def main():
    patchlist = [list(patch.values())[0] for patch in ParsePatches("config.json")['patches']]
    patchnames = GetPatchNames(patchlist)
    CreatePatchFiles(patchnames)
    ApplyPatches()

if __name__ == "__main__":
    main()
