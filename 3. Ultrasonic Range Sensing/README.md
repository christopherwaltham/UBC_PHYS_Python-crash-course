# 3. Ultrasonic Range Sensing

## Theory
Describe operating principle

## Sensor module
Describe interaction with sensor module, what functions are performed on the device, what functions must be performed by the Python script.

## Code
### Get distance mesurnments
Use of function `Arduino.pulseIn_set`

### Writing to file
Use of `csv` library

### Handeling exceptions
Dealing with no pulse return to allways get clean output values

## Calibrating time constant
Look at time mesurnments and corresponding distance traveled by sound. Determine scaling factor and thereby find the speed of sound in air.
