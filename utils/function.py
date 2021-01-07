
import os.path
import getpass
import subprocess
from shutil import copyfile
from .colors import *

# Get current username and set path to user home directory
username = getpass.getuser()
wmPath = f'/home/{username}/.config/i3/'
fileName = "config"

# Set home directory and locate i3wm config file
configPath = os.path.join(wmPath, fileName)
configPath_debug = fileName


def backupConfig():
    print(f"{YELLOW}Checking file backup...{NC}")
    if not os.path.isfile(configPath + ".bak"):
        print(f"{YELLOW}Backup file not found, creating {GREEN}{fileName}.bak{NC}")
        copyfile(configPath, configPath + ".bak")
    else:
        print(f"{GREEN}Found backup file, continue...{NC}")


def writeConfig(scripts):
    """
    This function used to automatically generate i3wm config file in ~/.config/i3/config. You must pass script to generate as this function arguments accept a multiline string
    """

    # Accept argument as array
    # with open(configPath, "a") as file1:
    #     for script in scripts:
    #         file1.write(script + "\n")

    # Accept argument as multiline string
    with open(configPath, "a") as file1:
        file1.write(scripts)


def updateConfig(param, newValue):

    # Read input file
    with open(configPath, "rt") as fin:

        # Separator
        separator = ' '

        # Store all lines into python dictionary
        configs = {}

        # Iterate each line in i3wm config file
        for line in fin.readlines():

            # Split each line separate by ' '
            splitted = line.split(separator)
            # Get last value from line
            try:
                value = splitted.pop(-1)
                # Get parameter without it's value
                parameter = separator.join(splitted)
                # Insert parameters and it's value into dictionary
                configs[parameter] = value
            except Exception as e:
                print(str(e))

        # Set value based on parameter
        configs[param] = newValue

        # List for store new line
        new_config = []

        # Iterate each parameter and it's value using items()
        for [parameter, value] in configs.items():
            # Combine parameter name and value to create new line
            line = separator.join([parameter, str(value)])
            new_config.append(line)

        # Combine all line into one string
        new_config = '\n'.join(new_config)

    with open(configPath, "wt") as fout:
        fout.write(new_config)


def getVariable(line):
    with open("VARIABLES") as var:
        configLine = var.readlines()
        print(configLine[line - 1])


def setVariable(line, newVal):
    with open("VARIABLES") as var:
        # Variables as dictionary
        paramSplit = {}

        # Separator
        separator = '='

        # Read line based on line arguments
        configLine = var.readlines()[line - 1]

        # Split parameter and it's value by '='
        splitted = configLine.split(separator)

        # Get only value from parameter
        value = splitted.pop(-1)

        # Get only parameter without value
        param = separator.join(splitted)

        # Insert parameter and it's value separately
        paramSplit[param] = value

        # Set new value based on parameter
        paramSplit[param] = newVal
        for [param, value] in paramSplit.items():
            # Combine parameter name and value to create new line
            nline = separator.join([param, str(value)])

        with open("VARIABLES", 'rt') as fin:
            data = fin.read()
            data = data.replace(configLine, nline + "\n")
        with open("VARIABLES", 'wt') as fout:
            fout.write(data)
