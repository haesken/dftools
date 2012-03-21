# encoding: utf-8

""" Disable aquifers in Dwarf Fortress. """

"""
Copyright (c) 2012, haesken
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of haesken nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL haesken BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import os
import re
from distutils.dir_util import copy_tree


def disable_aquifers(df_dir_df): #{{{
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
        raw_file.close() #}}}
