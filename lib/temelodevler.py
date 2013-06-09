#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Topoğrafyada kullanılan temel ödev hesapları
"""
#  NOT : Programın hesap makinesinde yapılacak işlem ile kıyaslaması yapılacak.

# Python modülleri
import math

# Programın modülleri
import ayarlar
from mat_fonk import *


#  Temel ödev hesaplamalarındaki sonucun hangi bölge olduğunu tespit etmek için.
def bolgesecimi(y, x):
    if (y >= 0) and (x >= 0): # 1. Bölge y+ x+
        return 0
    if (y >= 0) and (x < 0): # 2. Bölge y+ x+
        return 200
    if (y < 0) and (x < 0): # 3. Bölge y- x-
        return 200
    if (y < 0) and (x >= 0): # 4. Bölge y- x+
        return 400


def temelodev1(yA, xA, semt, mesafe):
    yB = yA + ( mesafe * math.sin(grad2radyan(semt)))
    xB = xA + ( mesafe * math.cos(grad2radyan(semt)))
    return round(yB, ayarlar._KOORDINAT), round(xB, ayarlar._KOORDINAT)


def temelodev2(yA, xA, yB, xB):
    delta_y = yB - yA
    delta_x = xB - xA

    try:
        semt = radyan2grad(math.atan(delta_y / delta_x)) + bolgesecimi(delta_y, delta_x)
    except:
        semt = 0

    try:
        mesafe = delta_y / math.sin(grad2radyan(semt))
    except:
        mesafe = delta_x / math.cos(grad2radyan(semt))

    return round(semt, ayarlar._ACIDEGERI), round(mesafe, ayarlar._MESAFE)


def temelodev3(AB_semt, B_acisi):
    B_semt = AB_semt + B_acisi
    if ( B_semt < 200 ):
        B_semt = B_semt + 200
    elif ( B_semt >= 200 ) and ( B_semt < 600 ):
        B_semt = B_semt - 200
    elif ( B_semt >= 600 ):
        B_semt = B_semt - 600
    else:
        pass
    return round(B_semt, ayarlar._ACIDEGERI)


def temelodev4(yA, xA, yB, xB, yP, xP):
    BP = temelodev2(yP, xP, yB, xB)
    BA = temelodev2(yA, xA, yB, xB)
    B_acisi = (BP.__getitem__(0) - BA.__getitem__(0))
    return round(B_acisi, ayarlar._ACIDEGERI)

