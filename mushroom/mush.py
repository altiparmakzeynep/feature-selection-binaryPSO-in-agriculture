#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 16:53:34 2022

@author: zeynep
"""
import pandas as pd

data = pd.read_csv("/home/zeynep/Desktop/bitirme/mushroom/mushrooms.csv")



#class
classes = {
        'p': 1,
        'e': 2
        }
#1
capShape = {
        'b': 1,
        'c': 2,
        'x': 3,
        'f': 4,
        'k': 5,
        's': 6,
        }
#2
capSurface = {
        'f': 1,
        'g': 2,
        'y': 3,
        's': 4
        }
#3
capColor = {
        'n': 1,
        'b': 2,
        'c': 3,
        'g': 4,
        'r': 5,
        'p': 6,
        'u': 7,
        'e': 8,
        'w': 9,
        'y': 10
        }
#4
bruises = {
        't': 1,
        'f': 2,
        }

#5
odor = {
        'a': 1,
        'l': 2,
        'c': 3,
        'y': 4,
        'f': 5,
        'm': 6,
        'n': 7,
        'p': 8,
        's': 9
        }
#6
gillAttachment = {
        'a': 1,
        'd': 2,
        'f': 3,
        'h': 4
        }

#7
gillSpacing = {
        'c': 1,
        'w': 2,
        'd': 3
        }

#8
gillSize = {
        'b': 1,
        'n': 2
        }

#9
gillColor = {
        'k': 1,
        'n': 2,
        'b': 3,
        'h': 4,
        'g': 5,
        'r': 6,
        'o': 7,
        'p': 8,
        'u': 9,
        'e': 10,
        'w': 11,
        'y': 12
        }

#10
stalkShape = {
        'e': 1,
        't': 2
        }

#11
stalkRoot = {
        'b': 1,
        'c': 2,
        'u': 3,
        'e': 4,
        'z': 5,
        'r': 6,
        '?': 7
        }

#12
stalkSurfaceAboveRing = {
        'f': 1,
        'y': 2,
        'k': 3,
        's': 4
        }

#13
stalkSurfaceBelowRing = {
        'f': 1,
        'y': 2,
        'k': 3,
        's': 4
        }

#14
stalkColorAboveRing = {
        'n': 1,
        'b': 2,
        'c': 3,
        'g': 4,
        'o': 5,
        'p': 6,
        'e': 7,
        'w': 8,
        'y': 9
        }

#15
stalkColorBelowRing = {
        'n': 1,
        'b': 2,
        'c': 3,
        'g': 4,
        'o': 5,
        'p': 6,
        'e': 7,
        'w': 8,
        'y': 9
        }

#16
veilType = {
        'p': 1,
        'u': 2
        }

#17
veilColor = {
        'n': 1,
        'o': 2,
        'w': 3,
        'y': 4
        }

#18
ringNumber = {
        'n': 1,
        'o': 2,
        't': 3
        }

#19
ringType = {
        'c': 1,
        'e': 2,
        'f': 3,
        'l': 4,
        'o': 5,
        'n': 6,
        'p': 7,
        's': 8,
        'z': 9
        }


#20
sporePrintColor = {
        'k': 1,
        'n': 2,
        'b': 3,
        'h': 4,
        'r': 5,
        'o': 6,
        'u': 7,
        'w': 8,
        'y': 9
        }

#21
population = {
        'a': 1,
        'c': 2,
        'n': 3,
        's': 4,
        'v': 5,
        'y': 6
        }

#22
habitat = {
        'g': 1,
        'l': 2,
        'm': 3,
        'p': 4,
        'u': 5,
        'w': 6,
        'd': 7
        }


data["class"] = data['class'].map(classes)
data["cap-shape"] = data['cap-shape'].map(capShape)
data["cap-surface"] = data['cap-surface'].map(capSurface)
data["cap-color"] = data['cap-color'].map(capColor)
data["bruises"] = data['bruises'].map(bruises)
data["odor"] = data['odor'].map(odor)
data["gill-attachment"] = data['gill-attachment'].map(gillAttachment)
data["gill-spacing"] = data['gill-spacing'].map(gillSpacing)
data["gill-size"] = data['gill-size'].map(gillSize)
data["gill-color"] = data['gill-color'].map(gillColor)
data["stalk-shape"] = data['stalk-shape'].map(stalkShape)
data["stalk-root"] = data['stalk-root'].map(stalkRoot)
data["stalk-surface-above-ring"] = data['stalk-surface-above-ring'].map(stalkSurfaceAboveRing)
data["stalk-surface-below-ring"] = data['stalk-surface-below-ring'].map(stalkSurfaceBelowRing)
data["stalk-color-above-ring"] = data['stalk-color-above-ring'].map(stalkColorAboveRing)
data["stalk-color-below-ring"] = data['stalk-color-below-ring'].map(stalkColorBelowRing)
data["veil-type"] = data['veil-type'].map(veilType)
data["veil-color"] = data['veil-color'].map(veilColor)
data["ring-number"] = data['ring-number'].map(ringNumber)
data["ring-type"] = data['ring-type'].map(ringType)
data["spore-print-color"] = data['spore-print-color'].map(sporePrintColor)
data["population"] = data['population'].map(population)
data["habitat"] = data['habitat'].map(habitat)

data.to_csv('/home/zeynep/Desktop/bitirme/mushroom/withoutZeroMush.csv')
print(data)
