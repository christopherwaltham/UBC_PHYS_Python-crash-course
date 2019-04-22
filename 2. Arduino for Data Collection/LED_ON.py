#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:00:15 2019

Script to turn LED on

@author: mkals
"""

from Arduino import Arduino

board = Arduino()               # find and connect microcontroller
print('Connected')              # confirms the microcontroller has been found

board.pinMode(3, 'OUTPUT')      # configure pin D3 to be an output pin
board.digitalWrite(3, 'HIGH')   # make LED light up

board.close()                   # close the connection to the board