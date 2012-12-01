dftools
=======

A set of command line tools for [Dwarf Fortress](http://www.bay12games.com/dwarves/).

## Download

Check the downloads page for prebuilt binaries (Linux / Windows)

## Usage

#### dfpm - Dwarf Fortress Package Manager

    Usage:
        dfpm [--directory] [--platform] install <package> <package>...
        dfpm [--directory] [--platform] remove <package> <package>...
        dfpm [--directory] [--platform] update
        dfpm [--directory] [--platform] upgrade
        dfpm [--directory] show
        dfpm -h | --help
        dfpm -l | --license
        dfpm -v | --version

    Options:
        -d --directory  Directory to install packages to.
        -p --platform   Manually set OS for OS dependent packages.

        -h --help       Display the help text.
        -l --license    Display the license
        -v --version    Disaply the version

    Examples:
        dfpm install dwarffortress
            Install Dwarf Fortress

        dfpm install dwarffortress ts-phoebus emb-lazynewbpack
            Install Dwarf Fortress, Phoebus tileset, and Lazy Newb Pack embark
            profiles.

        dfpm install ts-phoebus
            Install Phoebus tileset, will install Dwarf Fortress if it
            isn't present.

        dfpm --directory ~/foobar/ install dwarffortress
            Install Dwarf Fortress in "~/foobar/"

        dfpm --platform windows install dwarffortress
            Install the Windows version of Dwarf Fortress, even if the current
            OS is different.

        dfpm update
            Update package information.

        dfpm upgrade
            Upgrade packages.

#### dfopt - Dwarf Fortress Options

    Usage:
        dfopt [--directory] set <opt> <value>...
        dfopt [--directory] search <opt>
        dfopt [--directory] defaults
        dfopt [--directory] restore OPTSFILE
        dfopt -h | --help
        dfopt -l | --license
        dfopt -v | --version

    Options:
        -d --directory  Path to Dwarf Fortress install.

        -h --help       Display the help text.
        -l --license    Display the license
        -v --version    Disaply the version

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
