#!/usr/bin/env bash

rm -r develop/dist/
python develop/pyinstaller/utils/Build.py develop/df_install_windows.spec
python develop/pyinstaller/utils/Build.py develop/init_editor_windows.spec

mkdir -p binaries/dwarf_fortress_auto

cp develop/dist/* binaries/dwarf_fortress_auto
cp -r custom binaries/dwarf_fortress_auto

rm binaries/*.tar.gz
rm binaries/dwarf_fortress_auto/{df_install,init_editor}
tar cvzf dwarf_fortress_auto-$(git log --pretty=format:'%h' -n 1)-windows.tar.gz dwarf_fortress_auto/
