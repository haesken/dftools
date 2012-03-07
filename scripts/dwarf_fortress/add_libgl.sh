#!/usr/bin/env bash

# Copy the libgl library to the Dwarf Fortress libs dir.
libgl_path=$(find /usr/{lib,lib32} -iname libgl.so.1 | egrep -v "64|nvidia" | grep mesa)

if [ ! -d df_linux/libs ]; then
    mkdir df_linux/libs
fi

cp $libgl_path df_linux/libs/
echo "Copied: $libgl_path to df_linux/libs"
