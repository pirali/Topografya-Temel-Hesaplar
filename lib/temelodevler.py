#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Topoğrafyada kullanılan temel ödev hesapları
"""
#  NOT : Programın hesap makinesinde yapılacak işlem ile kıyaslaması yapılacak.

from mat_fonk import *
import math


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

def temelodev1(yA, xA, semt, mesafe):
    yB = yA + ( mesafe * math.sin( grad2radyan(semt) ))
    xB = xA + ( mesafe * math.cos( grad2radyan(semt) ))
    return yB, xB

def temelodev2(yA, xA, yB, xB):
    delta_y = yB - yA
    delta_x = xB - xA
    
    try:
        semt = radyan2grad(math.atan(delta_y / delta_x)) + bolgesecimi(delta_y, delta_x)
    except:
        semt = 0
        
    try:
        mesafe =  delta_y / math.sin( grad2radyan( semt ) )
    except:
        mesafe =  delta_x / math.cos( grad2radyan( semt ) )
        
    return semt, mesafe

def temelodev3():
    pass

def temelodev4():
    pass

if __name__ == "__main__":
    pass