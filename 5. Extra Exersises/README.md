# After finishing the modules
After you have finished all the modules, you are free to spend time doing what you find interesting or especially challenging to improve. We recommend getting familiar with the programming the Arduino directly.

What we have been doing up until this point, has been communicating with a special program running on the Arduino that knows how to interpret messages sent from your computer using the Arduino-Python3 library. Instead of running this program on the Arduino, you can upload a program of your own where the functionality is not dependent on the computer continually sending messages. This gives you greater freedom and will speed up your commands significantly, as there is way less overhead associated with executing a command.

Spyder is a development environment designed for Python. Similarly, the Arduino IDE is a development environment designed for programming Arduino boards directly. The Arduino IDE is based on a flavor of the programming language C++. The syntax is a little different from what you are used to in Python, but the functions used here are the ones you are familiar with from the Arduino-Python3 library.

You can download the Arduino IDE from [here](https://www.arduino.cc/en/Main/Software). A good exercise is to try to recreate some of the programs you made with the Arduino-Python3 library, but now directly in the Arduino IDE.


## Suggested Exercises
- humidity sensor, using DHT function in the Arduino-Python3 library
- generate a live plot of data from the ultrasonic sensor
- research on the web/datasheets the protocol used by the temperature and humidity sensor and decode its messages manually on the oscilloscope.
- set up an LCD display with temp/humidity sensor to make a mini weather station.
- measure, on the scope, (a) how quickly you can toggle a GPIO pin in a loop with the Arduino-Python3 library. Then (b) do it again inside in the Arduino IDE. As an advanced bonus, (c) read up in the ATMEGA-328P data sheet how to set a GPIO pin directly using a register write (instead of using the Arduino library digitalWrite function).
- play with servo motors - the EP project lab must have hundreds.
- in python, print an ASCII table - learn about chr() and ord() and ASCII encoding.
- learn how numbers are stored on computers: integer types, signed/unsigned - 2's complement. Floating point types.

## Extra Topics
- Python exception handling
- types and Python's weak type system
- funky python syntax (such as one line loops)
- Git/GitHub
- command line
