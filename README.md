# Patchable

Patchable is a python script that attempts to make patching suckless software a bit more suckless. It does this by disecting the patch files, creating component patch files, and applying those component patch files from the bottom to the top for every source file.

## Installation

You can download the repository with git clone.
```bash
git clone https://github.com/ArneWaumans/patchable.git
```

## Build 

to build the project, you need to have [pip](https://pypi.org/project/pip/) installed. With pip you have to install [pyinstaller](https://pypi.org/project/pyinstaller/).
```bash
pip install pyinstaller
```
After that, simply run the build.sh script and the executable will be located in the /dist folder.

## Usage
cd into your suckless install and add a /patches folder. this is the folder where you have to place your .diff files. After that, just run the program and the patches will be applied automatically.

E.g.
```bash
./patchable
```

## License
[GPL-v3.0](https://choosealicense.com/licenses/gpl-3.0/)
