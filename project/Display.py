import Adafruit_CharLCD as LCD
import random
import os
import datetime
import time


#few standard phrases 
PH_START_GAME = "Shake to begin!"
PH_GAME_FINISHED = "Boom! Game over!\n Shake again! :)"


lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_color(1,1,1)
lcd.clear()
		

class Display:
	def __init__(self):	
		with open('words2.txt') as words:
			self.lst =map(lambda x:x.strip(), words.readlines())
	def getWord(self):
		return self.lst[random.randint(0,len(self.lst))]
	

	def showWord(self,word):
		lcd.clear()
		lcd.message(word)
	
	def display(self, status):	
		if (status == 0):
			self.showWord(PH_START_GAME)
		elif (status == 2):
			word = self.getWord()	 
			self.showWord(word)
		elif (status == 3):
			self.showWord(PH_GAME_FINISHED)
		status.status = 34
	def button_status(self):
		return lcd.is_pressed(LCD.SELECT)

#d = Display()
#d.showWord(PH_GAME_FINISHED)
#d.playGame()

