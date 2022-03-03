from pprint import pprint

from parseconf import ParsePatches

from getpatchnames import GetPatchNames

from disectpatches import CreatePatchFiles

def main():
    patchlist = [list(patch.values())[0] for patch in ParsePatches("config.json")['patches']]
    patchnames = GetPatchNames(patchlist)
    CreatePatchFiles(patchnames)

if __name__ == "__main__":
    main()
