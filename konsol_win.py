#!/usr/bin/env python
# -*- coding: cp1254 -*-

"""
Topoğrafya Temel Hesaplar programının
konsoldan menu uygulaması.
"""

import locale

import lib.temelodevler

import lib.mat_fonk

import lib.konsol_fonk

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
            yA = input("A noktası y değeri : ")
            xA = input("A noktası x değeri : ")
            semt = input("Semt açısını giriniz : ")
            mesafe = input("Mesafe giriniz : ")
            sonuc = lib.temelodevler.temelodev1(yA, xA, semt, mesafe)
            print "B noktası y değeri : ", sonuc.__getitem__(0), "\nB noktası x değeri : ", sonuc.__getitem__(1)
            input("Devam etmek için enter tuşuna basınız.")
        except:
            continue
    elif sec == 2:
        try:
            print "2. A noktası ve B noktası koordinatları. \nHesaplanan : AB arası semt ve mesafe."
            yA = input("A noktası y değeri : ")
            xA = input("A noktası x değeri : ")
            yB = input("B noktası y değeri : ")
            xB = input("B noktası x değeri : ")
            sonuc = lib.temelodevler.temelodev2(yA, xA, yB, xB)
            print "Semt değeri : ", sonuc.__getitem__(0), "\nMesafe : ", sonuc.__getitem__(1)
            input("Devam etmek için enter tuşuna basınız.")
        except:
            continue
    elif sec == 3:
        try:
            print "3. AB arası semt ve BC arası kırılma açısı. \nHesaplanan : BC semt."
            AB_semt = input("AB semt : ")
            BC_kirilma = input("BC kırılma : ")
            sonuc = lib.temelodevler.temelodev3(AB_semt, BC_kirilma)
            print "BC semt değeri : ", sonuc
            input("Devam etmek için enter tuşuna basınız.")
        except:
            continue
    elif sec == 4:
        try:
            print "4. A, B, C noktası koordinatları. \nHesaplanan BA - BC arası kırılma açısı."
            yA = input("A noktası y değeri : ")
            xA = input("A noktası x değeri : ")
            yB = input("B noktası y değeri : ")
            xB = input("B noktası x değeri : ")
            yC = input("C noktası y değeri : ")
            xC = input("C noktası x değeri : ")
            sonuc = lib.temelodevler.temelodev4(yA, xA, yB, xB, yC, xC)
            print "BA ve BC arası kırılma açısı : ", sonuc
            input("Devam etmek için enter tuşuna basınız.")
        except:
            continue
    elif sec == 5:
        menu_calistir = False
    else:
        continue
        # None