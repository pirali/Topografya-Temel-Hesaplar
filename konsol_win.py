#!/usr/bin/env python
# -*- coding: cp1254 -*-

"""
Topo�rafya Temel Hesaplar program�n�n
konsoldan menu uygulamas�.
"""

import locale

import lib.temelodevler

import lib.mat_fonk

import lib.konsol_fonk

#T�rk�e karakterler d�zeltmesis
locale.setlocale(locale.LC_ALL, "")

menu_calistir = True

print "Topo�rafya Temel Hesaplar Program�\n"
print "Yazan   : �zkan �EN"
print "E-Posta : ozkansen@gmail.com"
print "G�r�� ve �nerilerinizi elektronik posta yoluyla iletebilirsiniz.\n"

while menu_calistir:
    print "1. A noktas� koordinatlar�, semt ve mesafe. \n\t\tHesaplanan : B noktas� koordinat�."
    print "2. A noktas� ve B noktas� koordinatlar�. \n\t\tHesaplanan : AB aras� semt ve mesafe."
    print "3. AB aras� semt ve BC aras� k�r�lma a��s�. \n\t\tHesaplanan : BC semt."
    print "4. A, B, C noktas� koordinatlar�. \n\t\tHesaplanan BA - BC aras� k�r�lma a��s�."
    print "5. Programdan ��k��."
    try:
        sec = input("Se�mek istedi�iniz i�lem : ")
    except:
        print "Men�de olmayan bir�eyi se�tiniz."
        continue
    if sec == 1:
        try:
            print "1. A noktas� koordinatlar�, semt ve mesafe. \nHesaplanan : B noktas� koordinat�."
            yA = input("A noktas� y de�eri : ")
            xA = input("A noktas� x de�eri : ")
            semt = input("Semt a��s�n� giriniz : ")
            mesafe = input("Mesafe giriniz : ")
            sonuc = lib.temelodevler.temelodev1(yA, xA, semt, mesafe)
            print "B noktas� y de�eri : ", sonuc.__getitem__(0), "\nB noktas� x de�eri : ", sonuc.__getitem__(1)
            input("Devam etmek i�in enter tu�una bas�n�z.")
        except:
            continue
    elif sec == 2:
        try:
            print "2. A noktas� ve B noktas� koordinatlar�. \nHesaplanan : AB aras� semt ve mesafe."
            yA = input("A noktas� y de�eri : ")
            xA = input("A noktas� x de�eri : ")
            yB = input("B noktas� y de�eri : ")
            xB = input("B noktas� x de�eri : ")
            sonuc = lib.temelodevler.temelodev2(yA, xA, yB, xB)
            print "Semt de�eri : ", sonuc.__getitem__(0), "\nMesafe : ", sonuc.__getitem__(1)
            input("Devam etmek i�in enter tu�una bas�n�z.")
        except:
            continue
    elif sec == 3:
        try:
            print "3. AB aras� semt ve BC aras� k�r�lma a��s�. \nHesaplanan : BC semt."
            AB_semt = input("AB semt : ")
            BC_kirilma = input("BC k�r�lma : ")
            sonuc = lib.temelodevler.temelodev3(AB_semt, BC_kirilma)
            print "BC semt de�eri : ", sonuc
            input("Devam etmek i�in enter tu�una bas�n�z.")
        except:
            continue
    elif sec == 4:
        try:
            print "4. A, B, C noktas� koordinatlar�. \nHesaplanan BA - BC aras� k�r�lma a��s�."
            yA = input("A noktas� y de�eri : ")
            xA = input("A noktas� x de�eri : ")
            yB = input("B noktas� y de�eri : ")
            xB = input("B noktas� x de�eri : ")
            yC = input("C noktas� y de�eri : ")
            xC = input("C noktas� x de�eri : ")
            sonuc = lib.temelodevler.temelodev4(yA, xA, yB, xB, yC, xC)
            print "BA ve BC aras� k�r�lma a��s� : ", sonuc
            input("Devam etmek i�in enter tu�una bas�n�z.")
        except:
            continue
    elif sec == 5:
        menu_calistir = False
    else:
        continue
        # None