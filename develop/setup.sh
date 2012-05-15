#!/usr/bin/env bash

dfa_root=$1

cd dfa_root
virutalenv --no-site-packages .virtualenv
source .virtualenv/bin/activate

pip install -r develop/requirements.txt
pip install -r develop/urlgrabber.txt
