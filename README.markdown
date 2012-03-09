Dwarf Fortress Auto
===================

A set of scripts to download/build
Dwarf Fortress, Dwarf Therapist, and other utilities.

## Requirements

* [Puppet](http://puppetlabs.com/)

Other dependencies will be handled by puppet.

## Usage

Install scripts dependencies:

    sudo puppet apply scripts/scripts_depends.pp

Run df_install.py

    python df_install.py [options]

#### df\_install.py Options

Install Dwarf Fortress

    -df, --dwarf_fortress

Install Phoebus tileset

    -ph, --phoebus

Install embark profiles from Lazy Newb Pack

    -lze, --lazy_newb_embark

Set init.txt/d\_init.txt options

    -ino, --init_options

Disable aquifers

    -daq, --disable_aquifers

Install Dwarf Therapist

    -dt, --dwarf_therapist
