# encoding: utf-8

""" Extract archive files.
    Handles tar and zip.
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

import tarfile
import zipfile


def find_type(archive_path): #{{{
    """ See if the file is actually an archive. """

    extension = archive_path.split(".")[-1].lower()

    if extension in ['tar', 'bz2', 'gz', 'gzip']:
        if tarfile.is_tarfile(archive_path):
            return ('tar', extension)

    elif extension == 'zip':
        if zipfile.is_zipfile(archive_path):
            return ('zip',) #}}}


def check_for_bad_filenames(names_list): #{{{
    """ Look for Malicious filenames in the archive.
        Throw an exception if we find any.
    """

    for name in names_list:
        if name.startswith('/'):
            raise ValueError('Malicous filenames in this archive!')
        for level in name.split('/'):
            if '..' in level:
                raise ValueError('Malicous filenames in this archive!') #}}}


def extract_tar(archive_path, comp_type, extract_path): #{{{
    """ Extract a tar archive. """

    tar_file = tarfile.open(archive_path,
            'r:{comp_type}'.format(comp_type=comp_type))

    check_for_bad_filenames(tar_file.getnames())

    tar_file.extractall(extract_path)
    tar_file.close() #}}}


def extract_zip(archive_path, extract_path): #{{{
    """ Extract a zip archive_path. """
    zip_file = zipfile.ZipFile(archive_path, 'r')

    check_for_bad_filenames(zip_file.namelist())

    zip_file.extractall(extract_path)
    zip_file.close() #}}}


def extract_archive(archive_path, extract_path): #{{{
    """ Extract an archive to the specified path. """

    archive_type = find_type(archive_path)

    if archive_type != None:
        if archive_type[0] == 'tar':
            extract_tar(archive_path, archive_type[1], extract_path)
        elif archive_type[0] == 'zip':
            extract_zip(archive_path, extract_path)
    else:
        raise IOError('Bad archive!') #}}}
