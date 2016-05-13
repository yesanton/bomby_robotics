import pyaudio  
import wave  
from time import sleep
import random

#define stream chunk   
chunk = 1024  

#define random ranges
random_min = 30
random_max = 60

class Sound:
	def PlayTickSleep(self, septime=1):
    		self.PlayTick()
    		sleep(septime)
	def PlayTick(self,filename=r"metal.wav"):
	    #open a wav format music
	    f = wave.open(filename,"rb")
	    #instantiate PyAudio
	    p = pyaudio.PyAudio()
	    #open stream
	    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
	                    channels = f.getnchannels(),
	                    rate = f.getframerate(),
	                    output = True)
	    #read data
	    data = f.readframes(chunk)
	    #paly stream
	    while data != '':
	        stream.write(data)
	        data = f.readframes(chunk)
	
	    #stop stream
	    stream.stop_stream()
	    stream.close()
	
	    #close PyAudio
	    p.terminate()
	
	def PlayTickTimeStop(self, max=30):
	    for i in range(max):
	        self.PlayTickSleep(1-i/float(max))
        def startGame(self, status):
                self.PlayTickTimeStop(random.randint(random_min,random_max))
                self.PlayTick("thunder2.wav")
		return 1
	
#s = Sound()
#s.startGame()
#s.PlayTickTimeStop(30)




