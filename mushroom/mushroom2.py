#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 15:10:40 2022

@author: zeynep
"""
import pandas as pd

data = pd.read_csv("/home/zeynep/Desktop/secondary_data.csv")

#class
classes = {
        'p': 1,
        'e': 2
        }

#1 cap-diameter
#2
capShape = {
        'b': 1,
        'c': 2,
        'x': 3,
        'f': 4,
        'p': 5,
        's': 6,
        'o': 7
        }
#3
capSurface = {
        'i': 1,
        'g': 2,
        'y': 3,
        's': 4,
        'h': 5,
        'l': 6,
        'k': 7,
        't': 8
        }
#4
capColor = {
        'n': 1,
        'b': 2,
        'g': 3,
        'r': 4,
        'p': 5,
        'u': 6,
        'e': 7,
        'w': 8,
        'y': 9,
        'l': 10,
        'o': 11,
        'k': 12
        }
#5
doesBruiseBleed = {
        't': 1,
        'f': 2,
        }
#6
gillAttachment = {
        'a': 1,
        'x': 2,
        'd': 3,
        'e': 4,
        's': 6,
        'p': 7,
        'f': 8,
        '?': 9,
        }
#7
gillSpacing = {
        'c': 1,
        'd': 2,
        'f': 3
        }
#8
gillColor = {
        'n': 1,
        'b': 2,
        'g': 3,
        'r': 4,
        'p': 5,
        'u': 6,
        'e': 7,
        'w': 8,
        'y': 9,
        'l': 10,
        'o': 11,
        'k': 12,
        'f': 13
        }

#9 stem-height
#10 stem-width

#11
stemRoot = {
        'b': 1,
        's': 2,
        'c': 3,
        'u': 4,
        'e': 5,
        'z': 6,
        'r': 7
        }

#12
stemSurface = {
        'i': 1,
        'g': 2,
        'y': 3,
        's': 4,
        'h': 5,
        'l': 6,
        'k': 7,
        't': 8,
        'f': 9
        }
#13
stemColor = {
        'n': 1,
        'b': 2,
        'g': 3,
        'r': 4,
        'p': 5,
        'u': 6,
        'e': 7,
        'w': 8,
        'y': 9,
        'l': 10,
        'o': 11,
        'k': 12,
        'f': 13
        }

#14
veilType = {
        'p': 1,
        'u': 2
        }

#15
veilColor = {
        'n': 1,
        'b': 2,
        'g': 3,
        'r': 4,
        'p': 5,
        'u': 6,
        'e': 7,
        'w': 8,
        'y': 9,
        'l': 10,
        'o': 11,
        'k': 12,
        'f': 13
        }

#16
hasRing = {
        't': 1,
        'f': 2
        }

#17
ringType = {
        'c': 1,
        'e': 2,
        'r': 3,
        'g': 4,
        'l': 5,
        'p': 6,
        's': 7,
        'z': 8,
        'y': 9,
        'm': 10,
        'f': 11,
        '?': 12,
        }

#18
sporePrintColor = {
        'n': 1,
        'b': 2,
        'g': 3,
        'r': 4,
        'p': 5,
        'u': 6,
        'e': 7,
        'w': 8,
        'y': 9,
        'l': 10,
        'o': 11,
        'k': 12
        }
#19
habitat = {
        'g': 1,
        'l': 2,
        'm': 3,
        'p': 4,
        'h': 5,
        'u': 6,
        'w': 7,
        'd': 8
        }

#20
season = {
        's': 1,
        'u': 2,
        'a': 3,
        'w': 4
        }

data["class"] = data['class'].map(classes)
data["cap-shape"] = data['cap-shape'].map(capShape)
data["cap-surface"] = data['cap-surface'].map(capSurface)
data["cap-color"] = data['cap-color'].map(capColor)
data["does-bruise-or-bleed"] = data['does-bruise-or-bleed'].map(doesBruiseBleed)
data["gill-attachment"] = data['gill-attachment'].map(gillAttachment)
data["gill-color"] = data['gill-color'].map(gillColor)
data["stem-root"] = data['stem-root'].map(stemRoot)
data["stem-surface"] = data['stem-surface'].map(stemSurface)
data["stem-color"] = data['stem-color'].map(stemColor)
data["veil-type"] = data['veil-type'].map(veilType)
data["veil-color"] = data['veil-color'].map(veilColor)
data["has-ring"] = data['has-ring'].map(hasRing)
data["ring-type"] = data['ring-type'].map(ringType)
data["habitat"] = data['habitat'].map(habitat)
data["season"] = data['season'].map(season)

data.to_csv('/home/zeynep/Desktop/bitirme/mushroom/mush2.csv')
print(data)
