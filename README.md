# Introduction

The purpose of this project is to have information I find useful on my desk.

# Hardware
* Raspberry Pi Model 3
* 5" generic touch screen for pi

Think of this like a Magic Mirror but smaller.

# Installation
1. Install kivy following their instructions
2. `chmod +x main.py` after cloning / pulling.
3. Have main.py run on boot or login

## Running with LightDM
1. Add a file in `/usr/share/xsessions/koppar.desktop`
2. Fill it with:
    ```
    [Desktop Entry]
    Type=Application
    Exec=/path/to/koppar/main.py
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

# ToDo:
* dynamic screens? plugin loader?
* redo navigation -> maybe gestures?
* everything

# Credit

Images downloaded from: https://icons8.com/icon/pack/free-icons/plasticine
Raspberry Pi Case used: https://www.thingiverse.com/thing:3374265