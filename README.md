dftools
=======

A set of command line tools for [Dwarf Fortress](http://www.bay12games.com/dwarves/).

## Usage

#### dfpm - Dwarf Fortress Package Manager

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

#### dfopt - Dwarf Fortress Options

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

#### dfsg - Dwarf Fortress Save Game (tool)

    Usage:
        dfsg [--directory] backup WORLD BACKUPDIR
        dfsg [--directory] backup all BACKUPDIR
        dfsg [--directory] restore WORLD BACKUPDIR
        dfsg [--directory] restore all BACKUPDIR
        dfsg -h | --help
        dfsg -l | --license
        dfsg -v | --version

    Options:
        -d --directory  Path to Dwarf Fortress install.

        -h --help       Display the help text.
        -l --license    Display the license
        -v --version    Disaply the version

    Examples:
        dfsg backup region1 ~/dfbackups
            Backs up world "region1" to "~/dfbackups"

        dfsg backup all ~/dfbackups
            Backs up all worlds to "~/dfbackups"

        dfsg --directory ~/df backup region1 ~/dfbackups
            Backs up world "region1" from "~/df" to "~/dfbackups"

        dfsg restore region1 ~/dfbackups
            Restores world "region1" from "~/dfbackups"

        dfsg restore  all ~/dfbackups
            Restores all worlds from "~/dfbackups"

        dfsg --directory ~/df restore region1 ~/dfbackups
            Restores world "region1" from "~/dfbackups" to "~/df"

## Attribution

This program uses materials from the
[Lazy Newb Pack](http://www.bay12forums.com/smf/index.php?topic=59026.0).

It also includes embark profiles, which were originally authored by
[LucasUP](http://www.funkybomp.com/),
[captnduck](https://www.youtube.com/user/captnduck), and
[Mike Mayday](http://mayday.w.staszic.waw.pl/df.php).



