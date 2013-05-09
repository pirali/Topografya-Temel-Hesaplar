#-*-coding:utf-8-*-

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

#########################################################


"""
Topoğrafyada kullanılan temel ödev hesapları
"""
#  NOT : Programın hesap makinesinde yapılacak işlem ile kıyaslaması yapılacak.

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
    yB = yA + ( mesafe * math.sin(grad2radyan(semt)))
    xB = xA + ( mesafe * math.cos(grad2radyan(semt)))
    return yB, xB


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

    return semt, mesafe


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
    return B_semt


def temelodev4(yA, xA, yB, xB, yP, xP):
    BP = temelodev2(yP, xP, yB, xB)
    BA = temelodev2(yA, xA, yB, xB)
    B_acisi = (BP.__getitem__(0) - BA.__getitem__(0))
    return B_acisi

########################################################

#Kivy ile android uygulaması bölümü

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

Builder.load_string("""
<Giris_ekran>:
	BoxLayout:
	    orientation: "vertical"
        cols: 1
        Button:
            text: "Temel Ödev 1 - A Nok, semt ve mesafe-> B Nok."
            on_press: root.manager.current = "temelodev1giris"
        Button:
            text: "Temel Ödev 2 - A ve B Nok-> semt ve mesafe"
            on_press: root.manager.current = "temelodev2giris"
        Button:
            text: "Temel Ödev 3 - AB Semt ve B açısı-> B semt"
            on_press: root.manager.current = "temelodev3giris"
        Button:
            text: "Temel Ödev 4 - A, B ve C Nok-> B kırılma açısı"
            on_press: root.manager.current = "temelodev4giris"
        Button:
            text: "Çıkış"
            on_press: exit()

<TemelOdev1_giris>:
    BoxLayout:
        orientation: "vertical"
        GridLayout:
            cols: 2
            Label:
                text: "y değeri : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm1_y
        GridLayout:
            cols: 2
            Label:
                text: "x değeri : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm1_x
        GridLayout:
            cols: 2
            Label:
                text: "Semt Açısı : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm1_semt
        GridLayout:
            cols: 2
            Label:
                text: "Mesafe : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm1_mesafe
        Button:
            text: "Hesapla"
        Button:
            text: "Temizle"
        Button:
            text: "Geri"
            on_press: root.manager.current = "giris"

<TemelOdev1_sonuc>:
    GridLayout:
        cols: 1
        Label:
            text: "B noktası koordinatları : "
        TextInput:
            text: ""
            readonly: True
            multiline: False
        Button:
            text: "Geri"
            on_press: root.manager.current = "temelodev1giris"

<TemelOdev2_giris>:
    BoxLayout:
        orientation: "vertical"
        GridLayout:
            cols: 2
            Label:
                text: "A nok - y değeri : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm2_yA
        GridLayout:
            cols: 2
            Label:
                text: "A nok - x değeri : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm2_xA
        GridLayout:
            cols: 2
            Label:
                text: "B nok - y değeri : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm2_yB
        GridLayout:
            cols: 2
            Label:
                text: "B nok - x değeri : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm2_yB
        Button:
            text: "Hesapla"
        Button:
            text: "Temizle"
        Button:
            text: "Geri"
            on_press: root.manager.current = "giris"

<TemelOdev2_sonuc>:
    GridLayout:
        cols: 1
        Label:
            text: "Semt : "
        TextInput:
            text: ""
            readonly: True
            multiline: False
        Label:
            text: "Mesafe : "
        TextInput:
            text: ""
            readonly: True
            multiline: False
        Button:
            text: "Geri"
            on_press: root.manager.current = "temelodev2giris"

<TemelOdev3_giris>:
    BoxLayout:
        orientation: "vertical"
        GridLayout:
            cols: 2
            Label:
                text: "AB arası semt : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm3_AB_semt
        GridLayout:
            cols: 2
            Label:
                text: "BC arası kırılma açısı : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm3_BC_aci
        Button:
            text: "Hesapla"
        Button:
            text: "Temizle"
        Button:
            text: "Geri"
            on_press: root.manager.current = "giris"

<TemelOdev3_sonuc>:
    GridLayout:
        cols: 1
        Label:
            text: "B Semt : "
        TextInput:
            text: ""
            readonly: True
            multiline: False
        Button:
            text: "Geri"
            on_press: root.manager.current = "temelodev3giris"

<TemelOdev4_giris>:
    BoxLayout:
        orientation: "vertical"
        GridLayout:
            cols: 2
            Label:
                text: "A nok - y değeri : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm4_yA
        GridLayout:
            cols: 2
            Label:
                text: "A nok - x değeri : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm4_xA
        GridLayout:
            cols: 2
            Label:
                text: "B nok - y değeri : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm4_yB
        GridLayout:
            cols: 2
            Label:
                text: "B nok - x değeri : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm4_yB
        GridLayout:
            cols: 2
            Label:
                text: "C nok - y değeri : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm4_yB
        GridLayout:
            cols: 2
            Label:
                text: "C nok - x değeri : "
                size_hint_x: None
                width: 200
            TextInput:
                text: ""
                multiline: False
                id: tm4_yB
        Button:
            text: "Hesapla"
        Button:
            text: "Temizle"
        Button:
            text: "Geri"
            on_press: root.manager.current = "giris"

<TemelOdev4_sonuc>:
    GridLayout:
        cols: 1
        Label:
            text: "ABC - B kırılma açısı : "
        TextInput:
            text: ""
            readonly: True
            multiline: False
        Button:
            text: "Geri"
            on_press: root.manager.current = "temelodev4giris"
""")

class Giris_ekran(Screen):
    pass

class TemelOdev1_giris(Screen):
    pass

class TemelOdev2_giris(Screen):
    pass

class TemelOdev3_giris(Screen):
    pass

class TemelOdev4_giris(Screen):
    pass

class TemelOdev1_sonuc(Screen):
    pass

class TemelOdev2_sonuc(Screen):
    pass

class TemelOdev3_sonuc(Screen):
    pass

class TemelOdev4_sonuc(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Giris_ekran(name="giris"))

sm.add_widget(TemelOdev1_giris(name="temelodev1giris"))
sm.add_widget(TemelOdev2_giris(name="temelodev2giris"))
sm.add_widget(TemelOdev3_giris(name="temelodev3giris"))
sm.add_widget(TemelOdev4_giris(name="temelodev4giris"))

sm.add_widget(TemelOdev1_sonuc(name="temelodev1sonuc"))
sm.add_widget(TemelOdev2_sonuc(name="temelodev2sonuc"))
sm.add_widget(TemelOdev3_sonuc(name="temelodev3sonuc"))
sm.add_widget(TemelOdev4_sonuc(name="temelodev4sonuc"))

class android(App):
    title = 'Topoğrafya Temel Ödev Hesapları'
    def build(self):
        return sm

if __name__ in ('__main__', '__android__'):
    android().run()