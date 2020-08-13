# Introduction

The purpose of this project is to have information I find useful on my desk.

# Hardware
* Raspberry Pi Model 3
* 5" generic touch screen for pi

Think of this like a Magic Mirror but smaller.

# Installation
1. Install kivy following their instructions
2. `chmod +x koppar.sh` after cloning / pulling. Maybe not
3. Have koppar.sh run on boot or login
4. Launch with `-m inspector` and press Ctrl+E to debug the application

## Running with LightDM
1. Add a file in `/usr/share/xsessions/koppar.desktop`
2. Fill it with:
    ```
    [Desktop Entry]
    Type=Application
    Exec=/path/to/koppar/koppar.sh
    Name=Koppar
    Comment=Testing
    ```
3. Modify your LightDM config in `/etc/lightdm/lightdm.conf`
4. Find these lines and enable them:
    ```
    autologin-guest=false
    autologin-user=pi
    autologin-user-timeout=0
    ```
5. Logout and then set the desktop environment to your new Koppar app. I don't know how to do this from the LightDM config file.

## Calibrating Touchscreen
1. `sudo su`
2. `aptitude install libts-bin`
3. This will create a configuration file called /etc/ts.conf
4. `export TSLIB_TSDEVICE=/dev/input/event0`
5. `export TSLIB_FBDEVICE=/dev/fb0`
6. `ts_calibrate`
7. This calibration data will be written to a calibration file called /etc/pointercal.
8. `ts_test`
9. Reboot.

# ToDo:
* dynamic screens? plugin loader?
* redo navigation -> maybe gestures?
* everything

# Credit

Images downloaded from: https://icons8.com/icon/pack/free-icons/plasticine
Raspberry Pi Case used: https://www.thingiverse.com/thing:3374265