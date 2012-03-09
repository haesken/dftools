#!/usr/bin/env bash

DF_WORK_DIR=$1

echo "Backing up objects dir."
cp -r $DF_WORK_DIR/dwarffortress/df_linux/raw/objects/ $DF_WORK_DIR/dwarffortress/df_linux/raw/objects_bak/

for i in $DF_WORK_DIR/dwarffortress/df_linux/raw/objects/*.txt; do
    sed -i 's/\[AQUIFER\]//g' $i
done
echo "Aquifers removed, generate a new world."
