#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Hesaplamalarda kullanılacak temel matematik fonksiyonları
"""

import math

#  pi sayısı tanımlaması
pi = math.pi

#  Radyan -> Grad dönüşümü
def radyan2grad(radyan):
    grad = 200 * radyan / pi
    return grad

# Grad -> Radyan dönüşümü
def grad2radyan(grad):
    radyan = pi * grad / 200
    return radyan

#  Derece -> Radyan dönüşümü
def derece2radyan(derece):
    radyan = math.degrees(derece)
    return radyan

#  Radyan -> Derece dönüşümü
def radyan2derece(radyan):
    derece = math.radians(radyan)
    return derece

#  Derece -> Grad dönüşümü
def derece2grad(derece):
    radyan = derece2radyan(derece)
    grad = radyan2grad(radyan)
    return grad

#  Grad -> Derece dönüşümü
def grad2derece(grad):
    radyan = grad2radyan(grad)
    derece = radyan2derece(radyan)
    return derece

