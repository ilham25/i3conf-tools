#! /usr/bin/python

from utils import writeConfig


rmBorder = ["###########################",
            "## Remove i3wm Title Bar ##",
            "###########################",
            "for_window [class=\"^ .*\"] border pixel 0",
            "new_window 1pixel",
            ]


writeConfig(insGaps)
