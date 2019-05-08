# Screen Display Tutorial

This instruction set covers connecting the small display screen to the Arduino Nano and using it to display text. This is useful for outputting results from sensors directly on the Arduino.

## Updating Arduino and Python Libraries

To be able to pass commands to the screen, you must have the latest control libraries installed. These come in two parts, one for the Arduino Nano itself, and the other for your computer's Python installation. Ask a TA for help to get the Arduino updated. 

To get the library on your computer, you need to uninstall and reinstall the `arduino-python3` package through `pip`. To do so, run the following commands in the terminal (accessed by right-clicking on the environment you are using in Anaconda).

```bash
pip uninstall arduino-python3
pip install arduino-python3
```

If successful, you should see that the package you have installed is version 0.5. You are now ready to connect the screen to the Arduino and display data.



## Connecting Screen to Arduino

The screen used has four pins. Two are dedicated to a 5 V connection and ground, while the other two exchange data with the Arduino. This connection type is known as an Inter-Integrated Circuit, or I2C. For the inquisitive, further reading on this type of connection [can be found here](https://en.wikipedia.org/wiki/I%C2%B2C).

The necessary ports can then be accessed by connecting the screen's SDA pin to the Arduino's A4, and SCK to A5, as can be seen on the diagram below. VCC and GND are connected to the Arduino's 5 V and ground pins, respectively. Note that the below diagram contains a different model of screen, but the pin names remain the same.

![Screen Connection Diagram](Images/screenConnection.png)

The screen is considered to be right-side-up when the pins are on the left-hand side, so take this into consideration when connecting your board.



## Displaying Text

Once the above has been completed, you are now ready to display text on the screen. The method to do so is very simple. Simply add

```pyt
board.displayText(text, font_size)
```

to your current code, where `text` is a string containing the text you want the board to display, and `font_size` is an integer which controls the size of the output text. 

This line should be placed at the end of your code, but before the `time.sleep()` command. An example of its usage is shown below.



## An Example

```python
# Import libraries
from Arduino import Arduino
import time

board = Arduino()  # find and connect microcontroller
print('Connected') # confirms the microcontroller has been found

try:
    while True:
        
        # Defines a dummy variable for distance.
        dist = 29
        
        # The displayText method only accepts strings, so we must convert the
        # distance measurement to a string as well.
        dist = str(dist)
        
        # For readability, we can add a label to the front of the string. This
        # 'adding' of strings is known as concatenation.
        dist = "Distance Measured: " + dist
       
        # Prints the distance to the screen, with font size 1.
        board.displayText(dist, 1)
        
        # Lets the system rest, so we don't attempt to print to it every tick.
        time.sleep(1)
        
# press ctrl+c while the console is active to terminate the program
except KeyboardInterrupt:
    board.close() # close the serial connection
```



## Recommended Exercises

1. Try experimenting with the `font_size` parameter of the method. What text size works best for displaying data? You can also introduce the newline character, `\n`, to a string to print on multiple lines.
2. Introduce the code you used previously with the ultrasonic sensor to display the distance measured in real time. Experiment with the refresh rate of the display to provide a smooth experience, while not overloading the serial connection with requests.
3. Displaying items on the screen takes a nonzero amount of time, and should be minimised in most applications. Use the `time` library function `time.time()` to print to the console the length of time  it took to display text. This simply returns the current time and date in seconds, so by measuring the difference between two calls, one may figure out how much time elapsed between them. [Documentation on the method is here](https://docs.python.org/3.5/library/time.html#time.time). How long does it take to display text as compared to the rest of the program?
