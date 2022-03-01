from parseconf import ParsePatches

def main():
    patchDict = ParsePatches("config.json")['patches'] 
    print(patchDict) 

if __name__ == "__main__":
    main()
