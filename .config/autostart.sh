#!/bin/bash

function run {
    if ! pgrep $1 ;
    then
        $@&
    fi
}

run dunst
run compton --config ~/.config/compton.conf
run nm-applet
run volumeicon
run nitrogen --restore
run pulseaudio --start
run sxhkd ~/.config/sxhkd/sxhkdrc
run caffeine-indicator
run fcitx-autostart
