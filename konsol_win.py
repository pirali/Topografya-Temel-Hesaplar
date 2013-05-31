#!/usr/bin/env python
# -*- coding: cp1254 -*-

"""
Topoğrafya Temel Hesaplar programının
konsoldan menu uygulaması.
"""

import locale

import lib.temelodevler
import lib.mat_fonk
from lib.konsol_fonk import *

#Türkçe karakterler düzeltmesis
locale.setlocale(locale.LC_ALL, "")

menu_calistir = True

print "Topoğrafya Temel Hesaplar Programı\n"
print "Yazan   : Özkan ŞEN"
print "E-Posta : ozkansen@gmail.com"
print "Görüş ve önerilerinizi elektronik posta yoluyla iletebilirsiniz.\n"

while menu_calistir:
    print "1. A noktası koordinatları, semt ve mesafe. \n\t\tHesaplanan : B noktası koordinatı."
    print "2. A noktası ve B noktası koordinatları. \n\t\tHesaplanan : AB arası semt ve mesafe."
    print "3. AB arası semt ve BC arası kırılma açısı. \n\t\tHesaplanan : BC semt."
    print "4. A, B, C noktası koordinatları. \n\t\tHesaplanan BA - BC arası kırılma açısı."
    print "5. Programdan çıkış."
    try:
        sec = input("Seçmek istediğiniz işlem : ")
    except:
        print "Menüde olmayan birşeyi seçtiniz."
        continue
    if sec == 1:
        try:
            print "1. A noktası koordinatları, semt ve mesafe. \nHesaplanan : B noktası koordinatı."
            yA = kontrol(raw_input("A noktası y değeri : "))
            xA = kontrol(raw_input("A noktası x değeri : "))
            semt = kontrol(raw_input("Semt açısını giriniz : "))
            mesafe = kontrol(raw_input("Mesafe giriniz : "))
            sonuc = lib.temelodevler.temelodev1(yA, xA, semt, mesafe)
            print "B noktası y değeri : ", sonuc.__getitem__(0), "\nB noktası x değeri : ", sonuc.__getitem__(1)
            raw_input("Devam etmek için enter tuşuna basınız.")
        except:
            continue
    elif sec == 2:
        try:
            print "2. A noktası ve B noktası koordinatları. \nHesaplanan : AB arası semt ve mesafe."
            yA = kontrol(raw_input("A noktası y değeri : "))
            xA = kontrol(raw_input("A noktası x değeri : "))
            yB = kontrol(raw_input("B noktası y değeri : "))
            xB = kontrol(raw_input("B noktası x değeri : "))
            sonuc = lib.temelodevler.temelodev2(yA, xA, yB, xB)
            print "Semt değeri : ", sonuc.__getitem__(0), "\nMesafe : ", sonuc.__getitem__(1)
            raw_input("Devam etmek için enter tuşuna basınız.")
        except:
            continue
    elif sec == 3:
        try:
            print "3. AB arası semt ve BC arası kırılma açısı. \nHesaplanan : BC semt."
            AB_semt = kontrol(raw_input("AB semt : "))
            BC_kirilma = kontrol(raw_input("BC kırılma : "))
            sonuc = lib.temelodevler.temelodev3(AB_semt, BC_kirilma)
            print "BC semt değeri : ", sonuc
            raw_input("Devam etmek için enter tuşuna basınız.")
        except:
            continue
    elif sec == 4:
        try:
            print "4. A, B, C noktası koordinatları. \nHesaplanan BA - BC arası kırılma açısı."
            yA = kontrol(raw_input("A noktası y değeri : "))
            xA = kontrol(raw_input("A noktası x değeri : "))
            yB = kontrol(raw_input("B noktası y değeri : "))
            xB = kontrol(raw_input("B noktası x değeri : "))
            yC = kontrol(raw_input("C noktası y değeri : "))
            xC = kontrol(raw_input("C noktası x değeri : "))
            sonuc = lib.temelodevler.temelodev4(yA, xA, yB, xB, yC, xC)
            print "BA ve BC arası kırılma açısı : ", sonuc
            raw_input("Devam etmek için enter tuşuna basınız.")
        except:
            continue
    elif sec == 5:
        menu_calistir = False
    else:
        continue
        # None