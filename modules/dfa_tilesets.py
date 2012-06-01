# encoding: utf-8

""" Install tilesets. """

""" #{{{
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

from distutils.dir_util import copy_tree
from os import path, remove

import dfa_common
import dfa_archive


def copy_tree_verbose(path_from, path_to): #{{{
    """ Recursively copy a file or directory. """
    print 'Copying {path_from} to {path_to}'.format(
            path_from=path_from, path_to=path_to)
    copy_tree(path_from, path_to) #}}}


def extract_tileset(path_tileset_archive, path_tileset): #{{{
    """ Try to extract a tileset, don't explode if the archive is corrupt. """
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
    dfa_media_repo_link = ("https://github.com/haesken/" +
            "dwarf_fortress_auto_media/blob/master/")

    if tileset_name == 'phoebus':
        tileset_url = (dfa_media_repo_link +
                "tilesets/34_10_phoebus.tar.gz?raw=true")
    elif tileset_name == 'mayday':
        tileset_url = (dfa_media_repo_link +
                "tilesets/34_10_mayday.tar.gz?raw=true")
    elif tileset_name == 'jollybastion':
        tileset_url = (dfa_media_repo_link +
                "tilesets/34_10_jolly_bastion_12x12.tar.gz?raw=true")
    elif tileset_name == 'square':
        tileset_url = (dfa_media_repo_link +
                "tilesets/34_10_phoebus.tar.gz?raw=true")

    tileset_filename = tileset_url.split('/')[-1][:-9]

    return (tileset_url, tileset_filename) #}}}


def define_tileset_paths(tileset_name, tileset_filename, df_paths): #{{{
    """ Define paths for the tileset files. """
    path_tileset_archive = path.join(df_paths['wrapper'], tileset_filename)
    path_tileset = path.join(df_paths['wrapper'], tileset_name)
    path_tileset_data = path.join(path_tileset, 'data/')
    path_tileset_raw = path.join(path_tileset, 'raw/')
    path_tileset_inits = path.join(
            path_tileset_data, 'init/{tileset_name}'.format(
                tileset_name=tileset_name))

    return {
        'tileset_archive': path_tileset_archive,
        'tileset': path_tileset,
        'tileset_data': path_tileset_data,
        'tileset_raw': path_tileset_raw,
        'tileset_inits': path_tileset_inits,
    } #}}}


def install_tileset(tileset_name, df_paths): #{{{
    """ Download and install a tileset. """

    # Check for the current version of the tileset
    print 'Checking current version of tileset.'
    tileset_url, tileset_filename = get_tileset_url(tileset_name)
    tileset_paths = define_tileset_paths(
            tileset_name, tileset_filename, df_paths)

    # Download the tileset if the archive isn't present.
    if not path.exists(tileset_paths['tileset_archive']):
        print '{tileset_filename} not present, downloading.'.format(
                tileset_filename=tileset_filename)
        dfa_common.download_with_progress(
                tileset_url, tileset_paths['tileset_archive'], 3)

    # If the archive hasn't already been extracted (to its own dir).
    if not path.exists(tileset_paths['tileset_data']):
        extracted_status = extract_tileset(
                tileset_paths['tileset_archive'],
                tileset_paths['tileset'])
        # If the archive is broken, corrupt, etc then remove it.
        if extracted_status != 0:
            remove(tileset_paths['tileset_archive'])

    # Copy tileset data/raws/inits to the df_main directory.
    if path.exists(tileset_paths['tileset_data']):
        copy_tree_verbose(
                tileset_paths['tileset_data'], df_paths['df_main_data'])
        copy_tree_verbose(
                tileset_paths['tileset_raw'], df_paths['df_main_raw'])

    # These should probably exist but might not.
    if path.exists(tileset_paths['tileset_inits']):
        copy_tree_verbose(
                tileset_paths['tileset_inits'], df_paths['df_main_inits']) #}}}
