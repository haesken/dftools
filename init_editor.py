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

    return parser.parse_args() #}}}


def read_file(path): #{{{
    """ Read the contents of a file.
        Return the contents.
    """
    f = open(path)
    lines = f.readlines()
    f.close()
    for line in lines:
        yield line.strip('\n').strip('\r') #}}}


def parse_option(line): #{{{
    """ Parse the option line.
        Returns a tuple with the option and a list of argument values.
    """
    segments = line.strip('[').strip(']').split(':')
    option = segments[0]
    values = segments[1:]
    return (option, values) #}}}


def find_option(option_name, lines): #{{{
    """ Find a line containing the option.
        Return the line.
    """

    option_lines = [line for line in lines
            if line.startswith('[') and line.endswith(']')]

    for option_line in option_lines:
        if option_name in parse_option(option_line)[0]:
            yield option_line #}}}


def set_option_values(option_pair, new_values): #{{{
    """ Set new values for an option.
        Returns a tuple with the option and new argument values.
    """

    new_pair = (option_pair[0], new_values)
    return new_pair #}}}


def make_option_line(option_tuple): #{{{
    """ Generate a valid option line for the init file, ex: '[Population:70]'.
        Returns the new line (including '\r\n' at the end).
    """

    # If we have multiple arguments join them with a :
    if len(option_tuple[1]) > 1:
        values = ':'.join(option_tuple[1])
    else:
        values = option_tuple[1][0]

    line = '[{option}:{values}]'.format(
            option=option_tuple[0],
            values=values.upper())

    return line #}}}


def write_lines_to_file(new_contents, file_path): #{{{
    """ Write text to a file. """
    new_contents_with_newlines = [line + os.linesep for line in new_contents]

    f = open(file_path, 'w')
    f.writelines(new_contents_with_newlines)
    f.close() #}}}


def insert_modified_line(inits, option_name, new_option_line): #{{{
    """ Insert the modified line into the file. """

    new_inits = []
    for line in inits:
        if line.startswith('[') and line.endswith(']'):
            if option_name in line:
                new_inits.append(new_option_line)
            else:
                new_inits.append(line)
        else:
            new_inits.append(line)

    return new_inits #}}}


def main(args): #{{{
    """ Read a file and look for a line containing the selected option.
        Then set the new value for that option and write it to the file.
    """

    if args.search: #{{{
        inits = list(read_file(args.path))
        search_term = args.search.upper()
        search_results = list(find_option(search_term, inits))

        if len(search_results) >= 1:
            for result in search_results:
                print result
        else:
            print "Found no option containing '{option}'!".format(
                    option=search_term) #}}}

    if args.option: #{{{
        for item in args.option:
            """ Read/write the inits file on each iteration so
                the current change doesn't discard the previous
                change.
            """
            inits = list(read_file(args.path))

            option_name = item[0].upper()
            search_results = list(find_option(option_name, inits))

            # Handle bad search results {{{
            if len(search_results) == 0:
                print "Found no option containing '{option}'!".format(
                        option=option_name)
                sys.exit()

            elif len(search_results) > 1:
                print "Multiple options containing '{option_name}'!".format(
                        option_name=option_name)
                print "Use ONE option from the following:"
                for i in search_results:
                    print i
                sys.exit() #}}}

            current_option_line = search_results[0]

            # If the option actually exists
            if current_option_line != None:
                option_tuple = parse_option(current_option_line)

                new_option_tuple = set_option_values(
                        option_tuple, item[1:])

                new_option_line = make_option_line(new_option_tuple)

                new_inits = insert_modified_line(
                        inits, option_tuple[0], new_option_line)

                write_lines_to_file(new_inits, args.path)
            else:
                print "Found no option '{option}', aborting.".format(
                        option=item[0]) #}}}


if __name__ == '__main__': #{{{
    try:
        main(get_args())
    except KeyboardInterrupt:
        sys.exit() #}}}
