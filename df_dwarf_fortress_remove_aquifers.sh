#!/usr/bin/env bash

raws_path='dwarffortress/df_linux/raw/objects'

for file in dwarffortress/df_linux/raw/objects/*
do
    sed s/\[AQUIFER\]//g $file > $file
done
