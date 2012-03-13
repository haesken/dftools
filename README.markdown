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

- [Puppet](http://puppetlabs.com/)

- Other dependencies will be handled by puppet.

## Usage
### Download

- Stable version
    - Go to the
        [tags page](https://github.com/haesken/dwarf_fortress_auto/tags)
        and download the latest tag.
- Current
    - [Download zip](https://github.com/haesken/dwarf_fortress_auto/zipball/master)
    - [Download tar.gz](https://github.com/haesken/dwarf_fortress_auto/tarball/master)

### Install dependencies:

Install script dependencies with Puppet.

    sudo puppet apply depends.pp

Note:

    The package list provided in depends.pp is for Ubuntu.
    If your are on a different platform you will need to
    install the dependencies manually.

### Run df\_install.py

    python df_install.py [options]

### df\_install.py Options

    -df,  --dwarf_fortress   : Install Dwarf Fortress
    -ph,  --phoebus          : Install Phoebus tileset
    -lze, --lazy_newb_embark : Install embark profiles from Lazy Newb Pack
    -daq, --disable_aquifers : Disable aquifers
    -dt,  --dwarf_therapist  : Install Dwarf Therapist (apt compatible platforms)

## Full dependency list
These are the packages installed via puppet, so you can find equivalents.

Dependencies for the scripts:

    python2.7
    python-lxml
    wget

Dependencies for Dwarf Fortress:

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

    ia32-libs (needed only on 64 bit systems)
