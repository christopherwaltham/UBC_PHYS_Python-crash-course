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
portName = '/dev/tty.usbserial-1430'  # exmaple of Mac port name

board = Arduino('9600', port=portName) # find and connect microcontroller
print('Connected')                     # confirms the microcontroller has been found

board.pinMode(5, 'OUTPUT')             # configure pin D5 to be an output pin

board.digitalWrite(5, 'HIGH')          # make LED light up
#board.digitalWrite(5, 'LOW')          # uncomment this line to turn LED off

# enter infinite loop
while True:
    board.digitalWrite(5, 'LOW')   # set pin LOW (0V)
    time.sleep(1)                  # wait 1 second
    board.digitalWrite(5, 'HIGH')  # set pin HIGH (5V)
    time.sleep(1)                  # wait 1 second