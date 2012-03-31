#!/usr/bin/env python
# encoding: utf-8

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

import argparse
import sys


def get_args(): #{{{
    """ Get arguments from the command line. """

    parser = argparse.ArgumentParser(
            description="Set options in a Dwarf Fortress init file.",
            formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-p", "--path",
            type=str,
            default="defaultval",
            help="Path to the Dwarf Fortress init.txt/d_init.txt file")

    parser.add_argument("-o", "--option",
            type=str,
            default="population",
            help="Option to set, ex: population")

    parser.add_argument("-v", "--value",
            type=str,
            default="defaultval",
            help="New value of the option, ex: 70")

    args = parser.parse_args()
    return args #}}}


def read_file(path): #{{{
    """ Read the contents of a file.
        Return the contents.
    """
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines #}}}


def find_option(option_name, lines): #{{{
    """ Find a line containing the option.
        Return the line.
    """

    for line in lines:
        if line.startswith('[') and line.strip('\r\n').endswith(']'):
            if option_name.lower() in line.lower():
                return line.strip('\r\n') #}}}


def parse_option(line): #{{{
    """ Parse the option line.
        Returns a tuple with the option and a list of argument values.
    """
    segments = line.strip('[').strip(']').split(':')
    option = segments[0]
    values = segments[1:]
    return (option, values) #}}}


def set_option_values(option_pair, new_values): #{{{
    """ Set new values for an option.
        Returns a tuple with the option and new argument values.
    """

    new_pair = (option_pair[0], new_values)
    return new_pair #}}}


def make_option_line(option_pair): #{{{
    """ Generate a valid option line for the init file, ex: '[Population:70]'.
        Returns the new line (including '\r\n' at the end).
    """

    values = [item for item in option_pair[1:]][0]
    line = '[{option}:{values}]\r\n'.format(
            option=option_pair[0],
            values=values)
    return line #}}}


def write_to_file(new_contents, file_path): #{{{
    """ Write text to a file. """

    f = open(file_path, 'w')
    f.write(new_contents)
    f.close() #}}}


def main(args): #{{{
    """ Read a file and look for a line containing the selected option.
        Then set the new value for that option and write it to the file.
    """

    inits = read_file(args.path)
    option_pair = parse_option(find_option(args.option, inits))
    new_option_pair = set_option_values(option_pair, args.value)
    new_option_line = make_option_line(new_option_pair)

    new_inits = []
    for line in inits:
        if new_option_pair[0] in line:
            new_inits.append(new_option_line)
        else:
            new_inits.append(line)

    new_init_contents = ''.join(new_inits)

    if new_init_contents != None:
        write_to_file(new_init_contents, args.path)
    else:
        raise ValueError #}}}


if __name__ == '__main__': #{{{
    try:
        main(get_args())
    except KeyboardInterrupt:
        sys.exit() #}}}
