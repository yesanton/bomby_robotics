import Adafruit_CharLCD as LCD
lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_color(1,1,1)
lcd.clear()
import os
import datetime
import pygame
from gopigo import *
import RPi.GPIO as GPIO
from time import sleep

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("metal.wav")
pygame.mixer.music.set_volume(0.4)

sound = pygame.mixer.Sound("metal.wav")
sound.play(loops = -1)

#while True:
#	pygame.mixer.music.play(-1)
#while pygame.mixer.music.get_busy():
#    pygame.time.Clock().tick(12)
#	pygame.time.wait(250)
#	pygame.mixer.stop()
#	pygame.time.wait(1111)
































