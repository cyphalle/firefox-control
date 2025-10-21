#!/bin/bash
cd "$(dirname "$0")"
./firefox_control_env/bin/python3 control_firefox.py "$@"
