#!/usr/bin/env bash

DF_WORK_DIR=$1

echo 'Installing Phoebus tileset.'

cd $DF_WORK_DIR/dwarffortress/

    if [ ! -d 'phoebus' ]; then
        mkdir phoebus
    fi
    cd phoebus
        if [ ! -f 'Phoebus.zip' ]; then
            python $DF_WORK_DIR/scripts/dwarf_fortress/download.py -dph
        else
            echo "Phoebus.zip found, not downloading."
        fi

        if [ ! -d data ]; then
            unzip Phoebus.zip
        else
            echo "Found data/, not extracting Phoebus.zip"
        fi

        if [ -d data ]; then
            cp -r data/* $DF_WORK_DIR/dwarffortress/df_linux/data/
            cp -r $DF_WORK_DIR/dwarffortress/df_linux/data/init/phoebus/* $DF_WORK_DIR/dwarffortress/df_linux/data/init/
            echo "Phoebus tileset installed."
        fi
