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

If you cannot find a port with this type of format, it might be that you have to install the driver for the board manually. The [ch340g-ch34g-ch34x-mac-os-x-driver](https://github.com/adrianmihalko/ch340g-ch34g-ch34x-mac-os-x-driver) can be downloaded and installed using [Homebrew](https://brew.sh) (a package manager for Mac). Follow the installation instrucitons, or ask for help. 
