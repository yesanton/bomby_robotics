import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_color(1,1,1)

lcd.clear()

import random

import os
import datetime
import time

class Display:
	def __init__(self):
		with open('words2.txt') as words:
			self.lst =map(lambda x:x.strip(), words.readlines())
	def getWord(self):
		
		return self.lst[random.randint(0,len(self.lst))]
	

	def showWord(self,word):
		lcd.clear()
		lcd.message(word)
	
	def playGame(self):
		word = "Shake to start"
		pressed = 1
		while(1):
			if(lcd.is_pressed(LCD.SELECT)):
				word = self.getWord()
				pressed = 1
			if (pressed == 1):
				self.showWord(word)
				pressed = 0
 

d = Display()

d.playGame()


