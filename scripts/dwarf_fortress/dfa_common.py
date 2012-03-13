#!/usr/bin/env python

import subprocess
import os
import fnmatch


def run_cmd(cmd): #{{{
    subprocess.call(cmd, shell=True) #}}}


def find_recursive(path, term): #{{{
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, term):
            matches.append(os.path.join(root, filename))
    return matches #}}}


def ensure_dir(directory): #{{{
    if not os.path.exists(directory):
        os.mkdir(directory) #}}}


def copy(src, dest): #{{{
    copy_cmd = 'cp -r {src} {dest}'.format(src=src, dest=dest)
    subprocess.call(copy_cmd, shell=True) #}}}
