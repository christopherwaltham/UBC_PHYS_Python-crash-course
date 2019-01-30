# Arduino Setup Instructions
This file contains instrucitons on how to download the Arduino IDE and upload sketches to microcontrollers.

## Setting up the Arduino IDE
- Download from: https://www.arduino.cc/en/Main/Software
- Configure for appropriate microcontroller and port by doing the following:
    - With the Arduino IDE open and active, go to “tools” -> “board” and select the board you want to upload a sketch to.
    - Go to “tools” again and set the “port” to the one the microcontroller is connected to. Most often you will only have one reasonable option to select, otherwise try them one after another and see if you are able to upload a sketch.
- To flash a program to the board, simply hit the “Upload” button. Watch the status messages at the bottom of the screen. If an error occurs, check the board and port is set correctly and that you do not have any syntax-errors in your sketch.

Tips: go to “File” -> “Examples” to find a large library of example sketches that for all sorts of applications. This is a very useful place to look to see how different tasks can be accomplished, and to have a starting point that you can modify for your own needs.
