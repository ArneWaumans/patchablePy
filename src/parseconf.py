import json

def ParsePatches(path: str) -> dict:
    patches = dict()
    with open(path, "r") as patchfile:
        patches = json.loads(patchfile.read())
    return patches
