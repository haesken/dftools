# encoding: utf-8

""" Install the embark profiles. """

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

from os import path


def append_embarks(path_embarks_custom, path_df_main):
    """ Append custom embark profiles to the current ones. """
    path_embarks_current = path.join(
        path_df_main, 'data/init/embark_profiles.txt')

    # If there is already a set of embark profiles, then append the new ones.
    if path.exists(path_embarks_current):
        new_embarks = (open(path_embarks_current, "r").read() +
                        open(path_embarks_custom, "r").read())
    else:
        new_embarks = open(path_embarks_custom, "r").read()

    open(path_embarks_current, "w").write(new_embarks)


def install_embarks(embarks_name, path_custom, df_paths):
    """ Install selected embark profiles. """
    path_embarks_custom = path.join(path_custom, 'embarks/')
    if embarks_name == "lnp":
        print "Added Lazy Newb Pack embark profiles!"
        append_embarks(
            path.join(path_embarks_custom, 'lazy_newb_pack.txt'),
            df_paths['df_main'])
    if embarks_name == "mayday":
        print "Added Mayday embark profiles!"
        append_embarks(
            path.join(path_embarks_custom, 'mayday.txt'),
            df_paths['df_main'])
