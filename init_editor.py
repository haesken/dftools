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
import os
import sys


def get_args(): #{{{
    """ Get arguments from the command line. """

    parser = argparse.ArgumentParser(
            description="Set options in a Dwarf Fortress init file.",
            formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-p", "--path",
            type=str,
            required=True,
            help="Path to the Dwarf Fortress init.txt/d_init.txt file")

    parser.add_argument("-o", "--option",
            type=str,
            action='append',
            nargs='*',
            help="Option/value pair to set.\n" +
                 "Examples:\n" +
                 "    population 80\n" +
                 "    embark_rectangle 4 4")

    parser.add_argument("-s", "--search",
            type=str,
            help="Search for an option.")

    parser.add_argument("-c", "--custom",
            type=str,
            help="Path to file to load options from.")

    return parser.parse_args() #}}}


def read_lines(path): #{{{
    """ Read the contents of a file.
        Return the contents.
    """

    f = open(path)
    lines = f.readlines()
    f.close()

    for line in lines:
        yield line.strip('\n').strip('\r') #}}}


def write_lines(new_contents, file_path): #{{{
    """ Write text to a file. """

    f = open(file_path, 'w')
    f.writelines([line + os.linesep for line in new_contents])
    f.close() #}}}


def parse_option_line(line): #{{{
    """ Parse the option line.
        Returns a tuple with the option and a list of argument values.
    """
    segments = line.strip('[').strip(']').split(':')
    option = segments[0]
    values = segments[1:]
    return (option, values) #}}}


def find_option_line(option_name, lines): #{{{
    """ Find a line containing the option.
        Return the line.
    """

    option_lines = [line for line in lines
            if line.startswith('[') and line.endswith(']')]

    for option_line in option_lines:
        if option_name in parse_option_line(option_line)[0]:
            yield option_line #}}}


def make_option_line(option_tuple): #{{{
    """ Generate a valid option line for the init file.
        Example: '[Population:70]'.
    """

    option_name = option_tuple[0]
    option_values = option_tuple[1:]

    # If we have multiple arguments join them with a :
    if len(option_values) > 1:
        new_values = ':'.join(option_values)
    else:
        new_values = option_values[0][0]

    return '[{option}:{values}]'.format(
            option=option_name,
            values=new_values.upper()) #}}}


def insert_option_line(inits, option_name, new_option_line): #{{{
    """ Insert the modified line into the file. """

    for line in inits:
        if line.startswith('[') and line.endswith(']') and option_name in line:
            yield new_option_line
        else:
            yield line #}}}


def search_inits(inits_path, search_term): #{{{
    """ Search for an option in a config file. """

    inits = list(read_lines(inits_path))
    search_results = list(find_option_line(search_term.upper(), inits))

    if len(search_results) != 0:
        for result in search_results:
            yield result
    else:
        yield "Found no option containing '{option}'!".format(
                option=search_term) #}}}


def set_option(option, inits_path): #{{{
    """ Read a file and look for a line containing the selected option,
        then set the new value for that option and write it to the file.
    """

    inits = list(read_lines(inits_path))

    option_name = option[0].upper()
    search_results = list(find_option_line(option_name, inits))

    # Handle bad search results {{{
    if len(search_results) == 0:
        print "Found no option containing '{option}'!".format(
                option=option_name)
        sys.exit()

    elif len(search_results) > 1:
        print "Multiple options containing '{option_name}'!".format(
                option_name=option_name)
        print "Use ONE option from the following:"
        for result in search_results:
            print result
        sys.exit() #}}}

    current_option_line = search_results[0]
    option_tuple = parse_option_line(current_option_line)

    new_option_tuple = (option_tuple[0], option[1:])
    new_option_line = make_option_line(new_option_tuple)

    new_inits = insert_option_line(
            inits, option_tuple[0], new_option_line)

    import ipdb; ipdb.set_trace()

    write_lines(new_inits, inits_path) #}}}


def custom_options(custom_options_path): #{{{
    """ Restore custom options from a file. """
    custom_options = [option.strip('[').strip(']').split(':')
            for option in list(read_lines(custom_options_path))]

    for option in custom_options:
        set_option(option, custom_options_path) #}}}


def main(args): #{{{
    """ Run selected functions. """

    if args.search:
        for result in list(search_inits(args.path, args.search)):
            print result

    if args.option:
        """ Read/write the inits file on each iteration so
            the current change doesn't discard the previous
            change.
        """
        for option in args.option:
            set_option(option, args.path)

    if args.custom:
        custom_options(args.custom) #}}}


if __name__ == '__main__': #{{{
    try:
        main(get_args())
    except KeyboardInterrupt:
        sys.exit() #}}}
