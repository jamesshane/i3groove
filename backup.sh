#!/bin/env sh
### Script written by James Shane ( github.com/jamesshane )

cd src
mkdir $HOME/Backup
./i3wm-themer.py --config config.yaml --backup $HOME/Backup
