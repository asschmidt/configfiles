#!/usr/bin/bash

COLORSCHEME=DoomOne

#export wallpaper='/home/andreas/OpenSource/wallpapers/0199.jpg'

### AUTOSTART PROGRAMS ###
numlockw on

#"$HOME"/.screenlayout/layout.sh &
# Run the monitor configuration
killall kanshi
sleep 1
kanshi &

killall conky
sleep 1
conky -c /home/andreas/.config/conky/conky.conf --pause=1 &

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
# find /usr/share/backgrounds/dtos-backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
# nitrogen --restore &

# Swayidle daemon

killall swayidle
swayidle \
	timeout 5 'qtile cmd-obj -o core -f hide_cursor' resume 'qtile cmd-obj -o core -f unhide_cursor' \
    timeout 300 'swaylock -f -c 000000' &
	#timeout 300 'swaylock -f -i /home/andreas/OpenSource/wallpapers/0199.jpg' &
