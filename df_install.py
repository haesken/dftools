#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
import sys

sys.path.append('scripts/dwarf_fortress/')
import disable_aquifers
import install_dwarf_fortress
import install_dwarf_therapist
import lazy_newb_embark
import phoebus


def get_args(): #{{{
    """ Get arguments from the command line. """

    parser = argparse.ArgumentParser(
            description="Install Dwarf Fortress and utilities.",
            formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-df", "--dwarf_fortress",
            action="store_true",
            help="Install Dwarf Fortress")

    parser.add_argument("-ph", "--phoebus",
            action="store_true",
            help="Install Phoebus tileset")

    parser.add_argument("-lze", "--lazy_newb_embark",
            action="store_true",
            help="Install embark profiles from Lazy Newb Pack")

    parser.add_argument("-daq", "--disable_aquifers",
            action="store_true",
            help="Disable aquifers")

    parser.add_argument("-dt", "--dwarf_therapist",
            action="store_true",
            help="Install Dwarf Therapist")

    args = parser.parse_args()
    return args #}}}


def main(args): #{{{
    df_dir_root = os.getcwd()
    df_dir_df = os.path.join(df_dir_root, 'dwarffortress/')
    bar = 60 * '='

    if args.dwarf_fortress: #{{{
        print bar
        print 'Installing Dwarf Fortress'
        install_dwarf_fortress.install_dwarf_fortress(df_dir_df)
        print bar
        print 'Dwarf Fortress installed!'
        print bar #}}}

    if args.phoebus: #{{{
        print bar
        print 'Installing Phoebus tileset'
        print bar
        phoebus.install_phoebus(df_dir_df)
        print 'Phoebus tileset installed!'
        print bar #}}}

    if args.lazy_newb_embark: #{{{
        print bar
        lazy_newb_embark.install_lazy_newb_embarks(df_dir_root)
        print 'Installed Lazy Newb Pack embark profiles!'
        print bar #}}}

    if args.disable_aquifers: #{{{
        print bar
        disable_aquifers.disable_aquifers(df_dir_df)
        print 'Disabled aquifers!'
        print bar #}}}

    if args.dwarf_therapist: #{{{
        print bar
        print 'Installing Dwarf Therapist'
        install_dwarf_therapist.install_dwarf_therapist()
        print bar
        print 'Installed Dwarf Therapist!'
        print bar #}}}
    #}}}


if __name__ == '__main__': #{{{
    try:
        main(get_args())
    except KeyboardInterrupt:
        sys.exit() #}}}
