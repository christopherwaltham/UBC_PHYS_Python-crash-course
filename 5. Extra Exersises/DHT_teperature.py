#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:46:20 2019

Script to interface with temperature and humidity sensor

@author: mkals
"""

from Arduino import Arduino
import time

PIN = 7                                  # pin where temperature sensor is connected

# connect to Arduino
board = Arduino()
print('Connected')

try:
    while True:
        # make distance measurement

        data = board.dht(PIN)

        [humidity, temperature, heatIndex] = data

        reply =  "Humidity = " + str(humidity) + " % \t"
        reply += "Temperature = " + str(temperature) + " ˙C \t"
        reply += "Heat Index = " + str(heatIndex) + " ˙C"

        print(reply)

        time.sleep(1) # delay to keep UART bus for getting overloaded

except:
    board.close() # close serial connection
