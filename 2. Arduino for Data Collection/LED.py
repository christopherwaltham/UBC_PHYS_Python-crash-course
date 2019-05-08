#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 21:30:16 2019

Progrm to turn an LED on and off.

@author: mkals
"""

# import libraries
from Arduino import Arduino
import time

pin = 5

board = Arduino()  # find and connect microcontroller
print('Connected') # confirms the microcontroller has been found

board.pinMode(pin, 'OUTPUT')   # configure pin D5 to be an output pin

# error handeling block
try:

    # enter infinite loop
    while True:
        board.digitalWrite(pin, 'LOW')   # set pin LOW (0V)
        time.sleep(1)                    # wait 1 second
        board.digitalWrite(pin, 'HIGH')  # set pin HIGH (5V)
        time.sleep(1)                    # wait 1 second

except:   # interrupt handeler
    board.close()           # close serial connection
