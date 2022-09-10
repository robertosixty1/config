#!/bin/env python3

from os import getenv, getcwd, listdir
from subprocess import run

HOME = getenv("HOME")
CWD = getcwd()
USER = listdir("/home/")[0]

if getenv("USER") == "root":
    run(["sudo", "-u", USER, "python", __file__])
    exit(0)

run(["rm", "-f", f"{HOME}/.tmux.conf"])

run(["ln", "-s", f"{CWD}/.tmux.conf", f"{HOME}/.tmux.conf"])

print("INTALLED SUCCESSFULLY!")