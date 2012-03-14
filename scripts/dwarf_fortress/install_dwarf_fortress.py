# encoding: utf-8

import os

from dfa_common import ensure_dir, download_with_progress
from extract_archive import extract_archive
from copy_libgl import copy_libgl
from download_df import get_dwarf_fortress_link


def install_dwarf_fortress(df_dir_df): #{{{
    """ Install Dwarf Fortress. """

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
