# encoding: utf-8

""" Enable/disable aquifers. """

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

from os import path, listdir
import re


def sub_all_in_file(somefile, regex, replacement):
    for line in raw_lines:
        if line != None and line != "\n":
            yield re.sub(regex, replacement, line)
        elif line == "\n":
            yield line


def disable_aquifers(df_paths):
    """ Delete all instances of "[AQUIFER]" in the raws. """

    print("Disabled aquifers!")

    # Make the paths of items in path_df_main_objects absolute
    objects = [path.join(df_paths["df_main_objects"], item)
            for item in listdir(df_paths["df_main_objects"])]

    # Only pay attention of the inorganic_stone files
    objects_aquifers = [entry for entry in objects
            if "inorganic_stone" in entry]

    for raw in objects_aquifers:
        raw_file = open(raw, "r")
        raw_lines = raw_file.readlines()
        raw_file.close()

        # Delete "[AQUIFER]" from every non-blank line.
        sub_all_in_file(raw_lines, "\[AQUIFER\]", "")

        raw_file = open(raw, "w")
        raw_file.writelines(output_lines)
        raw_file.close()


def toggle_aquifers(toggle, path_df_main):
    """ Enable or disable aquifers. """
    if toggle == "disable":
        disable_aquifers(path_df_main)
