#!/bin/sh
xrandr --output HDMI-0 --right-of eDP-1-1 --output eDP-1-1 --primary &
conky -c  /home/mjalmonte/.config/conky/default.conkyrc &
picom --experimental-backends &
nitrogen --restore &
optimus-manager-qt &
flatpak run org.ferdium.Ferdium &
jellyfinmediaplayer &
modprobe btusb &
dropbox &

