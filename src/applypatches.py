import os
import re
from pprint import pprint

def atoi(text):
    return int(text) if text.isdigit() else -1

def numkeys(text):
    return [atoi(c) for c in re.split('(\d+)', text)]

def ApplyPatches():
    patchCompDir = os.listdir(os.path.dirname(os.getcwd()) + "/patchcomps")

    patchComps = [patchComp for patchComp in patchCompDir]
    patchComps.sort(key=numkeys)
    pprint(patchComps)

    os.chdir("../modst")

    for patchComp in patchComps:
        os.system("git apply {}".format("../patchcomps/" + patchComp))
