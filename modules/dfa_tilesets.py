# encoding: utf-8

""" Install tilesets. """

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


def copy_tree_verbose(path_from, path_to): #{{{
    print 'Copying {path_from} to {path_to}'.format(
            path_from=path_from, path_to=path_to)
    copy_tree(path_from, path_to) #}}}


def extract_tileset(path_tileset_archive, path_tileset): #{{{
    try:
        dfa_archive.extract_archive(path_tileset_archive, path_tileset)
        return 0
    # If the archive is incomplete, corrupted, etc.
    except IOError:
        return 1 #}}}


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
    print 'Checking current version of tileset.'
    tileset_url, tileset_filename = get_tileset_url(tileset_name)

    path_tileset_archive = os.path.join(path_dwarffortress, tileset_filename)
    path_tileset = os.path.join(path_dwarffortress, tileset_name)
    path_tileset_data = os.path.join(path_tileset, 'data/')
    path_tileset_raw = os.path.join(path_tileset, 'raw/')
    path_tileset_inits = os.path.join(
            path_tileset_data, 'init/{tileset_name}'.format(
                tileset_name=tileset_name))

    # Download the tileset if the archive isn't present.
    if not os.path.exists(path_tileset_archive):
        print '{tileset_filename} not present, downloading.'.format(
                tileset_filename=tileset_filename)
        dfa_common.download_with_progress(tileset_url, path_tileset_archive, 3)

    # If the archive hasn't already been extracted (to its own dir).
    if not os.path.exists(path_tileset_data):
        extracted_status = extract_tileset(path_tileset_archive, path_tileset)
        # If the archive is broken, corrupt, etc then remove it.
        if extracted_status != 0:
            os.remove(path_tileset_archive)

    path_df_main = os.path.join(path_dwarffortress, 'df_linux/')
    path_df_main_data = os.path.join(path_df_main, 'data/')
    path_df_main_raw = os.path.join(path_df_main, 'raw/')
    path_df_main_inits = os.path.join(path_df_main_data, 'init')

    # Copy tileset data/raws to the df_main directory.
    if os.path.exists(path_tileset_data):
        copy_tree_verbose(path_tileset_data, path_df_main_data)
        copy_tree_verbose(path_tileset_raw, path_df_main_raw)

    # Copy tileset init files into the actual init directory.
    if os.path.exists(path_tileset_inits):
        copy_tree_verbose(path_tileset_inits, path_df_main_inits) #}}}
