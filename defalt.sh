#file didn't exist for me, so test and touch
if [ -e $HOME/.Xresources ]
then
	echo "... .Xresources found."
else
	touch $HOME/.Xresources
fi

#file didn't exist for me, so test and touch
if [ -e $HOME/.config/nitrogen/bg-saved.cfg ]
then
        echo "... .bg-saved.cfg found."
else
				mkdir $HOME/.config/nitrogen
        touch $HOME/.config/nitrogen/bg-saved.cfg
fi

#rework of user in config.yaml
cd src
rm -f config.yaml
cp defaults/config.yaml .
sed -i -e "s/USER/$USER/g" config.yaml

#file didn't excist for me, so test and touch
if [ -e $HOME/.config/polybar/config ]
then
        echo "... polybar/config found."
else
				mkdir $HOME/.config/polybar
        touch $HOME/.config/polybar/config
fi

#backup, configure and set theme to default
cp -r ../scripts/* /home/$USER/.config/polybar/
mkdir $HOME/Backup
python i3wm-themer.py --config config.yaml --backup $HOME/Backup
python i3wm-themer.py --config config.yaml --install defaults/

echo ""
echo "Read the README.md"
