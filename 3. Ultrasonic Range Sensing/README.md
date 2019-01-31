# 3. Ultrasonic Range Sensing

## Theory
Describe operating principle

## Sensor module
Describe interaction with sensor module, what functions are performed on the device, what functions must be performed by the Python script.

## Code
### Get distance mesurnments
Use of function `Arduino.pulseIn_set`


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
Use of `csv` library

### Handeling exceptions
Dealing with no pulse return to allways get clean output values

## Calibrating time constant
Look at time mesurnments and corresponding distance traveled by sound. Determine scaling factor and thereby find the speed of sound in air.


## Complete sketch



Next section: [Pendulum Experiment](/4.%20Pendulum%20Experiment/)
