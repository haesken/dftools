#!/usr/bin/env python
# encoding: utf-8

""" dfpm

Usage:
    dfpm [--directory DIR] [--platform PLATFORM] update
    dfpm [--directory DIR] [--platform PLATFORM] install <package>...
    dfpm [--directory DIR] [--platform PLATFORM] remove <package>...
    dfpm [--directory DIR] [--platform PLATFORM] upgrade [<package>...]
    dfpm [--directory DIR] [--platform PLATFORM] show [<package>...]
    dfpm -h | --help
    dfpm -l | --license
    dfpm -v | --version

Options:
    -d --directory DIR      Directory to install packages to.
    -p --platform PLATFORM  Override platform detection.
                            Valid values: linux / osx / windows

    -h --help               Display the help text.
    -l --license            Display the license
    -v --version            Disaply the version

Examples:
    dfpm install dwarffortress
        Install Dwarf Fortress.

    dfpm install dwarffortress phoebus lazynewbpack
        Install Dwarf Fortress, Phoebus tileset, and Lazy Newb Pack embark
        profiles.

    dfpm install phoebus
        Install Phoebus tileset, will install Dwarf Fortress if it
        isn't present.

    dfpm --directory ~/foobar/ install dwarffortress
        Install Dwarf Fortress in "~/foobar/".

    dfpm --platform windows install dwarffortress
        Install the Windows version of Dwarf Fortress, even if the current
        OS is different.

    dfpm update
        Check for updates to packages.

    dfpm upgrade
        Upgrade all packages.

    dfpm upgrade dwarffortress
        Upgrade only Dwarf Fortress.

    dfpm upgrade dwarffortress phoebus
        Upgrade Dwarf Fortress and Phoebus packages.

    dfpm show
        Show package information for all installed packages.

    dfpm show dwarffortress
        Show package information for package "dwarffortress"

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

from os import path, getcwd
from docopt import docopt
import sys

sys.path.append("modules/")
import dftlib


class packageManager(object):
    def __init__(self, path_root_dir, platform):
        """ Set up paths and file objects to use. """

        self.df_paths = dftlib.make_df_paths(path_root_dir, platform)
        self.platform = platform

    def install(package_name):
        pass

    def remove(package_name):
        pass

    def update():
        pass

    def upgrade(package_name):
        pass

    def show(package_name):
        pass


def main(args):
    """ Run selected options. """

    if args["--license"]:
        print(license)
        sys.exit()

    if args["--version"]:
        print(version)
        sys.exit()

    if args["--platform"] is not None:
        platform = args["--platform"]
    else:
        platform = dftlib.detect_platform()

    if args["--directory"] is not None:
        path_root_dir = args["--directory"]
    else:
        path_root_dir = getcwd()

    manage = packageManager(path_root_dir, platform)

    if args["install"]:
        manage.install(args["<package>"])

    if args["remove"]:
        manage.remove(args["<package>"])

    if args["update"]:
        manage.update()

    if args["upgrade"]:
        manage.upgrade(args["<package>"])

    if args["show"]:
        manage.show(args["<package>"])

if __name__ == '__main__':
    try:
        main(docopt(__doc__))
    except KeyboardInterrupt:
        sys.exit()
