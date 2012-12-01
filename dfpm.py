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
    -d --directory DIR      Directory to install packages to. [default: ./]
    -p --platform PLATFORM  Override platform. [default: detect]
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
import dfpm_interface


def detect_platform():
    """ Detect what platform we are running on. """
    if "linux" in sys.platform:
        return "linux"
    elif "darwin" in sys.platform:
        return "osx"
    # Includes cygwin
    elif "win" in sys.platform:
        return "windows"


def main(args):
    """ Run selected options. """

    if args["--platform"] == "detect":
        platform = detect_platform()
    else:
        platform = args["--platform"]

    if args["--directory"]:
        path_root_dir = args["--directory"]
    else:
        path_root_dir = getcwd()

    # Actual Dwarf Fortress install directory.
    name_df_main = "df_{platform}".format(platform=platform)
    path_df_main = path.join(path_root_dir, name_df_main)

    df_paths = {
            "df_root": path_root_dir,
            "df_main": path_df_main,
            "df_data": path.join(path_df_main, "data/"),
            "df_inits": path.join(path_df_main, "data/init"),
            "df_raw": path.join(path_df_main, "raw/"),
            "df_objects": path.join(path_df_main, "raw/objects"),
            "df_libs": path.join(path_df_main, "libs"),
            }

    if args["install"]:
        dfpm_interface.install(platform, df_paths, args["<package>"])

    if args["remove"]:
        dfpm_interface.remove(platform, df_paths, args["<package>"])

    if args["update"]:
        dfpm_interface.update(platform, df_paths)

    if args["upgrade"]:
        dfpm_interface.upgrade(platform, df_paths, args["<package>"])

    if args["show"]:
        dfpm_interface.show(platform, df_paths, args["<package>"])

    if args["--license"]:
        print(license)

    if args["--version"]:
        print(version)

if __name__ == '__main__':
    try:
        main(docopt(__doc__))
    except KeyboardInterrupt:
        sys.exit()
