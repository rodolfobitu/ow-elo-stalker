#!/usr/bin/env bash

rm -r deploy
mkdir deploy
cp config-web.yaml deploy
cp user-rank-web.sql deploy
cp users-web.sql deploy
cp web.py deploy
cp req.txt deploy
cp templates deploy
cp run.sh deploy
