#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 00:09:47 2022

@author: zeynep
"""

import pandas as pd

data = pd.read_csv("/home/zeynep/Desktop/none3.csv")

#class
classes = {
        'hakaretvar': 1,
        'hakaretyok': 0
        }

data["CLASS"] = data['CLASS'].map(classes)

data.to_csv('/home/zeynep/Desktop/none4.csv')

