
import os.path
import getpass


def writeConfig(scripts):
    """
    This function used to automatically generate i3wm config file in ~/.config/i3/config. You must pass script to generate as this function arguments as list file type
    """

    # Get current username and set path to user home directory
    username = getpass.getuser()
    homeDir = f'/home/{username}/'

    # Set home directory and locate i3wm config file
    configPath = os.path.join(homeDir, "guaranteed_tags")

    # Accept argument as array
    # with open(configPath, "a") as file1:
    #     for script in scripts:
    #         file1.write(script + "\n")

    # Accept argument as multiline string
    with open(configPath, "a") as file1:
        file1.write(scripts)
