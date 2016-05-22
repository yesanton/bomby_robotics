from threading import Thread
from Display import Display
from time import sleep
from Sound import Sound

class Status(object):
    def __init__(self):
        #0- not started
        #1- started
        #2- Exploded
        #3- Closing
        self.status=0
        #True : change the word
        #False: keep the word
        self.changeword=False
        
        #Count how many words been shown
        self.wordscounter=0

    def reset(self):
        self.status=0
        self.changeword=False
        self.wordscounter=0
        self.currentword=''
    def wordupdated(self):
        self.changeword=False
        self.wordscounter+=1
        
    def getstatus(self):
        return self.status
    
status = Status()
print status.getstatus()
disp = Display(status)
sound = Sound(status)

def Displayfunction():
    while status.status!=3:
        disp.display()
        sleep(0.5)
    print 'Display Thread Ended \n'
displaythread = Thread(target=Displayfunction)
soundthread= Thread(target=sound.SoundOperator)

def initialize():
    displaythread.start()
    soundthread.start()
    print '1'
    sleep(2)#shaking
    status.status=1
    status.changeword=True
    print '2'
    sleep(2)
    status.status=2
    sleep(2)
    status.status=3
    disp.clear()
    
try:
    initialize()
except:
    status.status=3
