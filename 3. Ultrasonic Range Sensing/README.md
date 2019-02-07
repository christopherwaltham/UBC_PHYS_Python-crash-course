# 3. Ultrasonic Range Sensing

## Theory
The HC-SR04 is an inexpensive distance sensor that is easy to work with. It is uses two ultrasonic transducers, one acting as a speaker and one acting as a microphone. The left transducers emits a high frequency sound pulse that travels thorugh the air. When it hits a solid surface, these pulses are reflected back at the microphone. The time required for the sound to make the trip away and back is used to determine how far the sound has traveled, and thus how far away the obsticle is.

![](Images/sensor_operation.png)

## Sensor module
The ultasonic sensor module makes it easy to get distance data. It has a 4 pin interface: two pins for power and ground, one pin for a trigger and one pin for the echo. It works like this:
- When you want to make a distance mesurnment, send a quick pulse to the sensor on the trigger line.
- The sensor will send out a sound-pulse and wait for an echo to come back.
- When the module detects an echo, it sends a pulse on the echo line.
- The time difference between when the trigger pulse was sent and when the echo pulse returned can be used to determine how far the sound has traveled.


## Code
### Get distance mesurnments

In your code, you will need to keep track of how long it has taken from the trigger pulse was sent to the echo returns. We could write this functionality manually, but it is much easier to use a library function called `pulseIn_set`. This function sends a message to the Arduino to set the pin high, and start a timer. The function returns when a pulse has been recieved, providing the time (in microseconds) that the sound has spent traveling.



```python
from Arduino import Arduino
import time

PORT_NAME = 'COM3' # MUST BE UPDATED TO USE THE CORRECT PORT

board = Arduino('9600', port='PORT_NAME')
print('Connected')

while True:
    pulseTime = board.pulseIn_set(13, 'HIGH')
    print(pulseTime)

    time.sleep(1)
```

### Writing to file
You can use the `csv` library to write data to a file. This can be very useful for data analysis later.

```python
from Arduino import Arduino
import time

# NEW, import csv library
import csv

PORT_NAME = 'COM3' # MUST BE UPDATED TO USE THE CORRECT PORT

board = Arduino('9600', port='PORT_NAME')
print('Connected')

while True:
    pulseTime = board.pulseIn_set(13, 'HIGH')
    print(pulseTime)

    # open a csv file and write time and pulseTime to it
    with open("test_data.csv","a") as f:
        writer = csv.writer(f,delimiter=",")
        writer.writerow([time.time(), pulseTime])

    time.sleep(0.5) # wait 0.5 seconds
```

### Handeling exceptions
Dealing with no pulse return to allways get clean output values

## Calibrating time constant
Look at time mesurnments and corresponding distance traveled by sound. Determine scaling factor and thereby find the speed of sound in air.


## Complete sketch



Next section: [Pendulum Experiment](/4.%20Pendulum%20Experiment/)
