'''
Program that reads an analog voltage from a potentiometer and dims an LED accordingly.  
'''

# import libraries
from Arduino import Arduino

board = Arduino()  # find and connect microcontroller
print('Connected')                        # confirms the microcontroller has been found

# Pin numbers
LED = 3 # pin on LED
POT = 6 # centre tap of potentiometer

# configure pins
board.pinMode(LED, "OUTPUT")
board.pinMode(POT, "INPUT")

# Dynamic update of limits
#maxVal = board.analogRead(POT)
#minVal = board.analogRead(POT)

# Static set limits
maxVal = 2**10  # max of analog read
minVal = 20     # min of typical potentiometer reading

# use low pass fiter to remove flickering at low read values
val = 0
decayFactor = 0.98

try:
    while True:
    
        # update read valuable        
        val = decayFactor * val + (1-decayFactor) * board.analogRead(POT)
        
        # Dynamic update of limits
        #maxVal = max(maxVal, val)
        #minVal = min(minVal, val)
        
        ledStrength = (val-minVal)/(maxVal-minVal+1)*2**8
        board.analogWrite(LED, ledStrength)

        # Print values to screen, good for debugging
        #print(str(val) + ', ' + str(ledStrength) + ',   ' + str(maxVal) + ' + ' + str(minVal))

except:
    board.close()
