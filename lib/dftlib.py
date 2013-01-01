# encoding: utf-8

""" Common dftools functions """

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

from os import path, walk, mkdir, linesep
import fnmatch
import hashlib
import requests
import sys


def make_df_paths(path_root, platform):
    """ Set up paths for convenience. """

    # Actual Dwarf Fortress install directory.
    # Ex: df_linux, df_osx, df_windows
    name_main = "df_{platform}".format(platform=platform)
    path_main = path.join(path_root, name_main)

    return {
        "root":    path_root,
        "main":    path_main,
        "data":    path.join(path_main, "data/"),
        "init":    path.join(path_main, "data/init"),
        "raw":     path.join(path_main, "raw/"),
        "objects": path.join(path_main, "raw/objects"),
        "libs":    path.join(path_main, "libs"),
        }


def detect_platform():
    """ Detect what platform we are running on. """

    if "linux" in sys.platform:
        return "linux"
    elif "darwin" in sys.platform:
        return "osx"
    # Includes cygwin
    elif "win" in sys.platform:
        return "windows"


def ensure_dir(directory):
    """ Make sure a directory exists, if not create it. """

    if not path.exists(directory):
        mkdir(directory)


def read_lines(file_path):
    """ Read the contents of a file into a list of lines. """

    with open(file_path, "rb") as f:
        return [line.strip("\n").strip("\r") for line in f.readlines()]


def read(file_path):
    """ Read the contents of a file.  """

    with open(file_path, "rb") as f:
        return f.read()


def write_lines(file_path, new_contents):
    """ Write text to a file. """

    with open(file_path, "wb") as f:
        f.writelines([line + linesep for line in new_contents])


def write(file_path, new_contents):
    """ Write the contents of a file.  """

    with open(file_path, "wb") as f:
        return f.write(new_contents)


def mksha(object_to_sum):
    """ Take a file object and return its sha1. """

    return hashlib.sha1(object_to_sum).hexdigest()


def is_same_file(path_file_a, path_file_b):
    """ Sha two files to see if they are the same. """

    sha_file_a = mksha(read(path_file_a))
    sha_file_b = mksha(read(path_file_b))

    if sha_file_a == sha_file_b:
        return True
    else:
        return False


def find_recursive(search_path, term):
    """ Search a directory recursively for a file. """

    for root, dirnames, filenames in walk(search_path):
        for filename in fnmatch.filter(filenames, term):
            yield path.join(root, filename)


def get_url(url):
    """ Get a url, return it's contents. """

    headers = {"User-Agent": "dftools"}
    resp = requests.get(url, headers=headers)
    if resp.status_code == requests.codes.ok:
        return resp.content, resp.status_code
    else:
        return None, resp.status_code


def download_file(url, path_file):
    """ Download a file. """

    raw_file, status_code = get_url(url)

    if status_code == requests.codes.ok:
        with open(path_file, "wb") as archive:
            archive.write(raw_file)
