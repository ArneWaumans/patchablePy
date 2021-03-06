import os
import re
from pprint import pprint

def atoi(text):
    return int(text) if text.isdigit() else -1

def numkeys(text):
    return [atoi(c) for c in re.split('(\d+)', text)]

def cleanup():
    cleanupYN = input("Do you want to remove the patchcomps? [Y/n]? ")
    if (cleanupYN.lower() == 'y'):
        print("cleaning patchcomps...")
        os.system("rm -r ./patchcomps")

def ApplyPatches():
    patchCompDir = os.listdir(os.getcwd() + "/patchcomps")

    patchComps = [patchComp for patchComp in patchCompDir]
    patchComps.sort(key=numkeys)

    for patchComp in patchComps:
        os.system("git apply {}".format("./patchcomps/" + patchComp))
        print("git apply {}".format("./patchcomps/" + patchComp))

    cleanup()
