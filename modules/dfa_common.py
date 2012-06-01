# encoding: utf-8

""" Common DFA functions """

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

from os import path, walk, mkdir
import fnmatch

import urlgrabber.progress
import urlgrabber.grabber


def find_recursive(search_path, term): #{{{
    """ Search a directory recursively for a file. """
    for root, dirnames, filenames in walk(search_path):
        for filename in fnmatch.filter(filenames, term):
            yield path.join(root, filename) #}}}


def ensure_dir(directory): #{{{
    """ Make sure a directory exists, if not create it. """
    if not path.exists(directory):
        mkdir(directory) #}}}


def download_with_progress(url, filename, retry_num): #{{{
    """ Download a file with a progress bar. """
    print "Downloading: {url}".format(url=url)
    dfa_user_agent = 'Dwarf Fortress Auto'
    grabber = urlgrabber.grabber.URLGrabber(user_agent=dfa_user_agent)
    grabber.opts.progress_obj = urlgrabber.progress.TextMeter()
    grabber.opts.retry = retry_num
    grabber.urlgrab(url, filename) #}}}
