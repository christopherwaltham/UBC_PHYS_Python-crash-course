'''
Program that makes a method to display RBG color codes on an RGB LED.
'''

# import libraries
from Arduino import Arduino
import time

board = Arduino()  # find and connect microcontroller
print('Connected')                        # confirms the microcontroller has been found

# Pin numbers
RED   = 3
GREEN = 5
BLUE  = 6

# configure pins
board.pinMode(RED, "OUTPUT")
board.pinMode(GREEN, "OUTPUT")
board.pinMode(BLUE, "OUTPUT")

# define method to
def rgb(r, g, b):
    board.analogWrite(RED, r)
    board.analogWrite(GREEN, g)
    board.analogWrite(BLUE, b)

# call method to set color to RGB code
rgb(255, 0, 246)

# see https://www.google.com/search?q=color+picker
# for an easy way to generate RGB color codes

board.close()
