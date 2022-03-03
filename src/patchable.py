import pprint

from parseconf import ParsePatches

from getpatchnames import GetPatchNames

from disectpatches import GetPatchCode

def main():
    patchlist = [list(patch.values())[0] for patch in ParsePatches("config.json")['patches']]
    patchnames = GetPatchNames(patchlist)
    GetPatchCode(patchnames[2]) # testing function

if __name__ == "__main__":
    main()
