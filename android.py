#-*-coding:utf-8-*-

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from lib.temelodevler import *

class Giris_ekran(BoxLayout):
	def backward(self, express):
		if express:
			self.display.text = express[:-1]

	def calculate(self, express):
		if not express: return

		try:
			self.display.text = str( eval(express) )
		except Exception:
			self.display.text = 'error'

class TemelOdev1_giris(BoxLayout):
    pass

class android(App):
    title = 'Topoğrafya Temel Ödev Hesapları'

    def build(self):
        return Giris_ekran()

if __name__ in ('__main__', '__android__'):
    android().run()