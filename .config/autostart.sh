#!/bin/bash

function run {
    if ! pgrep $1 ;
    then
        $@&
    fi
}

run dunst
run picom --config ~/.config/picom.conf
run nm-applet
run volumeicon
run nitrogen --restore
run pulseaudio --start
