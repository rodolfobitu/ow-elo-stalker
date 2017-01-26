#!/usr/bin/env bash

cd /rep/ow-web

pip3 install -r req.txt
python3 web.py >>/tmp/web-ow.log
