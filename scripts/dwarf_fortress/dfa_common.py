#!/usr/bin/env python

""" Common functions for Dwarf Fortress Auto """

import subprocess
import os
import fnmatch

import urlgrabber.progress
import urlgrabber.grabber


def run_cmd(cmd): #{{{
    """ Run an external command. """

    subprocess.call(cmd, shell=True) #}}}


def find_recursive(path, term): #{{{
    """ Search a directory recursively for a file. """

    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, term):
            matches.append(os.path.join(root, filename))
    return matches #}}}


def ensure_dir(directory): #{{{
    """ Make sure a directory exists, if not create it. """

    if not os.path.exists(directory):
        os.mkdir(directory) #}}}


def download_with_progress(url, filename): #{{{
    """ Download a file with a progress bar. """

    grabber = urlgrabber.grabber.URLGrabber()
    grabber.opts.progress_obj = urlgrabber.progress.TextMeter()
    grabber.urlgrab(url, filename) #}}}
