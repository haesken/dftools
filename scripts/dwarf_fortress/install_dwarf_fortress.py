# encoding: utf-8

import os

from dfa_common import run_cmd, ensure_dir
import copy_libgl
import download_df


def install_dwarf_fortress(df_dir_df):
    """ Install Dwarf Fortress. """

    ensure_dir(df_dir_df)

    tar_path = os.path.join(df_dir_df, 'Dwarf_Fortress.tar.bz2')

    if not os.path.exists(tar_path):
        print ('Dwarf_Fortress.tar.bz2 not present, ' +
                'downloading Dwarf Fortress...')
        download_df.download_link(
                download_df.get_dwarf_fortress_link(),
                tar_path)
    else:
        print 'Dwarf_Fortress.tar.bz2 present, not downloading.'

    if not os.path.exists(os.path.join(df_dir_df, 'df_linux/')):
        print 'Extracting Dwarf_Fortress.tar.bz2'
        run_cmd('tar -xf {tar_file} -C {folder}'.format(
            tar_file=tar_path, folder=df_dir_df))
    else:
        print 'df_linux dir present, not extracting'

    print 'Installing libgl library'
    copy_libgl.copy_libgl()
