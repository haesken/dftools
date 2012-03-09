#!/usr/bin/env bash

echo '----------------------------------------'
echo $0
echo $1
echo '----------------------------------------'

# Copy the libgl library to the Dwarf Fortress libs dir.
libgl_path=$(find /usr/{lib,lib32} -iname libgl.so.1 | egrep -v "64|nvidia" | grep mesa)
df_libs_path="$1/dwarffortress/df_linux/libs/"
echo $df_libs_path

cp $libgl_path $df_libs_path
echo "Copied: $libgl_path to $df_libs_path"
