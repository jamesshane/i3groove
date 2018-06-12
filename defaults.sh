#!/bin/env sh
### Script written by James Shane ( github.com/jamesshane )

cd src
cp -r ../scripts/* /home/$USER/.config/polybar/
python i3wm-themer.py --config config.yaml --install defaults/
