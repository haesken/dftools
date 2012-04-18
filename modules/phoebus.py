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

from os import path, remove
from distutils.dir_util import copy_tree

from dfa_common import ensure_dir, download_with_progress
from extract_archive import extract_archive
from find_links import get_phoebus_host_link, get_phoebus_download_link


def download_phoebus(path_phoebus_archive): #{{{
    """ blah """

    print 'Phoebus.zip not present, downloading'
    download_with_progress(
            get_phoebus_download_link(get_phoebus_host_link()),
            path_phoebus_archive, 1) #}}}


def install_phoebus(path_dwarffortress): #{{{
    """ Download and install the Phoebus tileset. """

    path_phoebus = path.join(path_dwarffortress, 'phoebus/')
    path_phoebus_data = path.join(path_phoebus, 'data/')
    path_phoebus_raw = path.join(path_phoebus, 'raw/')

    path_phoebus_archive = path.join(path_dwarffortress, 'Phoebus.zip')

    path_dflinux = path.join(path_dwarffortress, 'df_linux/')
    path_dflinux_data = path.join(path_dflinux, 'data/')
    path_dflinux_raw = path.join(path_dflinux, 'raw/')

    ensure_dir(path_dwarffortress)
    ensure_dir(path_phoebus)

    if not path.exists(path_phoebus_archive):
        download_phoebus(path_phoebus_archive)

    # We retry here because the file host (dffd) is rather slow.
    if not path.exists(path_phoebus_data):
        print 'Extracting Phoebux tileset'

        retry = 0
        while retry < 3:
            try:
                extract_archive(path_phoebus_archive, path_phoebus)
                retry += 1
            # If the archive is incomplete, corrupted, etc.
            except IOError:
                remove(path_phoebus_archive)
                download_phoebus(path_phoebus_archive)
                retry += 1

    # Copy Phoebus data dir to df_linux/data
    if path.exists(path_phoebus_data):
        print 'Copying Phoebus data dir to {dest}'.format(
                dest=path_dflinux_data)
        copy_tree(path_phoebus_data, path_dflinux_data)

    # Copy Phoebus raw dir to df_linux/raw
    if path.exists(path_phoebus_raw):
        print 'Copying Phoebus raw dir to {dest}'.format(
                dest=path_dflinux_raw)
        copy_tree(path_phoebus_raw, path_dflinux_raw)

    # Copy Phoebus init files into actual init dir.
    if path.exists(path.join(
        path_dwarffortress, 'df_linux/data/init/phoebus')):
        print 'Installing Phoebus init files'
        copy_tree(path.join(path_dflinux_data, 'init/phoebus/'),
            path.join(path_dflinux_data, 'init/')) #}}}
