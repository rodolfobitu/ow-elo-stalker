#!/usr/bin/env bash

rm -r deploy
mkdir deploy
cp config.yaml deploy
cp insert_rank.sql deploy
cp ow.py deploy
cp req.txt deploy
cp run.sh deploy
cp users.sql deploy


