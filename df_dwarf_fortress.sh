#!/usr/bin/env bash

# Install dependencies
sudo puppet apply depends_df.pp

# Create the dir if it doesn't exist.
if [ ! -d dwarffortress ]; then
    mkdir dwarffortress
fi
cd dwarffortress

# Grab a copy of Dwarf Fortress with the Phoebus tileset and extract it.
if [ ! -f DF_Phoebus.tar.gz ]; then
    wget 'http://dffd.wimbli.com/download.php?id=2944&f=DF_Phoebus_34_02v01_Linux.tar.gz' -O DF_Phoebus.tar.gz
fi
tar -xf DF_Phoebus.tar.gz

# Copy the libgl library to the Dwarf Fortress dir.
cp $(find /usr/lib -iname libgl.so.1 | grep i386) df_linux/libs/
