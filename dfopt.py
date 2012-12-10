#!/usr/bin/env python
# encoding: utf-8

""" dfopt - Dwarf Fortress Options

Usage:
    dfopt [--directory DIR] set (<opt> <value>)...
    dfopt [--directory DIR] search (<opt>)
    dfopt [--directory DIR] defaults
    dfopt [--directory DIR] backup OPTSFILE
    dfopt [--directory DIR] restore OPTSFILE
    dfopt -h | --help
    dfopt -l | --license
    dfopt -v | --version

Options:
    -d --directory DIR  Path to Dwarf Fortress install.

    -h --help           Display the help text.
    -l --license        Display the license
    -v --version        Disaply the version

Examples:
    dfopt search population
        Search the configs for variables containing "population".

    dfopt set population_cap 80
        Set POPULATION_CAP to 80

    dfopt set baby_child_cap 0:10
        Set BABY_CHILD_CAP to 0:10

    dfopt set population_cap 80 baby_child_cap 0:10
        Set multiple values at once.

    dfopt restore file.json
        Read a json file containing saved options and values,
        then set the game's options to those values.
"""

license = """
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

import collections
import os
import sys
from docopt import docopt


def read_lines(path):
    """ Read the contents of a file.
        Return the contents.
    """

    f = open(path)
    lines = f.readlines()
    f.close()

    return [line.strip("\n").strip("\r") for line in lines]


def write_lines(new_contents, file_path):
    """ Write text to a file. """

    f = open(file_path, "w")
    f.writelines([line + os.linesep for line in new_contents])
    f.close()


def parse_option_line(line):
    """ Parse the option line.
        Returns a tuple with the option and a list of argument values.
    """

    return line.strip("[").strip("]").split(":")


def find_option_line(option_name, lines):
    """ Find a line containing the option.
        Return the line.
    """

    for line in lines:
        if line.startswith("[") and line.endswith("]"):
            # The search term must be exactly equal to the name of the option.
            if option_name == parse_option_line(line)[0]:
                yield line


def make_option_line(option_list):
    """ Generate a valid option line for the init file.
        Example: "[Population:70]"
    """

    option_name, option_values = option_list[0], option_list[1:]

    # If we have multiple arguments join them with a :
    if len(option_values) > 1:
        new_values = ":".join(option_values)
    else:
        new_values = option_values[0]

    return "[{option}:{values}]".format(
            option=option_name, values=new_values.upper())


def insert_option_line(inits, option_name, new_option_line):
    """ Insert the modified line into the file. """

    for line in inits:
        if (line.startswith("[") and line.endswith("]") and
                option_name == parse_option_line(line)[0]):
            yield new_option_line
        else:
            yield line


def search_inits(inits_path, search_term):
    """ Search for an option in a config file. """

    inits = read_lines(inits_path)
    search_results = list(find_option_line(search_term, inits))

    if len(search_results) != 0:
        for result in search_results:
            yield result
    else:
        yield "Found no option {option}!".format(
                option=search_term)


def set_option(option, inits_path):
    """ Read a file and look for a line containing the selected option,
        then set the new value for that option and write it to the file.
    """

    inits = read_lines(inits_path)

    option_name = option[0]
    search_results = list(find_option_line(option_name, inits))

    # Handle bad search results {{{
    if len(search_results) == 0:
        print "Found no option {option}!".format(
                option=option_name)
        sys.exit()


    current_option_line = search_results[0]
    option_list = parse_option_line(current_option_line)

    new_option_list = list(flatten_iterable((option_list[0], option[1:])))
    new_option_line = make_option_line(new_option_list)

    new_inits = insert_option_line(inits, option_name, new_option_line)

    write_lines(new_inits, inits_path)


def restore_options(restore_inits_path, inits_path):
    """ Restore custom options from a file. """

    restore_file_options = [parse_option_line(option)
            for option in read_lines(restore_inits_path)]

    for option in restore_file_options:
        set_option(process_option(option), inits_path)


def flatten_iterable(an_iterable):
    """ Flatten a nested iterable. """

    for element in an_iterable:
        if (isinstance(element, collections.Iterable) and not
                isinstance(element, basestring)):

            for sub_element in flatten_iterable(element):
                yield sub_element
        else:
            yield element


def uppercase_args(option):
    """ Uppercase each item in a list. """

    return [arg.upper() for arg in option]


def process_option(option):
    """ Flatten a list and uppercase each element. """

    return list(uppercase_args(flatten_iterable(option)))


def main(args):
    """ Run selected functions. """

    if args.search_term:
        for result in list(
                search_inits(args.inits_path, args.search_term.upper())):
            print result

    if args.options_list:
        """ Read/write the inits file on each iteration so
            the current change doesn"t discard the previous
            change.
        """
        for option in args.options_list:
            set_option(process_option(option), args.inits_path)

    if args.restore_inits_path:
        restore_options(args.restore_inits_path, args.inits_path)

    if args["--license"]:
        print(license)

    if args["--version"]:
        print(version)


if __name__ == '__main__':
    try:
        main(docopt(__doc__))
    except KeyboardInterrupt:
        sys.exit()
