# encoding: utf-8

import os
import envoy
import shutil


def copy_libgl(): #{{{
    libgl_canidates_lib = envoy.run('find /usr/lib -iname libgl.so.1')
    libgl_canidates_lib32 = envoy.run('find /usr/lib32 -iname libgl.so.1')

    libgl_canidates = []

    for canidate in libgl_canidates_lib.std_out.strip().split('\n'):
        libgl_canidates.append(canidate)

    for canidate in libgl_canidates_lib32.std_out.strip().split('\n'):
        libgl_canidates.append(canidate)

    libgl_path = [canidate for canidate in libgl_canidates
        if 'nvidia' not in canidate and '64' not in canidate][0]


    df_libs_path = os.path.join(
            '/home/mike/games/dwarf_fortress_auto/', 'dwarffortress/df_linux/libs/')

    shutil.copy2(libgl_path, os.path.join(df_libs_path, 'libgl.so.1'))

    print "Copied: {libgl_path} to {df_libs_path}".format(
            libgl_path=libgl_path, df_libs_path=df_libs_path) #}}}
