#! /usr/bin/env python3

from utils.function import *
from utils.colors import *
from utils.linevar import *

headText = f"""{BLUE}
#######################
## i3wm Config Tools ##
# {NC}"""

choiceText = f"""{YELLOW}
1. Remove i3wm Title Bar
2. Gaps Config{NC}"""


def rmTitle():
    rmBorder = """
###########################
## Remove i3wm Title Bar ##
###########################
for_window [class=\"^ .*\"] border pixel 0
new_window 1pixel"""

    writeConfig(rmBorder)


def chgConf():
    ginner = int(input("Gaps inner : "))
    gouter = int(input("Gaps outer : "))

    setConfig(GAPS_INNER_LINE, GAPS_INNER_STRING, ginner)
    setConfig(GAPS_OUTER_LINE, GAPS_OUTER_STRING, gouter)
    os.system("i3-msg restart >> /dev/null")


def getVar():
    target = getVariable(SMART_GAPS_LINE)
    for [param, value] in target.items():
        if not value == "ON":
            print("smart gaps off")


def setVar():
    ginner = int(input("Gaps inner : "))
    gouter = int(input("Gaps outer : "))
    smartGaps = input("Smart gaps (y/n) : ")

    setVariable(GAPS_INNER_LINE, ginner)
    setVariable(GAPS_OUTER_LINE, gouter)

    if smartGaps == "y":
        setVariable(SMART_GAPS_LINE, "ON")
    elif smartGaps == "n":
        setVariable(SMART_GAPS_LINE, "OFF")
        # target = getVariable(SMART_GAPS_LINE)
        # for [param, value] in target.items():
        #     if not value == "ON":
        #         print("smart gaps off")
    else:
        raise


options = {
    1: rmTitle,
    2: chgConf,
    3: getVar,
    4: setVar
}

print(headText)
print(choiceText)
choice = input("Choice : ")

backupConfig()

try:
    options[int(choice)]()
except:
    print(f"{RED}Input error")
