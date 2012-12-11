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

version = "0.4.0"

import sys
from os import path, getcwd
from docopt import docopt

sys.path.append("modules")
import dftlib


class optionsManager(object):
    def __init__(self, path_root_dir):
        self.df_paths = dftlib.make_df_paths(path_root_dir, "linux")

        self.inits = dftlib.read_lines(
                path.join(self.df_paths["init"], "init.txt"))
        self.d_inits = dftlib.read_lines(
                path.join(self.df_paths["init"], "d_init.txt"))

    def _parse_option(self, option):
        return option.split(":")[0], option.split(":")[1:]

    def _make_option(self, option, values):
        if len(values) > 1:
            value = ":".join(values)
        else:
            value = values

        return "[{option}:{value}]".format(option=option, value=value)

    def search(self, option):
        """ Search for an option. """

        for item in [self.inits, self.d_inits]:
            for line in item:
                if line.startswith("[") and option in line:
                    if line in self.inits:
                        yield ("inits", line)
                    elif line in self.d_inits:
                        yield ("d_inits", line)

    def setopt(self, option, values):
        """ Set a new value for an option. """

        self.results = list(self.search(option))

        if len(self.results) == 0:
            print("Option not found!")
        elif len(self.results) > 2:
            print("Too many options containing that query!")
        elif len(self.results) == 1:
            self.option_line_new = self._make_option(option, values)

    def backup(self, path_optsfile):
        pass

    def restore(self, path_optsfile):
        pass


def main(args):
    """ Run selected functions. """

    if not args["--directory"] == None:
        path_root_dir = args["--directory"]
    else:
        path_root_dir = getcwd()

    options = optionsManager(path_root_dir)

    if args["search"]:
        for term in args["<opt>"]:
            for result in options.search(term.upper()):
                print(result[1])

    if args["set"]:
        # Set one option at a time.
        for option in args["<opt>"]:
            # Unpack the pairs by using the option name's index
            # as the value's index.
            options.setopt(
                    option.upper(),
                    args["<value>"][args["<opt>"].index(option)].upper())

    if args["defaults"]:
        options.restore("default")

    if args["backup"]:
        options.backup(args["OPTSFILE"])

    if args["restore"]:
        options.restore(args["OPTSFILE"])

    if args["--license"]:
        print(license)

    if args["--version"]:
        print(version)


if __name__ == '__main__':
    try:
        main(docopt(__doc__))
    except KeyboardInterrupt:
        sys.exit()
