#!/bin/env python3

from os import getenv, getcwd, listdir
from os.path import abspath
from subprocess import run

HOME = getenv("HOME")
CWD = getcwd()
USER = listdir("/home/")[0]

if getenv("USER") == "root":
    run(["sudo", "-u", USER, "python", __file__])
    exit(0)

run(["rm", "-f", f"{HOME}/.dummy"])
run(["ln", "-s", f"{CWD}/.dummy", f"{HOME}/.dummy"])

for f in listdir("./.config"):
    run(["ln", "-s", abspath(f"./.config/{f}"), f"{HOME}/.config/{f}"])

print("INTALLED SUCCESSFULLY!")
