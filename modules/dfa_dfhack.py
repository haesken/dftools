# encoding: utf-8

""" Download and install dfhack (https://github.com/peterix/dfhack). """

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

from os import path

import dfa_common
import dfa_archive
import dfa_links


def install_dfhack(df_paths): #{{{
    """ Download and install dfhack. """

    path_dfhack = path.join(df_paths['wrapper'], 'dfhack/')
    path_dfhack_archive = path.join(path_dfhack, 'dfhack.tar.gz')

    if not path.exists(path_dfhack_archive):
        print 'dfhack archive not found, downloading.'
        dfa_common.ensure_dir(path_dfhack)
        dfa_common.download_with_progress(
                dfa_links.get_dfhack_download_link(), path_dfhack_archive, 3)
    else:
        print 'Found dfhack archive here, not downloading.'

    # Extract the archive contents to a separate folder first.
    if not path.exists(path.join(df_paths['df_main'], 'dfhack.init-example')):
        print 'Extracting DFHack.'
        dfa_archive.extract_archive(path_dfhack_archive, df_paths['df_main'])
    else:
        print 'Found DFHack already extracted here, not overwriting.' #}}}
