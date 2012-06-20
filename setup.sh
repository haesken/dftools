#!/usr/bin/env bash

virtualenv --no-site-packages .virtualenv
source .virtualenv/bin/activate

pip install -r develop/python-depends/requirements.txt
