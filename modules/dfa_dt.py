# encoding: utf-8

""" Install Dwarf Therapist via apt. """

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

import dfa_common


def install_dwarf_therapist(): #{{{
    """ Install Dwarf Therapist (Ubuntu) """

    sources_path = '/etc/apt/sources.list'
    sources = open(sources_path).readlines()
    dt_lines = [line for line in sources
            if 'dwarftherapist.com/apt' in line]

    if len(dt_lines) == 0:
        print 'Dwarf Therapist repo not found in {sources}'.format(
                sources=sources_path)
        print 'Adding repo to {sources}'.format(sources=sources_path)

        dfa_common.run_cmd("sudo apt-add-repository " +
                "'deb http://dwarftherapist.com/apt oneiric universe'")
    else:
        print 'Dwarf Therapist found in {sources}, not adding.'.format(
                sources=sources_path)

    dfa_common.run_cmd("sudo apt-get update")
    dfa_common.run_cmd("sudo apt-get install dwarftherapist") #}}}
