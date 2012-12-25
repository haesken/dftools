#!/usr/bin/env python
# encoding: utf-8

""" dfopt - Dwarf Fortress Options

Usage:
    dfopt [--directory DIR] search (<opt>)
    dfopt [--directory DIR] set (<opt> <value>)...
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

    dfopt restore OPTSFILE
        Read a file containing saved options and values,
        then set the game's options to those values.

        This uses the same format as Dwarf Fortress's init files, eg:
        "[OPTION:VALUE]" or "[OPTION:VALUE:VALUE]"
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

version = "0.4.0"

import sys
from os import path, getcwd
from docopt import docopt

sys.path.append("modules")
import dftlib


class optionsManager(object):
    def __init__(self, path_root_dir):
        """ Set up paths and file objects to use. """

        self.df_paths = dftlib.make_df_paths(path_root_dir, "linux")
        self.path_inits = path.join(self.df_paths["init"], "init.txt")
        self.path_d_inits = path.join(self.df_paths["init"], "d_init.txt")

        self.inits = dftlib.read_lines(self.path_inits)
        self.d_inits = dftlib.read_lines(self.path_d_inits)

    def _parse_option(self, line):
        """ Parse an option line.
            Return the option's name as a str,
            and the values as a list of strings.
        """

        line_bare = line.lstrip("[").rstrip("]")
        return line_bare.split(":")[0], line_bare.split(":")[1:]

    def _make_option(self, option, values):
        """ Format an option and its new values for use in the inits file.
            Uses the format: [OPTION:VALUE], or [OPTION:VALUE:VALUE]
        """

        if type(values) == list:
            value = ":".join(values)
        else:
            value = values

        return "[{option}:{value}]".format(option=option, value=value)

    def _replace_option(self, option, values, lines, line_number):
        """ Overwrite the selected line with one containing the new value. """

        lines[line_number] = self._make_option(option, values)
        return lines

    def _get_inits_name_and_line_num(self, line):
        """ If the provide line is in one of the inits file,
            return the name of that inits file and the line number.

            This is to make these two files appear as one "set" of options
            to the user.
        """

        if line in self.inits:
            return "inits.txt", self.inits.index(line), line
        elif line in self.d_inits:
            return "d_inits.txt", self.inits.index(line), line

    def search(self, option, fuzzy):
        """ Search for an option.

            If fuzzy is True, will return any option that
            contains the search string.

            If fuzzy is False, will only return exact
            matches for the search term.
        """

        for item in [self.inits, self.d_inits]:
            for line in item:
                if fuzzy:
                    if line.startswith("[") and option in line:
                        yield self._get_inits_name_and_line_num(line)
                elif not fuzzy:
                    if line.startswith("[") and option in line:
                        # Only accept exact matches.
                        if self._parse_option(line)[0] == option:
                            yield self._get_inits_name_and_line_num(line)

    def setopt(self, option, values):
        """ Set a new value for an option. """

        self.results = list(self.search(option, False))

        if len(self.results) == 0:
            print("Option not found!")
        elif len(self.results) > 2:
            print("Too many options containing that query!")
        elif len(self.results) == 1:
            if self.results[0][0] == "inits.txt":
                dftlib.write_lines(self.path_inits, self._replace_option(
                        option, values, self.inits, self.results[0][1]))

            elif self.results[0][0] == "d_inits.txt":
                dftlib.write_lines(self.path_d_inits, self._replace_option(
                        option, values, self.d_inits, self.results[0][1]))

    def backup(self, path_optsfile):
        pass

    def restore(self, path_optsfile):
        self.optsfile = dftlib.read_lines(path_optsfile)
        for line in self.optsfile:
            if line.startswith("["):
                self.setopt(
                        self._parse_option(line)[0],
                        self._parse_option(line)[1])


def main(args):
    """ Run selected options. """

    if args["--license"]:
        print(license)
        sys.exit()

    if args["--version"]:
        print(version)
        sys.exit()

    if args["--directory"] is not None:
        path_root_dir = args["--directory"]
    else:
        path_root_dir = getcwd()

    options = optionsManager(path_root_dir)

    if args["search"]:
        for term in args["<opt>"]:
            for result in options.search(term.upper(), True):
                print(result[2])

    if args["set"]:
        # Set one option at a time.
        for option in args["<opt>"]:
            options.setopt(
                    option.upper(),
                    # Unpack in pairs by using the option name's index
                    # as the value's index.
                    args["<value>"][args["<opt>"].index(option)].upper())

    if args["defaults"]:
        options.restore("default")

    if args["backup"]:
        options.backup(args["OPTSFILE"])

    if args["restore"]:
        options.restore(args["OPTSFILE"])


if __name__ == '__main__':
    try:
        main(docopt(__doc__))
    except KeyboardInterrupt:
        sys.exit()
