#!/usr/bin/env bash

virutalenv --no-site-packages .virtualenv
source .virtualenv/bin/activate

pip install -r develop/requirements.txt
pip install -r develop/urlgrabber.txt
