# 4. Pendulum Experiment
The module is an experiment where we use the ultrasonic distance sensor to collect data about a pendulum undergoing damped simple harmonic motion.

## Experimental setup and procedure
The setup for this experiment requires. The most important thing is that the pendulum is aimed squarely at the large, flat surface on the pendulum at all times during the oscillations. This means it is important that you do not make the amplitude of the oscillations too large.

### Equipment
- Cardboard
- String
- Hole-punch
- Mass
- Stand for suspending the pendulum
- Box or similar for the sensor to sit on

## Setup
1. Cut out a rectangle in cardboard that is about 5 cm by 10 cm.
2. Use a hole-punch to make three holes in it. Two holes are in the upper left and right corner for attaching the string, and one is at the bottom center for suspending the mass.
3. Tie a string through the top holes.
4. Hang the string on the stand (not sure what this will be yet).
5. Position the ultrasonic sensor so that it points directly at the cardboard cutout as the pendulum oscillates.

![](Images/setup.jpg)

## Code
Used the code you developed during the last module to measure the distance and print it to a file. The code below can also be used as a starting point, including a fairly accurate time to distance calibration.

```python
from Arduino import Arduino
import time

# NEW, import csv library
import csv

PORT_NAME = '/dev/tty.usbserial-1420' # MUST BE UPDATED TO USE THE CORRECT PORT
FILE_NAME = 'pendulum_data_MK.csv'    # name of file that data will be written to
PIN_SENSE = 12                        # pin where ultrasic sensor is connected

# connect to Arduino
board = Arduino('9600', port=PORT_NAME)
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
    f.close() # close file gracefully when program is terminated
```

## Procedure
1. Excite the pendulum so that it starts oscillating. Make sure it moves about 10 cm away from the equilibrium position in either direction.
2. Start the Python program to collect data.
3. Wait for the oscillations to die down before stopping data-collection. 20 seconds of data will be more than enough, but you can collect for longer if you want to.
4. Change the name of the file that data is being printed to if you're going to redo the experiment. This makes it easy to see which data-points corresponds to which runs of the experiment.


## Data Analysis
For analyzing the data, we can continue using Spyder to write and run code. Another tool designed explicitly for this type of work is known as `Jupyter Notebook`. You can install and launch Jupyter from the Anaconda Navigator in the same way you have been using Spyder. The following instructions have been written using a Jupyter notebook that you can open and copy code from, or that you can download and use as a starting point for your work.

[Jupyter Notebook with data analysis.](Data_Analysis.ipynb)
