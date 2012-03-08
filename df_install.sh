#!/usr/bin/env bash

# DF_WORK_DIR=$PWD

bash scripts/dwarf_fortress/install_dwarf_fortress.sh $DF_WORK_DIR

if [[ $1 == 'phoebus' ]]; then
    bash $DF_WORK_DIR/scripts/dwarf_fortress/phoebus.sh $DF_WORK_DIR
else
    echo "Not installing Phoebus tileset."
fi

# bash scripts/dwarf_therapist/install_dwarf_therapist.sh
