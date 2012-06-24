Dwarf Fortress Auto
===================

A set of scripts to download and install Dwarf Fortress a few utilities.

## Attribution

This program uses materials from the
[Lazy Newb Pack](http://www.bay12forums.com/smf/index.php?topic=59026.0).

Specifically it includes the provided embark profiles, which
were originally authored by
[LucasUP](http://www.funkybomp.com/),
[captnduck](https://www.youtube.com/user/captnduck), and
[Mike Mayday](http://mayday.w.staszic.waw.pl/df.php).


## Usage
### Download

- Check the Downloads page for prebuilt binaries (Linux/OSX/Windows)

### Run

- Linux/OSX
    - Run either of these in a terminal.

        `./df_install -h`

        `./init_options -h`

- Windows
    - Open a command prompt in the dwarf_fortress_auto dir and run:

        `df_install.exe -h`

        `init_options.exe -h`

#### df\_install

    Usage: ./df_install [options]

    -h,   --help             : Display the help text.
    -d,   --directory        : Directory to install Dwarf Fortress to.
    -p,   --platform         : Override OS detection.

        This will override the OS detection and
        let you specify what version of DF to use
        (Linux/OSX/Windows).

        This is useful if you want to install a different
        OS's version of DF.

    -df,  --dwarf_fortress   : Install Dwarf Fortress.
    -t,   --tileset          : Install a tileset

        Example:
            Install the Phoebus tileset: -t phoebus

        Available tilesets:
            Phoebus                                : phoebus
            Jolly Bastion 9x12                     : jolly9
            Jolly Bastion 12x12                    : jolly12
            Jolly Bastion 12x12 (With curses font) : jollycurses
            Mayday                                 : mayday

    -e,   --embarks          : Install embark profiles

        Example:
            Install Lazy Newb Pack embark profiles: -e lnp

        Available embark profiles:
            Lazy Newb Pack   : lnp
            Mayday           : mayday

    -aq,  --aquifers         : Enable/disable aquifers

        Example:
            Disable aquifers : -aq disable
        Available modes:
            Enable           : enable
            Disable          : disable

    -dfh, --dfhack           : Install DFHack
    -q,   --quick            : Quick install

        Equivalent to '-df -t phoebus -e lnp -aq disable'

    -l,  --license           : Display the license
    -v,  --version           : Disaply the version


#### init\_editor
    Usage: python init_editor [options]

    -p,   --path             : Path to the config file to write to.
    -s,   --search           : Search for an option.

        Example:
            Search for POPULATION_CAP : -s population_cap

    -o,   --option           : Option to change.

        Examples:
            Set POPULATION_CAP to 80   : -o population_cap 80
            Set BABY_CHILD_CAP to 0:10 : -o baby_child_cap 0 10

        This option can be repeated, example:
            -o population_cap 80 -o baby_child_cap 0 10

    -r,   --restore          : Restore custom options from a file.

        Examples:
            Restore values from 'foo.txt' : -r foo.txt

        This option will read options from a file and write
        the values to the selecte file.

        The format/syntax for the restore file is the same
        as the Dwarf Fortress config file, and two examples
        are included. (custom_d_init.txt, custom_init.txt)

    -l,   --license          : Display the license
