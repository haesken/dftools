#!/usr/bin/env python
# encoding: utf-8

""" A set of scripts to download and install Dwarf Fortress,
    tilesets, and embark profiles.
"""

# License #{{{
license = """
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
""" #}}}

from os import path, getcwd
import argparse
import sys

sys.path.append('modules/')
import dfa_common
import dfa_aquifers
import dfa_df
import dfa_dfhack
import dfa_embarks
import dfa_tilesets


def detect_platform(): #{{{
    """ Detect what platform we are running on. """
    if 'linux' in sys.platform:
        return 'linux'
    elif 'darwin' in sys.platform:
        return 'osx'
    # Includes cygwin
    elif 'win' in sys.platform:
        return 'windows' #}}}


def get_args(): #{{{
    """ Get arguments from the command line. """

    parser = argparse.ArgumentParser(
            description="Install Dwarf Fortress and utilities.")

    parser.add_argument("-d", "--directory",
            type=str,
            default=path.join(getcwd(), 'dwarffortress'),
            help="Directory to install Dwarf Fortress to.")

    parser.add_argument("-p", "--platform",
            type=str,
            choices=("linux", "osx", "windows"),
            default=detect_platform(),
            help="Override platform detection.")

    parser.add_argument("-df", "--dwarf_fortress",
            action="store_true",
            help="Install Dwarf Fortress.")

    parser.add_argument("-t", "--tileset",
            type=str,
            choices=("phoebus", "jolly9", "jolly12"),
            help="Install a tileset.")

    parser.add_argument("-e", "--embarks",
            type=str,
            choices=("lnp", ),
            help="Install embark profiles.")

    parser.add_argument("-aq", "--aquifers",
            type=str,
            choices=('disable', 'enable'),
            help="Enable or disable aquifers.")

    parser.add_argument("-dfh", "--dfhack",
            action="store_true",
            help="Install DFHack.")

    parser.add_argument("-q", "--quick",
            action="store_true",
            help="Quick install of some sensible defaults.\n" +
                 "Equivalent to '-df -t phoebus -e lnp -aq disable'")

    parser.add_argument("-l", "--license",
            action="store_true",
            help="Display the license.")

    return parser.parse_args() #}}}


def main(args): #{{{
    """ Run selected options. """

    # Wrapper directory where downloaded/extracted archives,
    # and the main df directory go.
    path_wrapper_dir = args.directory
    dfa_common.ensure_dir(path_wrapper_dir)

    # Actual Dwarf Fortress install directory.
    name_df_main = 'df_{platform}'.format(platform=args.platform)
    path_df_main = path.join(path_wrapper_dir, name_df_main)

    # Directory for custom files such as embark profiles and init restores.
    path_custom = path.join(getcwd(), 'custom')

    df_paths = {
            'wrapper': path_wrapper_dir,
            'df_main': path_df_main,
            'df_main_data': path.join(path_df_main, 'data/'),
            'df_main_inits': path.join(path_df_main, 'data/init'),
            'df_main_raw': path.join(path_df_main, 'raw/'),
            'df_main_objects': path.join(path_df_main, 'raw/objects'),
            'df_main_libs': path.join(path_df_main, 'libs'),
            }

    divider = 60 * '='

    if args.dwarf_fortress or args.quick:
        print divider
        dfa_df.install_dwarf_fortress(args.platform, df_paths)
        print divider

    if args.tileset or args.quick:
        print divider
        dfa_tilesets.install_tileset(args.tileset, df_paths)
        print divider

    if args.embarks or args.quick:
        print divider
        dfa_embarks.install_embarks(
                args.embarks, path_custom, df_paths)
        print divider

    if args.aquifers or args.quick:
        print divider
        dfa_aquifers.toggle_aquifers(args.aquifers, df_paths)
        print divider

    if args.dfhack:
        print divider
        dfa_dfhack.install_dfhack(args.platform, df_paths)
        print divider

    if args.license:
        print license #}}}


if __name__ == '__main__': #{{{
    try:
        main(get_args())
    except KeyboardInterrupt:
        sys.exit() #}}}
