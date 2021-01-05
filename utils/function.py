
import os.path
import getpass

# Get current username and set path to user home directory
username = getpass.getuser()
homeDir = f'/home/{username}/'

# Set home directory and locate i3wm config file
configPath = os.path.join(homeDir, ".config/i3/config")
configPath_debug = "config"


def writeConfig(scripts):
    """
    This function used to automatically generate i3wm config file in ~/.config/i3/config. You must pass script to generate as this function arguments as list file type
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
    with open(configPath_debug, "rt") as fin:

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

    with open(configPath_debug, "wt") as fout:
        fout.write(new_config)
