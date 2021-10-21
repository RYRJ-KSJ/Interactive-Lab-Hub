import time
import board
import busio
import os
from playsound import playsound

import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
    for i in range(12):
        if mpr121[i].value:
            if i == 5 or i == 6:
        	    playsound('great.mp3')
        	elif i == 4 or i == 7:
        		playsound('wonderful.mp3')
        	elif i == 3 or i == 8:
        		playsound('tryanotherpoint.mp3')
        	elif i == 2 or i == 9:
        		playsound('wonderful.mp3')
        	elif i == 1 or i == 10:
        		playsound('tryanotherpoint.mp3')

    time.sleep(0.25)