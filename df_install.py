#!/usr/bin/env python
# encoding: utf-8

import argparse
import subprocess
import os
import sys


def get_args(): #{{{
    """ Get arguments from the command line. """

    parser = argparse.ArgumentParser(
            description="Install Dwarf Fortress",
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

    parser.add_argument("-dt", "--dwarf_therapist",
            action="store_true",
            help="Build & Install Dwarf Therapist")

    args = parser.parse_args()
    return args #}}}


def run(cmd): #{{{
    subprocess.call(cmd, shell=True) #}}}


def main(args): #{{{
    DF_WORK_DIR = os.getcwd()

    run('sudo puppet apply {workdir}/scripts/scripts_depends.pp'.format(
        workdir=DF_WORK_DIR))

    if args.dwarf_fortress == True:
        run('bash {workdir}/scripts/dwarf_fortress/install.sh {workdir}'.format(
            workdir=DF_WORK_DIR))

    if args.phoebus == True:
        run('bash {workdir}/scripts/dwarf_fortress/phoebus.sh {workdir}'.format(
            workdir=DF_WORK_DIR))

    if args.dwarf_therapist == True:
        run('bash {workdir}/scripts/dwarf_therapist/install_dwarf_therapist.sh {workdir}'.format(
            workdir=DF_WORK_DIR)) #}}}


try:
    main(get_args())
except KeyboardInterrupt:
    sys.exit()
