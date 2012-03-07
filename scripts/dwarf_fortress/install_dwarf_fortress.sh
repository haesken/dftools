#!/usr/bin/env bash

# Dwarf Fortress

# Install dependencies
sudo puppet apply depends_df.pp

# Create the dir if it doesn't exist.
if [ ! -d dwarffortress ]; then
    mkdir dwarffortress
fi
cd dwarffortress

# Grab a copy of Dwarf Fortress with the Phoebus tileset and extract it.
# if [ ! -f DF_Phoebus.tar.gz ]; then
#     wget $1 -O DF_Phoebus.tar.gz
# fi
# tar -xf DF_Phoebus.tar.gz

bash add_libgl.sh
