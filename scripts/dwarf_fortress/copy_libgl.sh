#!/usr/bin/env bash

DF_WORK_DIR=$1

# Copy the libgl library to the Dwarf Fortress libs dir.
libgl_path=$(find /usr/{lib,lib32} -iname libgl.so.1 | egrep -v "64|nvidia" | grep mesa)
df_libs_path="$DF_WORK_DIR/df_linux/libs/"

if [ ! -d $df_libs_path ]; then
    mkdir -p $df_libs_path
fi

cp $libgl_path $df_libs_path
echo "Copied: $libgl_path to $df_libs_path"
