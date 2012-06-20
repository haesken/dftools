#!/usr/bin/env bash
sudo apt-get install libxslt1-dev libxml2-dev

virtualenv --no-site-packages .virtualenv
source .virtualenv/bin/activate

pip install -r develop/python-depends/requirements.txt
