# encoding: utf-8

import os
from dfa_common import copy


def install_lazy_newb_embarks(df_dir_root):
    src = os.path.join(
            df_dir_root,
            'custom/data/init/embark_profiles.txt')

    dest = os.path.join(
            df_dir_root,
            'dwarffortress/df_linux/data/init/embark_profiles.txt')

    copy(src, dest)
