#!/usr/bin/env bash

rm -r binaries/
rm -r develop/dist/
rm -r develop/build/

python develop/pyinstaller/utils/Build.py develop/df_install.spec
python develop/pyinstaller/utils/Build.py develop/init_editor.spec

mkdir -p binaries/dwarf_fortress_auto
cp develop/dist/* binaries/dwarf_fortress_auto
cp -r custom binaries/dwarf_fortress_auto

rm binaries/dwarf_fortress_auto/{df_install.exe,init_editor.exe}
cd binaries
tar cvzf dwarf_fortress_auto-$(git log --pretty=format:'%h' -n 1)-linux.tar.gz dwarf_fortress_auto/
