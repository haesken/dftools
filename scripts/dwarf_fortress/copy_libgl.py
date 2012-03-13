# encoding: utf-8

import os
import shutil
from dfa_common import find_recursive


def copy_libgl(df_dir_df): #{{{

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

    df_libs_path = os.path.join(df_dir_df, 'df_linux/libs/')

    shutil.copy2(libgl_path, os.path.join(df_libs_path, 'libgl.so.1'))

    print "Copied: {libgl_path} to {df_libs_path}".format(
            libgl_path=libgl_path, df_libs_path=df_libs_path) #}}}
