#!/usr/bin/env python3

# Read input file
with open("sample.txt", "rt") as fin:

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
        except:
            pass

    # Set value based on parameter
    configs['gaps inner'] = 1102
    

    # List for store new line
    new_config = []

    # Iterate each parameter and it's value using items()
    for [parameter, value] in configs.items():
        # Combine parameter name and value to create new line
        line = separator.join([parameter, str(value)])
        new_config.append(line)

    # Combine all line into one string
    new_config = '\n'.join(new_config)

with open("sample.txt", "wt") as fout:
    fout.write(new_config)
