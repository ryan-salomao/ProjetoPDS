#!/usr/bin/env bash
virtualenv venv
chmod 777 venv/bin/activate
source ./venv/bin/activate
pip install -r requirements.txt
