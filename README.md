## gPhoto2 Bottle

gPhoto2 Bottle is a simple web app based for controlling cameras supported by [gPhoto2](http://www.gphoto.org/) software. The app is based on the [Bottle](http://bottlepy.org/) framework. The app is designed for use with Raspberry Pi, but it should run on any Debian or Ubuntu machine.

<img src="gphoto2-bottle.png" alt="gPhoto2 Bottle">

## Dependencies

* Python
* Python Bottle
* gPhoto2
* Git (optional)

## Install and Run

1. Clone the project's repository using the `git clone https://github.com/dmpop/gphoto2-bottle.git` command. Switch to the resulting *gphoto2-bottle* directory.
2. Compile and install gPhoto 2.5.2 by running the `sudo ./gphoto2-updater.sh` command. This step is required only if the official repositories contain version of gPhoto2 lower than 2.5.2.
3. Install the Bottle framework using the `sudo apt-get install python-pip` and `sudo pip install bottle` commands.
4. Launch the app by running the `sudo ./gphoto2-bottle.py` command.
5. Make sure that your camera connected to the machine running gPhoto2 Bottle via a USB cable.
6. Point the browser to http://127.0.0.1.8080/ (replace *127.0.0.1* with the actual IP address of the machine running gPhoto2 Bottle) to access and use the app.

## PiFace Command and Display Support

gPhoto2 Bottle provides rudimentary support for [PiFace Command and Display](http://www.piface.org.uk/products/piface_control_and_display/). To enable this functionality install the *pyfacecad* library using the `sudo apt-get install python{,3}-pifacecad` command.
