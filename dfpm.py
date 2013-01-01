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

from os import getcwd, path
from docopt import docopt
import json
import requests
import sys

sys.path.append("lib")
import dftlib


class packageManager(object):
    def __init__(self, path_root_dir, platform, path_config):
        """ Set up paths and file objects to use. """

        self.df_paths = dftlib.make_df_paths(path_root_dir, platform)
        self.platform = platform
        self.config = json.loads(open(path_config, "r").read())

    def _download_url(self, url):
        resp = requests.get(url)
        if resp.status_code == requests.codes.ok:
            return resp.content

    def _pkgs_download_available(self):
        """ Download the list of available packages. """
        return self._download_url(self.config["urls"]["pkg_list"])

    def _pkgs_update_available(self):
        """ If avilable packages.json doesn't exist, download it.

            If it does exist download a fresh copy, and if the
            versions differ, write the contents of the new file
            to the old one.
        """

        if not path.exists(self.config["paths"]["files"]["pkg_list"]):
            dftlib.write(self.config["paths"]["files"]["pkg_list"],
                         self._pkgs_download_available())
        else:
            pkgs_new = json.dumps(self._pkgs_download_available())
            pkgs_cur = json.dumps(dftlib.read(
                    self.config["paths"]["files"]["pkg_list"]))

            if int(pkgs_new["version"]) > int(pkgs_cur["version"]):
                dftlib.write(self.pkgs_cur_path, pkgs_new)

    def _pkgs_get_available(self):
        """ If there is no package list in the working dir, download one."""

        if not path.exists(self.config["paths"]["files"]["pkg_list"]):
            self._pkgs_update_available()

        return json.dumps(dftlib.read(
            self.config["paths"]["files"]["pkg_list"]))

    def install(self, package_name):
        pkgs_avail = self._pkgs_get_available()

        dftlib.ensure_dir(self.config["paths"]["dirs"]["tmp"])

        pass
        """
        If the package manifest is not present, download it.
        If the package tar is not present, download it.
        Read package manifest.
        Verify the checksum provided in the manifest.

        if the checksum is correct:
            Extract the archive.
            Symlink the extracted files.

            if symlinking succeeded:
                read init options from manifest

        else:
            raise checksum exception
        """

    def remove(self, package_name):
        pass

    def update(self):
        self._pkgs_update_available()

    def upgrade(self, package_name):
        pass

    def show(self, package_name):
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
