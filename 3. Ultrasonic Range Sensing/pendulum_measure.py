# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#from Arduino import Arduino
#import time
#
#board = Arduino('9600') #plugged in via USB, serial com at rate 9600
#print('Connected')
#
#board.pinMode(5, "OUTPUT")
#board.analogWrite(5, 200)
#

from Arduino import Arduino
import time
import csv


board = Arduino('9600')
print('Connected')


try:
    while True:
    pulseTime = board.pulseIn_set(12, 'HIGH')

    # open a csv file and write time and pulseTime to it
    with open("test_data.csv","a") as f:
        writer = csv.writer(f,delimiter=",")
        writer.writerow([time.time(), pulseTime])

    time.sleep(0.1)
    
except KeyboardInterrupt:
    pass



    
    