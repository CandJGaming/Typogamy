import os
from playsound import playsound
import multiprocessing

sound = os.path.abspath("GameSongs/Song0")
x = 9
while(x < 10):
	playsound('Song0.wav')
	x = x+1