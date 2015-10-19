#soundproj.py

from pyo import *
import pdb
import time

source_file = "ohyeah.wav"
file_2 = "example.wav"
clip_length = 4

s = Server().boot()
s.start()

#Delay effect chain
src = SfPlayer(source_file, loop=False, mul=.1).mix(2).out()
d = Delay(src, delay=[.15,.4], feedback=.7, mul=.6).out()
s.recstart(filename="C:/Users/Dan/Desktop/Dev/python examples/example.wav")
time.sleep(clip_length)
#s.gui(locals())
s.recstop()
s.shutdown()

#Reverse clip after applying delay
t = Server().boot()
t.start()
t.recstart(filename="C:/Users/Dan/Desktop/Dev/python examples/example_2.wav")
src_2 = SfPlayer(file_2, loop=False, speed=-1, mul=.4).mix(2).out()
time.sleep(clip_length)
t.recstop()
t.shutdown()
exit()
