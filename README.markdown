Dwarf Fortress Auto
===================

A set of scripts to download and install Dwarf Fortress and
Dwarf Therapist, with a few included utilities.

## Attribution

This program uses materials from the
[Lazy Newb Pack](http://www.bay12forums.com/smf/index.php?topic=59026.0).

Specifically it includes the provided embark profiles, which
were originally authored by
[LucasUP](http://www.funkybomp.com/),
[captnduck](https://www.youtube.com/user/captnduck), and
[Mike Mayday](http://mayday.w.staszic.waw.pl/df.php).


## Requirements

- [Pip](www.pip-installer.org)
- Dwarf Fortress' dependencies (found at the end of this readme)

## Usage
### Download

- Stable version (Recommended)
    - Go to the
        [tags page](https://github.com/haesken/dwarf_fortress_auto/tags)
        and download the latest tag.

### Install

    ./setup.sh

#### df\_install.py
    Usage: python df_install.py [options]

    -dir, --directory        : Directory to install Dwarf Fortress to.
    -df,  --dwarf_fortress   : Install Dwarf Fortress
    -t,   --tileset          : Install tilesets

        Example:
            Install Phoebus tileset: -t phoebus

        Available tilesets:
            Phoebus          : phoebus
            Mayday           : mayday
            Jolly Bastion    : jollybastion
            ASCII (Square)   : asciisquare
            Default          : default

    -e,   --embarks          : Install embark profiles

        Example:
            Install Lazy Newb Pack embark profiles: -e lnp

        Available embark profiles:
            Lazy Newb Pack   : lnp
            Default          : default

    -aq,  --aquifers         : Enable/disable aquifers

        Example:
            Disable aquifers : -aq disable
        Available modes:
            Enable           : enable
            Disable          : disable

    -dfh, --dfhack           : Install DFHack
    -q,   --quick            : Quick install

        Equivalent to '-df -t phoebus -e lnp -aq disable'


#### init\_editor.py
    Usage: python init_editor.py [options]

    -p,   --path             : Path to the config file to write to.
    -s,   --search           : Search for an option.

        Examples:
            Search for POPULATION : -s pop
            Search for BABY_CHILD_CAP : -s child

    -o,   --option           : Option to change.

        Examples:
            Set POPULATION_CAP to 80   : -o population 80
            Set BABY_CHILD_CAP to 0:10 : -o child 0 10

        This option can be repeated, example:
            -o population 80 -o child 0 10

    -r,   --restore          : Restore custom options from a file.

        Examples:
            Restore values from 'foo.txt' : -r foo.txt

        This option will read options from a file and write
        the values to the selecte file.

        The format/syntax for the restore file is the same
        as the Dwarf Fortress config file, and two examples
        are included. (custom_d_init.txt, custom_init.txt)


## Dependency list
Dependencies for Dwarf Fortress (Ubuntu packages):

    ncurses-base
    libncurses5
    libncurses5-dev
    libsdl1.2debian-all
    libsdl1.2-dev
    libsdl-image1.2
    libsdl-image1.2-dev
    libglu1-mesa
    libglu1-mesa-dev
    libgtk2.0-0
    libgtk2.0-dev
    libopenal1
    libopenal-dev

    ia32-libs (only needed on 64 bit systems)
