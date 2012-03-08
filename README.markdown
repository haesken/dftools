Dwarf Fortress Auto
===================

A set of scripts to download/build
Dwarf Fortress, Dwarf Therapist, and other utilities.

## Requirements

[Puppet](http://puppetlabs.com/)

[Python 2.7](http://www.python.org/)

Other dependencies will be handled by puppet.

## Usage

Install dependencies:

    sudo puppet apply scripts/scripts_depends.pp

Run df_install.py

    python df_install.py [options]

#### df\_install.py Options

* -df / --dwarf\_fortress : Install Dwarf Fortress
* -ph / --phoebus : Install Phoebus tileset
* -lze / --lazy\_newb\_embark : Install embark profiles from Lazy Newb Pack
* -dt / --dwarf\_therapist : Install Dwarf Therapist
