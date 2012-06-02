#!/usr/bin/env bash

rm -r develop/build/dist/
python develop/pyinstaller/utils/Build.py develop/build/df_install.spec
python develop/pyinstaller/utils/Build.py develop/build/init_editor.spec

mkdir -p build/dwarf_fortress_auto

cp develop/build/dist/* build/dwarf_fortress_auto
cp -r custom build/dwarf_fortress_auto

rm *.tar.gz
cd build
tar cvzf dwarf_fortress_auto-$(git log --pretty=format:'%h' -n 1).tar.gz dwarf_fortress_auto/
