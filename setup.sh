#!/usr/bin/env bash

virutalenv --no-site-packages .virtualenv
source .virtualenv/bin/activate

pip install -r develop/python-depends/requirements.txt
pip install -r develop/python-depends/urlgrabber.txt
