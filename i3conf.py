#! /usr/bin/env python3

from utils import writeConfig, updateConfig
from utils.colors import *

headText = f"""{BLUE}
#######################
## i3wm Config Tools ##
#######################{NC}"""


def rmTitle():
    rmBorder = """
###########################
## Remove i3wm Title Bar ##
###########################
for_window [class=\"^ .*\"] border pixel 0
new_window 1pixel"""

    writeConfig(rmBorder)


def chgConf():
    param = input("Parameter : ")
    val = int(input("Value : "))
    updateConfig(param, val)


options = {
    1: rmTitle,
    2: chgConf
}

print(headText)
choice = input("Choice : ")

try:
    options[int(choice)]()
except:
    print(f"{RED}Input error")
