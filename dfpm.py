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
    -c --config CONFIGFILE  Use a different config file.

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

from os import getcwd, path
from docopt import docopt
import json
import sys

import lib.dftlib as dftlib


class package(object):
    """ """

    def __init__():
        pass

    def get_manifest():
        manifest = json.loads(dftlib.get_url())

    def status():
        pass

    def verify():
        pass

    def extract():
        pass

    def symlink():
        pass

    def install():
        pass


class packageManager(object):
    def __init__(self, path_root_dir, platform, path_config):
        """ Set up paths and file objects to use. """

        self.df_paths = dftlib.make_df_paths(path_root_dir, platform)
        self.platform = platform
        self.config = json.loads(open(path_config, "r").read())
        self.workdir = self.config["paths"]["dirs"]["work"]
        self.pkg_list = path.join(self.workdir,
                self.config["paths"]["files"]["pkg_list"])

    def _pkgs_update_available(self):
        """ If avilable packages.json doesn't exist, download it.

            If it does exist download a fresh copy, and if the
            versions differ, write the contents of the new file
            to the old one.
        """

        dftlib.ensure_dir(self.workdir)
        pkgs_web = dftlib.get_url(self.config["urls"]["pkg_list"])

        if not path.exists(path.join(self.workdir, self.pkg_list)):
            dftlib.write(self.pkg_list, pkgs_web)
        else:
            pkgs_new = json.loads(pkgs_web)
            pkgs_cur = json.loads(dftlib.read(
                path.join(self.workdir, self.pkg_list)))

            if int(pkgs_new["version"]) > int(pkgs_cur["version"]):
                dftlib.write(self.pkg_list, json.dumps(pkgs_new))

    def _pkgs_get_available(self):
        """ If there is no package list in the working dir, download one."""

        if not path.exists(self.pkg_list):
            self._pkgs_update_available()

        return json.loads(dftlib.read(self.pkg_list))

    def install(self, package_names):
        dftlib.ensure_dir(self.workdir)
        pkgs_avail = self._pkgs_get_available()

        for package_name in package_names:
            if package_name in pkgs_avail:
                pkg = package(package_name)
                if pkg.status() == "installed":
                    pass


        """
        If the package tar is not present, download it.
        Read package manifest.
        Verify the checksum provided in the manifest.

        if the checksum is correct:
            Extract the archive.
            Symlink the extracted files.

            if symlinking succeeded:
                read init options from manifest
                set options/values listed in manifest

        else:
            raise checksum exception
        """

    def remove(self, package_names):
        pass

    def update(self):
        self._pkgs_update_available()

    def upgrade(self, package_names):
        pass

    def show(self, package_names):
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

    if args["--config"] is not None:
        path_config = args["--config"]
    else:
        path_config = "dfpm.conf"

    manage = packageManager(path_root_dir, platform, path_config)

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
