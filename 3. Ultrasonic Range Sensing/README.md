# 3. Ultrasonic Range Sensing

## Theory
The HC-SR04 is an inexpensive distance sensor that is easy to work with. It uses two ultrasonic transducers, one acting as a speaker and one serving as a microphone. The left transducers emit a high-frequency sound pulse that travels through the air. When it hits a solid surface, these pulses are reflected back towards the module. This echo is registered by the microphone. The time required for the sound to make the trip away and back is used to determine how far the sound has traveled, and thus the distance to the obstacle.

![](Images/sensor_operation.png)

## Sensor module
The ultrasonic sensor module makes it easy to get distance data by abstracting out a lot of the work associated with actuating the speaker and recognizing the echoes.

It has a 4 pin interface:
- PWR is power. It is connected to 5V.
- GND is ground. It is connected to a ground pin of the microcontroller.
- TRIG is the trigger pin. It is connected to a digital pin of the microcontroller.
- ECHO is the echo pin. It is connected to a digital pin of the microcontroller.

In our case, we will connect TRIG and ECHO to the same pin, as this will enable us to use a convenient function in the Arduino-Python library called `pulseIn_set`.

Getting a distance measurement from the module works like this:
- When you want to make a distance measurement, send a quick pulse to the sensor on the trigger line.
- The ultrasonic module with use the speaker to send out a sound-pulse and wait for an echo to come back.
- When the module detects an echo, it sends a pulse to the microcontroller over the ECHO wire.
- The time difference between when the trigger pulse was transmitted and when the echo pulse returned can be used to determine how far the sound has traveled (distance = speed * time).


## Code
### Get distance measurements

In your code, you will need to keep track of how long it has taken from the trigger pulse was sent to the echo returns. We could write this functionality manually, but it is much easier to use a library function called `pulseIn_set`. This function sends a message to the Arduino to send a pulse (high indicates the pulse should be positive), and start a timer. The function returns when a pulse has been received with the time (in microseconds) that the sound has spent traveling.

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

### Calibrating
By using a ruler, you can manually determine how far the sound has traveled


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

### Handling exceptions
Dealing with no pulse return to always get clean output values

## Calibrating time constant
Look at time measurements and corresponding distance traveled by sound. Determine scaling factor and thereby find the speed of sound in air.


## Complete sketch



Next: [Module 4: Pendulum Experiment](/4.%20Pendulum%20Experiment/)
