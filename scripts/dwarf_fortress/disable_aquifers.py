#!/usr/bin/env python

""" Disable aquifers in Dwarf Fortress. """

import os
import re
from distutils.dir_util import copy_tree


def disable_aquifers(df_dir_df):
    """ Delete all instances of '[AQUIFER]' in the raws. """

    raws_dir = os.path.join(df_dir_df, 'df_linux/raw/')
    dir_objects = os.path.join(raws_dir, 'objects/')
    dir_objects_backup = os.path.join(raws_dir, 'objects_bak/')

    # Backup the raws dir
    if not os.path.exists(dir_objects_backup):
        copy_tree(dir_objects, dir_objects_backup)

    # Make the paths of items in dir_objects absolute
    objects = [os.path.join(dir_objects, item) for item in
            os.listdir(dir_objects)]

    # Only pay attention of the inorganic_stone files
    objects_aquifers = [entry for entry in objects
            if 'inorganic_stone' in entry]

    for raw in objects_aquifers:
        raw_file = open(raw, 'r')
        raw_lines = raw_file.readlines()
        raw_file.close()

        output_lines = []
        # Delete '[AQUIFER]' from every non-blank line.
        for line in raw_lines:
            if line != None and line != '\n':
                output_lines.append(re.sub('\[AQUIFER\]', '', line))
            elif line == '\n':
                output_lines.append(line)

        raw_file = open(raw, 'w')
        raw_file.writelines(output_lines)
        raw_file.close()
