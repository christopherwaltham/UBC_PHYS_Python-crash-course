# Finding USB Port Name for Arduino
Every time you connect the Arduino to your computer, it will be assigned a port name so that you and software can reference it. This name may change every time you connect the device.

## Windows
- Open _Device Manager_
- Expand the _Ports (COM & LPT)_ list

A typical port name for Windows is `COM3`

## Mac
- Open the _terminal_
- Type the command `ls /dev/*`

A typical port name for macOS is `/dev/tty.usbserial-1410`
