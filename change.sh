#!/bin/env sh
### Script written by James Shane ( github.com/jamesshane )

cd src
./i3wm-themer.py --config config.yaml --load themes/$1.json
