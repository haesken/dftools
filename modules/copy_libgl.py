# encoding: utf-8

""" Find and copy libgl library to the Dwarf Fortress libs directory. """

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
from distutils.file_util import copy_file
from dfa_common import find_recursive


def copy_libgl(path_dflinux): #{{{
    """ Find and copy libgl library to the Dwarf Fortress libs directory. """

    libgl_canidates = []

    lib_matches = find_recursive('/usr/lib/', 'libGL.so.1')
    if lib_matches != None:
        for item in lib_matches:
            libgl_canidates.append(item)

    lib_matches_32 = find_recursive('/usr/lib32/', 'libGL.so.1')
    if lib_matches != None:
        for item in lib_matches_32:
            libgl_canidates.append(item)

    libgl_path = [canidate for canidate in libgl_canidates
        if 'nvidia' not in canidate and '64' not in canidate][0]

    path_df_libs = os.path.join(path_dflinux, 'df_linux/libs/')

    copy_file(libgl_path, os.path.join(path_df_libs, 'libGL.so.1'))

    print "Copied: {libgl_path} to {path_df_libs}".format(
            libgl_path=libgl_path, path_df_libs=path_df_libs) #}}}
