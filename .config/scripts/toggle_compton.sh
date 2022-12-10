#!/bin/env sh

if ! pgrep compton ; then
    compton --config ~/.config/compton.conf &
else
    killall -9 compton
fi
