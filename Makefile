SHELL = /bin/sh

PREFIX  = /usr/local

build:
	pyinstaller --onefile -n patchable ./src/__main__.py

install:
	mkdir -p $(PREFIX)/bin
	cp -f ./dist/patchable $(PREFIX)/bin
	chmod 755 $(PREFIX)/bin/patchable

uninstall:
	rm $(PREFIX)/bin/patchable

clean:
  rm -rf build
  rm -rf dist
  rm patchable.spec