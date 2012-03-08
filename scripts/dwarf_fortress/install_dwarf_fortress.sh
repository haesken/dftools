#!/usr/bin/env bash

DF_WORK_DIR=$1
echo -n 'DF_WORK_DIR: '
echo $DF_WORK_DIR

# Install dependencies
echo "Installing dependencies..."
sudo puppet apply $DF_WORK_DIR/scripts/dwarf_fortress/depends.pp

if [ ! -d dwarffortress ]; then
    mkdir dwarffortress
fi

cd dwarffortress

    # Download Dwarf Fortress
    if [ ! -f 'Dwarf_Fortress.tar.bz2' ]; then
        python $DF_WORK_DIR/scripts/dwarf_fortress/download.py -ddf
    else
        echo 'Found Dwarf_Fortress.tar.bz2 in dwarffortress/, not downloading.'
    fi

    # Extract Dwarf Fortress
    if [ ! -d 'df_linux' ]; then
        df_filename='Dwarf_Fortress.tar.bz2'
        echo "Extracting '$df_filename'"
        tar -xf $df_filename
    else
        echo 'Found df_linux in dwarffortress/, not overwriting.'
    fi

    # Install libgl library.
    if [ ! -f 'df_linux/libs/libGL.so.1' ]; then
        bash $DF_WORK_DIR/scripts/dwarf_fortress/copy_libgl.sh
    else
        echo 'Found libgl.so.1 in df_linux/libs/, not overwriting.'
    fi
