#!/usr/bin/env bash
sudo puppet apply develop/depends/ubuntu_packages.pp

git submodule update --init

virtualenv --no-site-packages .virtualenv
source .virtualenv/bin/activate
pip install -r develop/depends/python-modules.txt
