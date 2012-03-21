# encoding: utf-8

""" Download and install Dwarf Fortress. """

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

from dfa_common import ensure_dir, download_with_progress
from extract_archive import extract_archive
from copy_libgl import copy_libgl
from download_df import get_dwarf_fortress_link


def install_dwarf_fortress(df_dir_df): #{{{
    """ Download and install Dwarf Fortress. """

    ensure_dir(df_dir_df)

    tar_path = os.path.join(df_dir_df, 'Dwarf_Fortress.tar.bz2')

    if not os.path.exists(tar_path):
        print ('Dwarf_Fortress.tar.bz2 not present, ' +
                'downloading Dwarf Fortress...')
        download_with_progress(
                get_dwarf_fortress_link(),
                tar_path)
    else:
        print 'Dwarf_Fortress.tar.bz2 present, not downloading.'

    if not os.path.exists(os.path.join(df_dir_df, 'df_linux/')):
        print 'Extracting Dwarf_Fortress.tar.bz2'
        extract_archive(tar_path, df_dir_df)
    else:
        print 'df_linux dir present, not extracting'

    if not os.path.exists(os.path.join(df_dir_df, 'df_linux/libs/libgl.so.1')):
        print 'Installing libgl library'
        copy_libgl(df_dir_df) #}}}
