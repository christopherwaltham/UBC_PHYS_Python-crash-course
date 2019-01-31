
# 2. Arduino for Data Collection

[Arduino](https://www.arduino.cc) is a platform of [microcontrollers](https://en.wikipedia.org/wiki/Microcontroller) that has a large user-base, and that is easy to work with. These microcontrollers are programmed in a language developed for the Arduino boards, which is closely related to the programming language called [C](https://en.wikipedia.org/wiki/C_(programming_language)). Learning two programming languages at once is not easy, so we have already uploaded code on the boards so that you can control it by sending it commands from Python.

To communicate with the microcontroller, you will be using a [serialized communication](https://en.wikipedia.org/wiki/Serial_communication) method simply known as Serial. It encodes the information you want to send into a sequence of bits (zeros and ones) and sends them one by one through a single wire. Two more wires are also required: ground to give the computers a shared reference, and a clock to communicate when a new bit has been sent.

Python has libraries that know how to decode information and send it over this serial link so that we do not need to know anything about how it is implemented. One of these libraries is called Arduino-Python.

## Installing Arduino-Python
Arduino-Python is not available through the package manager in Anaconda. We, therefore, need to use _pip_, which is another package manager
 - Go to Anaconda and select the environments tab.
 - Click the play button next to the Python environment you set up earlier.
 - Click "Open Terminal".
 - Type `pip install arduino-python` followed by return.
 - The library should now be installed. Quit the Terminal/Command Line window, and return to Spyder.

## Connecting an LED to the microcontroller
- Introduction to the breadboard
- Introduction to LEDs, polarity and the need for a current limiting resistor
- Introduction to Arduino pins and digital voltage levels
- Schematic for connecting LED to a microcontroller

## Quick user guide
Now, you can control the Arduino by typing the following lines of code into Spyder. After starting the program, some seconds may pass, but then the LED should start flashing rapidly.

```python
from Arduino import Arduino   # import library
import time

board = Arduino('9600')       # find and connect microcontroller
board.pinMode(13, "OUTPUT")   # configure pin 13 to be an output pin

# enter infinite loop
while True:
    board.digitalWrite(13, "LOW")   # set pin low (0V)
    time.sleep(1)                   # wait 1 second
    board.digitalWrite(13, "HIGH")  # set pin high (5V)
    time.sleep(1)                   # wait 1 second
```

If it does not work, it might be because the computer is not automatically able to determine which USB port the Arduino is plugged into. Go to system settings to find the name of the port and change line 3 to `board = Arduino('9600', port='PORT_NAME')` where PORT_NAME is replaced by the port name that the Arduino is connected to on your computer. On a Windows machine, the port name is typical `COM3` or something similar, whereas on a Mac the port name typically will look like `/dev/tty.usbmodem143201`.
