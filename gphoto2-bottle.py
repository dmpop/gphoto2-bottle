#!/usr/bin/python

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from bottle import post, route, request, static_file, template, run
from subprocess import Popen, PIPE
import os, time, urllib

#Import the RPi.GPIO module
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #Turn the LED on pin 27 on (indicates that the server is up and running)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, True)
except ImportError:
    pass

# Camera-specific parameters
param1 = '/main/capturesettings/f-number=f/'
param2 = '/main/capturesettings/shutterspeed2='
param3 = '/main/imgsettings/iso='
# Default gPhoto2 command
gphoto2_command = 'gphoto2 --capture-image-and-download --filename "%Y%m%d-%H%M%S-%03n.%C"'

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
@route('/', method='POST')
def releasecontrol():
    if (request.POST.get("shutter-release")):
        os.system(gphoto2_command)

    if (request.POST.get("set-config")):
        aperture = request.forms.get('aperture')
        os.system('gphoto2 --set-config-value ' + param1 + aperture)
        shutterspeed = request.forms.get('shutterspeed')
        os.system('gphoto2 --set-config-value ' + param2 + shutterspeed)
        iso = request.forms.get('iso')
        os.system('gphoto2 --set-config-value ' + param3 + iso)

    if (request.POST.get("get-all-files")):
        os.system('gphoto2 --get-all-files')
    if (request.POST.get("command")):
        cmd = urllib.unquote_plus(request.forms.get('cmd'))
        os.system('gphoto2 ' + cmd)
    if (request.POST.get("start")):
        number = request.forms.get('number')
        interval = request.forms.get('interval')
        os.system('gphoto2 --interval '+ str(interval) +' --frames ' + str(number) + ' --capture-image-and-download --filename "%Y%m%d-%H%M%S-%03n.%C"')
    if (request.POST.get("stop")):
        os.system("killall -KILL python")
    if (request.POST.get("shutdown")):
        os.system("sudo halt")
    output = template('gphoto2-bottle.tpl')
    return output

@route('/config')
def config():
    output = Popen(["gphoto2", "--list-config"], stdout=PIPE).communicate()[0]
    return  """
        <title>gPhoto2 Bottle Config</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="static/styles.css">
        <link href='http://fonts.googleapis.com/css?family=Oxygen+Mono' rel='stylesheet' type='text/css'>
        <p class="mono"><a href="../">Back</a></p><p class="mono">
        """ + output + "</p>"

@route('/help')
def help():
    output = template('help.tpl')
    return output

#Cable release interface
def trigger():
    try:
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(25, GPIO.OUT)
        GPIO.output(23, True)
        time.sleep(0.5)
        GPIO.output(25, True)
        time.sleep(0.5)
        GPIO.output(25, False)
        GPIO.output(23, False)
    except:
        pass

@route('/trigger')
@route('/trigger', method='POST')
def switch():
    if (request.POST.get("trigger")):
        trigger()
    if (request.POST.get("start")):
        i = 1
        number = int(request.forms.get('number'))
        interval = int(request.forms.get('interval'))
        while (i <= number):
            trigger()
            time.sleep(interval)
            i = i + 1
    if (request.POST.get("stop")):
            try:
                GPIO.output(27, False)
            except:
                print "RPi.GPIO library is not installed."
            os.system("killall -KILL python")
    if (request.POST.get("shutdown")):
            os.system("sudo halt")
    output = template('trigger.tpl')
    return output

run(host="0.0.0.0",port=8080, debug=True, reloader=True)
