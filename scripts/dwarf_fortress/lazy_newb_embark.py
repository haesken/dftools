# encoding: utf-8

from os import path
from distutils.file_util import copy_file


def install_lazy_newb_embarks(df_dir_root):
    copy_file(path.join(
            df_dir_root,
            'custom/data/init/embark_profiles.txt'),
            path.join(
            df_dir_root,
            'dwarffortress/df_linux/data/init/embark_profiles.txt'))
