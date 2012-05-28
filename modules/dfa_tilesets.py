# encoding: utf-8

""" Install the Phoebus tileset. """

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

import os
from distutils.dir_util import copy_tree

import dfa_common
import dfa_archive
import dfa_links


def copy_data():
    pass


def copy_raws():
    pass


def copy_inits():
    pass


def extract_tileset(path_tileset_archive, path_tileset):
    try:
        dfa_archive.extract_archive(path_tileset_archive, path_tileset)
        return 0

    # If the archive is incomplete, corrupted, etc.
    except IOError:
        return 1


def get_tileset_url(tileset_name): #{{{
    """ Get the url for the specified tileset,
        return the url and the filename of the archive.
    """
    if tileset_name == 'phoebus':
        tileset_url = dfa_links.get_phoebus_download_link(
                dfa_links.get_phoebus_host_link())
        tileset_filename = tileset_url.split('=')[-1]
        return (tileset_url, tileset_filename) #}}}


def install_tileset(tileset_name, platform, path_dwarffortress): #{{{
    """ Download and install a tileset. """

    # Check for the current version of the tileset
    tileset_url, tileset_filename = get_tileset_url(tileset_name)

    path_tileset_archive = os.path.join(path_dwarffortress, tileset_filename)
    path_tileset = os.path.join(path_dwarffortress, tileset_name)
    path_tileset_data = os.path.join(path_tileset, 'data/')
    path_tileset_raw = os.path.join(path_tileset, 'raw/')

    # Download the tileset if the archive isn't present.
    if not os.path.exists(path_tileset_archive):
        dfa_common.download_with_progress(tileset_url, path_tileset_archive, 3)

    # If the archive hasn't already been extracted (to its own dir)
    if not os.path.exists(path_tileset_data):
        extracted_status = extract_tileset(path_tileset_archive, path_tileset)
        # If the archive is broken, corrupt, etc then remove it.
        if extracted_status != 0:
            os.remove(path_tileset_archive)

    # copy tileset data
    # copy tileset raws
    # copy tileset inits


    path_dflinux = os.path.join(path_dwarffortress, 'df_linux/')
    path_dflinux_data = os.path.join(path_dflinux, 'data/')
    path_dflinux_raw = os.path.join(path_dflinux, 'raw/')

    dfa_common.ensure_dir(path_dwarffortress)
    dfa_common.ensure_dir(path_tileset)

    # We retry here because the file host (dffd) is rather slow.

    # Copy Phoebus data dir to df_linux/data
    if os.path.exists(path_tileset_data):
        print 'Copying Phoebus data dir to {dest}'.format(
                dest=path_dflinux_data)
        copy_tree(path_tileset_data, path_dflinux_data)

    # Copy Phoebus raw dir to df_linux/raw
    if os.path.exists(path_tileset_raw):
        print 'Copying Phoebus raw dir to {dest}'.format(
                dest=path_dflinux_raw)
        copy_tree(path_tileset_raw, path_dflinux_raw)

    # Copy Phoebus init files into actual init dir.
    if os.path.exists(os.path.join(
        path_dwarffortress, 'df_linux/data/init/phoebus')):
        print 'Installing Phoebus init files'
        copy_tree(os.path.join(path_dflinux_data, 'init/phoebus/'),
            os.path.join(path_dflinux_data, 'init/')) #}}}
