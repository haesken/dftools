#!/usr/bin/env python

import subprocess
import os


def run_cmd(cmd): #{{{
    subprocess.call(cmd, shell=True) #}}}


def ensure_dir(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def copy(src, dest):
    copy_cmd = 'cp -r {src} {dest}'.format(src=src, dest=dest)
    subprocess.call(copy_cmd, shell=True) #}}}
