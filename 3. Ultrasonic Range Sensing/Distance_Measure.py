"""
Program to 
"""

from Arduino import Arduino
import time

# NEW, import csv library
import csv

PORT_NAME = 'COM3'                    # MUST BE UPDATED TO USE THE CORRECT PORT
FILE_NAME = 'pendulum_data.csv'       # name of file that data will be written to
PIN_SENSE = 12                        # pin where ultrasic sensor is connected

# connect to Arduino
board = Arduino('9600', port=PORT_NAME)
print('Connected')
f = open(FILE_NAME,'a')              # open a file for 'a'ppending
writer = csv.writer(f,delimiter=',') # prepare for writing to file

# Write data-field titles to file
writer.writerow(['Time (s)', 'Distance (cm)'])

startTime = time.time() # capture current time as datum

try:
    while True:
        # make distance measurement
        pulseTime = board.pulseIn_set(PIN_SENSE, 'HIGH')
        distance = pulseTime * 0.034 / 2; # in cm

        # write list of data to file
        currentTime = time.time()-startTime
        data = [currentTime, distance]

        writer.writerow(data) # write data to file
        print('time = %5.2f   distance = %5.1f' % tuple(data))

        time.sleep(0.5) # delay to keep UART bus for getting overloaded

# press ctrl+c while the console is active to terminate the program
except KeyboardInterrupt:
    board.close() # close serial connection
    f.close()     # close file gracefully when program is terminated
