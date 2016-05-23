import RPi.GPIO as GPIO


#GPIO.setmode(GPIO.BOARD)

GPIO.setup(21, GPIO.IN)
def WaitShake():
        print 'Shake visited'
        while(1):
                if(GPIO.input(21)):
                        print("HIGH")
                else:
                        print("LOW")
                        return True
