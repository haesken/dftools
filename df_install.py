#!/usr/bin/env python
# encoding: utf-8

import argparse
import os
import sys
import subprocess

sys.path.append('scripts/dwarf_fortress/')
import copy_libgl
import disable_aquifers
import download_df
import lazy_newb_embark


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


def run_cmd(cmd): #{{{
    subprocess.call(cmd, shell=True) #}}}


def main(args): #{{{
    df_dir_root = os.getcwd()
    df_dir_df = os.path.join(df_dir_root, 'dwarffortress/')
    bar = 60 * '='

    if args.dwarf_fortress: #{{{
        print bar
        print 'Installing Dwarf Fortress'
        print bar

        if not os.path.exists(df_dir_df):
            os.mkdir(df_dir_df)

        tar_path = os.path.join(df_dir_df, 'Dwarf_Fortress.tar.bz2')

        if not os.path.exists(tar_path):
            print ('Dwarf_Fortress.tar.bz2 not present, ' +
                    'downloading Dwarf Fortress...')

            download_df.download_link(
                    download_df.get_dwarf_fortress_link(),
                    tar_path)
        else:
            print 'Dwarf_Fortress.tar.bz2 present, not downloading.'

        if not os.path.exists(os.path.join(df_dir_df, 'df_linux/')):
            print 'Extracting Dwarf_Fortress.tar.bz2'
            run_cmd('tar -xf {tar_file} -C {folder}'.format(
                tar_file=tar_path, folder=df_dir_df))
        else:
            print 'df_linux dir present, not extracting'

        print 'Installing libgl library'
        copy_libgl.copy_libgl()

        print 'Dwarf Fortress installed!' #}}}

    if args.phoebus: #{{{
        print bar
        print 'Installing Phoebus tileset'
        print bar

        phoebus_dir = os.path.join(df_dir_df, 'phoebus/')
        zip_path = os.path.join(df_dir_df, 'Phoebus.zip')

        if not os.path.exists(df_dir_df):
            os.mkdir(df_dir_df)

        if not os.path.exists(phoebus_dir):
            os.mkdir(phoebus_dir)

        if not os.path.exists(zip_path):
            print 'Phoebus.zip not present, downloading'
            download_df.download_link(
                    download_df.get_phoebus_download_link(
                    download_df.get_phoebus_host_link()),
                    zip_path)

        phoebus_dir_data = os.path.join(phoebus_dir, 'data/')
        phoebus_dir_raw = os.path.join(phoebus_dir, 'raw/')
        df_dir_data = os.path.join(df_dir_df, 'df_linux/data/')
        df_dir_raw = os.path.join(df_dir_df, 'df_linux/raw/')

        if not os.path.exists(phoebus_dir_data):
            print 'Extracting Phoebux tileset'
            run_cmd('unzip -q {zip_file} -d {folder}'.format(
                zip_file=zip_path, folder=phoebus_dir))

        # Copy phoebus data dir to df_linux/data
        if os.path.exists(phoebus_dir_data):
            print 'Copying Phoebus data dir to {dest}'.format(dest=df_dir_data)
            run_cmd('cp -r {src}/* {dest}'.format(
                src=phoebus_dir_data,
                dest=df_dir_data))

        # Copy phoebus raw dir to df_linux/raw
        if os.path.exists(phoebus_dir_raw):
            print 'Copying Phoebus raw dir to {dest}'.format(dest=df_dir_raw)
            run_cmd('cp -r {src}/* {dest}'.format(
                src=phoebus_dir_raw,
                dest=df_dir_raw))

        if os.path.exists(os.path.join(
            df_dir_df, 'df_linux/data/init/phoebus')):
            print 'Installing Phoebus init files'
            run_cmd('cp -r {src}/* {dest}'.format(
                src=os.path.join(df_dir_data, 'init/phoebus'),
                dest=os.path.join(df_dir_data, 'init/')))

        print 'Phoebus tileset installed!' #}}}

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
        run_cmd("sudo apt-add-repository " +
                "'deb http://dwarftherapist.com/apt oneiric universe'")
        run_cmd("sudo apt-get update")
        run_cmd("sudo apt-get install dwarftherapist") #}}}
    #}}}


if __name__ == '__main__':
    try:
        main(get_args())
    except KeyboardInterrupt:
        sys.exit()
