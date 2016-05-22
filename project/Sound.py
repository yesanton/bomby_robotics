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
        def __init__(self,status):
            self.gstatus=status
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
	    
	def PlayTick2(self,filename=r"metal.wav"):
            if self.gstatus.status!=1:
                    return
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
            wordcount=self.gstatus.wordscounter
	    for i in range(max):
                if self.gstatus.wordscounter>wordcount:
                        return
                if self.gstatus.status==3:
                        return
	        self.PlayTickSleep(1-i/float(max))
            self.PlayTick2("thunder2.wav")
            self.gstatus.status=2
	def SoundOperator(self):
            while 1:
                if self.gstatus.status==3:
                        print 'sound thread Ended\n'
                        return                    
                if self.gstatus.status==0:
                    sleep(1)
                    continue
                if self.gstatus.status==1:
                    print('let the show begin')
                    self.PlayTickTimeStop(random.randint(random_min,random_max))

	
#s = Sound()
#s.startGame()
#s.PlayTickTimeStop(30)




