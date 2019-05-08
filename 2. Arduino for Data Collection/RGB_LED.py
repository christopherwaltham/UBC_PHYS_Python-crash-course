'''
Program to demonstrate how to flash the three colors of a RGB diode
sequentially using the Arduino-Python serial library.
'''

# import libraries
from Arduino import Arduino
import time

board = Arduino()  # find and connect microcontroller
print('Connected') # confirms the microcontroller has been found

# give pins names, so they are easy to reference
RED   = 3
GREEN = 5
BLUE  = 6

# configure the pins as outputs
board.pinMode(RED, "OUTPUT")
board.pinMode(GREEN, "OUTPUT")
board.pinMode(BLUE, "OUTPUT")

# turn all LEDs off
board.analogWrite(RED, 0)
board.analogWrite(GREEN, 0)
board.analogWrite(BLUE, 0)

try:
    while True:
        board.analogWrite(RED, 255)     # set RED to full brightness
        time.sleep(1)                   # wait 1 second

        board.analogWrite(RED, 0)       # turn RED off
        board.analogWrite(GREEN, 255)   # set GREEN to full brightness
        time.sleep(1)                   # wait 1 second

        board.analogWrite(GREEN, 0)     # turn RED off
        board.analogWrite(BLUE, 255)    # set GREEN to full brightness
        time.sleep(1)                   # wait 1 second

        board.analogWrite(BLUE, 0)      # turn GREEN off

# press ctrl+c while the console is active to terminate the program
except:
    board.close() # close the serial connection
