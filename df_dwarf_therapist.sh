#!/usr/bin/env bash

# Dwarf Therapist

# Install dependencies
sudo puppet apply depends_dt.pp

# Grab a copy of the Dwarf Therapist source,
# if it already exists then update it.
if [ ! -d dwarftherapist_build ]; then
    hg clone https://dwarftherapist.googlecode.com/hg/ dwarftherapist_build
else
    cd dwarftherapist_build
    hg pull && hg update
    cd -
fi

# Build Dwarf Therapist.
cd dwarftherapist_build
    qmake
    make
cd ../

# Create new dirs if they don't exist.
if [ ! -d dwarftherapist ]; then
    mkdir -p dwarftherapist/log
else
    if [ ! -d dwarftherapist/log ]; then
        mkdir dwarftherapist/log
    fi
fi

# Copy the Dwarf Therapist binary and the 'etc' folder to the new dirs.
cp dwarffortress/dwarftherapist_build/bin/release/DwarfTherapist dwarffortress/dwarftherapist/
cp -r dwarffortress/dwarftherapist_build/etc/ dwarffortress/dwarftherapist/
