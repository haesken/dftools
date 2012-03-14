#!/usr/bin/env python
# encoding: utf-8

""" A set of scripts to download and install Dwarf Fortress
    and Dwarf Therapist, with a few included utilities.
"""

import argparse
import os
import sys

sys.path.append('scripts/dwarf_fortress/')
import disable_aquifers
import install_dwarf_fortress
import install_dwarf_therapist
import lazy_newb_embark
import phoebus
from dfa_common import ensure_dir


def get_args(): #{{{
    """ Get arguments from the command line. """

    parser = argparse.ArgumentParser(
            description="Install Dwarf Fortress and utilities.",
            formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-dir", "--directory",
            type=str,
            default=os.getcwd(),
            help="Directory to install Dwarf Fortress in.")

    parser.add_argument("-df", "--dwarf_fortress",
            action="store_true",
            help="Install Dwarf Fortress.")

    parser.add_argument("-ph", "--phoebus",
            action="store_true",
            help="Install Phoebus tileset.")

    parser.add_argument("-lze", "--lazy_newb_embark",
            action="store_true",
            help="Install embark profiles from Lazy Newb Pack.")

    parser.add_argument("-daq", "--disable_aquifers",
            action="store_true",
            help="Disable aquifers.")

    parser.add_argument("-dt", "--dwarf_therapist",
            action="store_true",
            help="Install Dwarf Therapist.")

    args = parser.parse_args()
    return args #}}}


def main(args): #{{{
    """ Run functions for selected args. """
    ensure_dir(args.directory)
    df_dir_df = os.path.join(args.directory, 'dwarffortress/')

    divider = 60 * '='

    if args.dwarf_fortress: #{{{
        print divider
        print 'Installing Dwarf Fortress'
        install_dwarf_fortress.install_dwarf_fortress(df_dir_df)
        print divider
        print 'Dwarf Fortress installed!'
        print divider #}}}

    if args.phoebus: #{{{
        print divider
        print 'Installing Phoebus tileset'
        print divider
        phoebus.install_phoebus(df_dir_df)
        print 'Phoebus tileset installed!'
        print divider #}}}

    if args.lazy_newb_embark: #{{{
        print divider
        lazy_newb_embark.install_lazy_newb_embarks(args.directory)
        print 'Installed Lazy Newb Pack embark profiles!'
        print divider #}}}

    if args.disable_aquifers: #{{{
        print divider
        disable_aquifers.disable_aquifers(df_dir_df)
        print 'Disabled aquifers!'
        print divider #}}}

    if args.dwarf_therapist: #{{{
        print divider
        print 'Installing Dwarf Therapist'
        install_dwarf_therapist.install_dwarf_therapist()
        print divider
        print 'Installed Dwarf Therapist!'
        print divider #}}}
    #}}}


if __name__ == '__main__': #{{{
    try:
        main(get_args())
    except KeyboardInterrupt:
        sys.exit() #}}}
