#!/usr/bin/env bash

rm -r develop/build/dist/
python develop/pyinstaller/utils/Build.py develop/df_install.spec
python develop/pyinstaller/utils/Build.py develop/init_editor.spec

mkdir -p binaries/dwarf_fortress_auto

cp develop/dist/* binaries/dwarf_fortress_auto
cp -r custom binaries/dwarf_fortress_auto

cd binaries
rm *.tar.gz
tar cvzf dwarf_fortress_auto-$(git log --pretty=format:'%h' -n 1)-linux.tar.gz dwarf_fortress_auto/
