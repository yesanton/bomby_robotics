import Adafruit_CharLCD as LCD
import random
import os
import datetime
import time
from Display import Display

#This is status of the game
#0 - initialized
#1 - game is in progress
#2 - word guessed - switch words
#4 - game finished

EXTERNAL_STATUS = 0


class GameEngine:
	display = Display()
	def playGame(self):
		pressed = 0
		EXTERNAL_STATUS = 0
		self.display.display(EXTERNAL_STATUS)
		while(1):
			if(self.display.button_status()):	
				pressed = 1
			if(pressed == 1):
				pressed = 0
				EXTERNAL_STATUS = 2
				self.display.display(EXTERNAL_STATUS)		
			if(EXTERNAL_STATUS == 4):
				self.display.display(EXTERNAL_STATUS)				



ge = GameEngine()
ge.playGame()








