#!/usr/bin/env python
#-*-coding:utf-8-*-

import os
import re


def addToClipBoard(text):
    #  Panoya kopyala
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


#Daha sonra geniş bir fonksiyon hazırlanacak
#sayi ve nokta haricindeki herşey kaldırılacak
# def sayi_kontrol(sayi):
#     sayi = eval(sayi.replace(",", "."))
#     return sayi

def kontrol(girdi):
    girdi = str(girdi)
    ara = re.search("[a-zA-Z,]", girdi)
    if ara:
        derle = re.compile("[a-zA-Z]")
        cikti = derle.sub("",girdi)
        ara2 = re.search(",", cikti)
        if ara2:
            derle2 = re.compile(",")
            cikti2 = derle2.sub(".",cikti)
            return float(cikti2)
        return float(cikti)
    return float(girdi)

def yuvarla(sayi):
    pass
