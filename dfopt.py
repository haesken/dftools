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
Copyright (c) 2012, haesken <haesken08@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

version = "0.4.0"

import json
import sys
from os import path, getcwd
from docopt import docopt

import lib.dftlib as dftlib


class optionsManager(object):
    def __init__(self, path_root_dir, path_config):
        """ Set up paths and file objects to use. """

        self.config = json.loads(dftlib.read(path_config))
        self.path_defaults = self.config["paths"]["dirs"]["defaults"]

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

    def _join_option_values(self, values):
        """ If values is a list of values, join then with a ":".
            Else if values is a str, just return it.
        """
        if type(values) == list:
            return ":".join(values)
        elif type(values) == str:
            return values

    def _make_option(self, option, values):
        """ Format an option and its new values for use in the inits file.
            Uses the format: [OPTION:VALUE], or [OPTION:VALUE:VALUE]
        """

        return "[{option}:{value}]".format(
                option=option, value=self._join_option_values(values))

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

    def _prep_json_option(self, option, values):
        return list(option, self._join_option_values(values))

    def _get_opts_from_file(self, path_optsfile):
        return json.loads(dftlib.read(path_optsfile))

    def _set_opts_from_json(self, opts_json):
        for key in opts_json.iterkeys():
            self.setopt(key, opts_json[key])

    def defaults(self):
        self._set_opts_from_json(self._get_opts_from_file(self.path_defaults))

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

    if args["--config"] is not None:
        path_config = args["--config"]
    else:
        path_config = "dfopt.conf"

    options = optionsManager(path_root_dir, path_config)

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
        options.defaults()

    if args["backup"]:
        options.backup(args["OPTSFILE"])

    if args["restore"]:
        options.restore(args["OPTSFILE"])


if __name__ == '__main__':
    try:
        main(docopt(__doc__))
    except KeyboardInterrupt:
        sys.exit()
