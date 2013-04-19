#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Topoğrafyada kullanılan temel ödev hesapları
"""


#  Temel ödev hesaplamalarındaki sonucun hangi bölge olduğunu tespit etmek için.
def bolgesecimi(y, x):
    if (y >= 0) and (x >= 0):
        return 0
    if (y >= 0) and (x < 0):
        return 200
    if (y < 0) and (x < 0):
        return 200
    if (y < 0) and (x >= 0):
        return 400

def temelodev1():
    pass

def temelodev2():
    pass

def temelodev3():
    pass

def temelodev4():
    pass
