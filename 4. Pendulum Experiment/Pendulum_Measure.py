"""
Script to read distances from an ultrasonic sensor using an Arduino 
microcontroller. Prints the information to a file.  
"""


from Arduino import Arduino
import time
import csv

PORT_NAME = '/dev/tty.usbserial-1410' # MUST BE UPDATED TO USE THE CORRECT PORT
FILE_NAME = 'pendulum_data.csv'       # name of file that data will be written to
PIN_SENSE = 12                        # pin where ultrasic sensor is connected 

# connect to Arduino
board = Arduino('115200', port=PORT_NAME)
print('Connected')

f = open(FILE_NAME,'a')              # open a file for 'a'ppending
writer = csv.writer(f,delimiter=',') # prepare for writing to file

# Write data-field titles to file
writer.writerow(['Counter', 'Time (s)', 'Distance (cm)']) 

counter = 0             # to count how many data-points we have collected
startTime = time.time() # capture current time as datum

try:
    while True:
        counter = counter + 1 # increment counter

        # make distance measurement
        pulseTime = board.pulseIn_set(PIN_SENSE, 'HIGH')
        distance = pulseTime * 0.034 / 2; # in cm

        # write list of data to file
        writer.writerow([counter, time.time()-startTime, distance])

        # print to console every 10 itterations. % is modulo operator
        if counter % 10 == 0:
            print(distance)
        
        time.sleep(0.01) # delay to keep UART bus for getting overloaded

# press ctrl+c while the console is active to terminate the program
except KeyboardInterrupt:
    board.close()
    f.close() # close file gracefully when program is terminated