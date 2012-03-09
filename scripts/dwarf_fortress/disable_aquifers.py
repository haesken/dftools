#!/usr/bin/env python
# encoding: utf-8

import os
import shutil
import subprocess


def disable_aquifers(df_dir_df):
    raws_dir = os.path.join(df_dir_df, 'df_linux/raw/')

    # Backup the raws dir
    shutil.copytree(
            os.path.join(raws_dir, 'objects/'),
            os.path.join(raws_dir, 'objects_bak/'))

    raws = os.listdir(os.path.join(raws_dir, 'objects/'))

    raws_aquifers = [entry for entry in raws if 'inorganic_stone' in entry]

    for raw in raws_aquifers:
        subprocess.call(
            "sed -i 's/\[AQUIFER\]//g' {raw}".format(raw=raw), shell=True)
