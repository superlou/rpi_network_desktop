# Raspberry Pi Network Desktop

This application creates an image and sets the desktop background using `pcmanfm`. This is helpful for finding the device on a network if you have an HDMI connection.

To autostart this on login, create a `.desktop` file in `~/.config/autostart` containing:

```
[Desktop Entry]
Type=Application
Exec=python3 /home/pi/workspace/cloned_location/main.py

```

