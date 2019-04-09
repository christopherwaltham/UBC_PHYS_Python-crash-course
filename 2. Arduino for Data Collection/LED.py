#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 21:30:16 2019

@author: mkals
"""

# import libraries
from Arduino import Arduino
import time

#portName = 'COM3'                      # example of Windows port name
portName = '/dev/tty.usbserial-1410'    # exmaple of Mac port name
pin = 5

board = Arduino('9600', port=portName) # find and connect microcontroller
print('Connected')                     # confirms the microcontroller has been found

time.sleep(2)

board.pinMode(pin, 'OUTPUT')           # configure pin D5 to be an output pin

#board.digitalWrite(5, 'LOW')          # uncomment this line to turn LED off

try: # error handeling block

    # enter infinite loop
    while True:
        board.digitalWrite(pin, 'LOW')   # set pin LOW (0V)
        time.sleep(1)                    # wait 1 second
        board.digitalWrite(pin, 'HIGH')  # set pin HIGH (5V)
        time.sleep(1)                    # wait 1 second

except KeyboardInterrupt:   # interrupt handeler
    board.close()           # close serial connection
