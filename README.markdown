Dwarf Fortress Auto
===================

A set of scripts to download and install
Dwarf Fortress and Dwarf Therapist, with a few included utilities.

## Requirements

- [Puppet](http://puppetlabs.com/)

- Other dependencies will be handled by puppet.

## Usage
### Install dependencies:

    sudo puppet apply depends.pp

Note:

    The package list provided in depends.pp is for Ubuntu.
    If your are on a different platform you will need to
    install the dependencies manually.


### Run df\_install.py

    python df_install.py [options]

## df\_install.py Options

Install Dwarf Fortress

    -df, --dwarf_fortress

Install Phoebus tileset

    -ph, --phoebus

Install embark profiles from Lazy Newb Pack

    -lze, --lazy_newb_embark

Disable aquifers

    -daq, --disable_aquifers

Install Dwarf Therapist (apt compatible platforms)

    -dt, --dwarf_therapist
