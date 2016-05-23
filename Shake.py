import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.IN)

while(1):
	if(GPIO.input(40)):
		print("HIGH")
	else:
		print("LOW")

