# -*- coding: utf-8 -*-
"""
Created on Sat May 18 13:01:39 2019

@author: fusion
"""

remedios = input().split()
remedios = list(map(int,remedios))
remedios.sort()
print(remedios[0])