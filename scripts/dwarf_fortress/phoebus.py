# encoding: utf-8

from os import path

import download_df
from dfa_common import ensure_dir, copy
from extract_archive import extract_archive


def install_phoebus(df_dir_df): #{{{
    """ Download and install the Phoebus tileset. """

    phoebus_dir = path.join(df_dir_df, 'phoebus/')
    zip_path = path.join(df_dir_df, 'Phoebus.zip')

    ensure_dir(df_dir_df)
    ensure_dir(phoebus_dir)

    if not path.exists(zip_path):
        print 'Phoebus.zip not present, downloading'
        download_df.download_link(
                download_df.get_phoebus_download_link(
                download_df.get_phoebus_host_link()),
                zip_path)

    phoebus_dir_data = path.join(phoebus_dir, 'data/')
    phoebus_dir_raw = path.join(phoebus_dir, 'raw/')
    df_dir_root = path.join(df_dir_df, 'df_linux/')
    df_dir_data = path.join(df_dir_df, 'df_linux/data/')
    df_dir_raw = path.join(df_dir_df, 'df_linux/raw/')

    if not path.exists(phoebus_dir_data):
        print 'Extracting Phoebux tileset'
        extract_archive(zip_path, phoebus_dir)

    # Copy Phoebus data dir to df_linux/data
    if path.exists(phoebus_dir_data):
        print 'Copying Phoebus data dir to {dest}'.format(dest=df_dir_data)
        copy(phoebus_dir_data, df_dir_root)

    # Copy Phoebus raw dir to df_linux/raw
    if path.exists(phoebus_dir_raw):
        print 'Copying Phoebus raw dir to {dest}'.format(dest=df_dir_raw)
        copy(phoebus_dir_raw, df_dir_root)

    # Copy Phoebus init files into actual init dir.
    if path.exists(path.join(
        df_dir_df, 'df_linux/data/init/phoebus')):
        print 'Installing Phoebus init files'
        copy(path.join(df_dir_data, 'init/phoebus/*'),
            path.join(df_dir_data, 'init/')) #}}}
