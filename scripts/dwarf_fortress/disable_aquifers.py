#!/usr/bin/env python
# encoding: utf-8

import os
import shutil
import subprocess


def disable_aquifers(df_dir_df):
    raws_dir = os.path.join(df_dir_df, 'df_linux/raw/')

    dir_objects = os.path.join(raws_dir, 'objects/'),
    dir_objects_backup = os.path.join(raws_dir, 'objects_bak/')

    # Backup the raws dir
    if not os.path.exists(dir_objects_backup):
        shutil.copytree(dir_objects, dir_objects_backup)

    # Make the paths of items in dir_objects absolute
    objects = [os.path.abspath(item) for item in
            os.listdir(dir_objects[0])]

    # Only pay attention of the inorganic_stone files
    objects_aquifers = [entry for entry in objects
            if 'inorganic_stone' in entry]

    for raw in objects_aquifers:
        subprocess.call(
            "sed -i 's/\[AQUIFER\]//g' {raw}".format(raw=raw), shell=True)
