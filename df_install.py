#!/usr/bin/env python
# encoding: utf-8

""" A set of scripts to download and install Dwarf Fortress
    and Dwarf Therapist, with a few included utilities.
"""

"""
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
