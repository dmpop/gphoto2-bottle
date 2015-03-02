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

try:
    import pifacecad
    cad = pifacecad.PiFaceCAD()
    cad.lcd.cursor_off()
    cad.lcd.blink_off()
    cad.lcd.clear()
except ImportError:
    print "pifacecad library is not installed."

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
def release_control():
    try:
        cad.lcd.clear()
        cad.lcd.backlight_on()
        cad.lcd.write('gPhoto2 Bottle is ready')
    except:
        print "pifacecad library is not installed."
    if (request.POST.get("shutter_release")):
        os.system(gphoto2_command)
        try:
            cad.lcd.backlight_on()
            cad.lcd.write('Done!')
        except:
            print "pifacecad library is not installed."
    if (request.POST.get("set-config")):
        aperture = request.forms.get('aperture')
        os.system('gphoto2 --set-config-value ' + param1 + aperture)
        shutterspeed = request.forms.get('shutterspeed')
        os.system('gphoto2 --set-config-value ' + param2 + shutterspeed)
        iso = request.forms.get('iso')
        os.system('gphoto2 --set-config-value ' + param3 + iso)
        try:
            cad.lcd.clear()
            cad.lcd.backlight_on()
            cad.lcd.write('Values have been set.')
        except:
            print "pifacecad library is not installed."
    if (request.POST.get("command")):
        cmd = urllib.unquote_plus(request.forms.get('cmd'))
        os.system('gphoto2 ' + cmd)
    if (request.POST.get("start")):
        number = request.forms.get('number')
        interval = request.forms.get('interval')
        os.system('gphoto2 --interval '+ str(interval) +' --frames ' + str(number) + ' --capture-image-and-download --filename "%Y%m%d-%H%M%S-%03n.%C"')
        try:
            cad.lcd.clear()
            cad.lcd.backlight_on()
            cad.lcd.write('Done!')
        except:
            print "pifacecad library is not installed."
    if (request.POST.get("stop")):
        try:
            cad.lcd.clear()
            cad.lcd.backlight_off()
            cad.lcd.write('Bye! :-)')
        except:
            print "pifacecad library is not installed."
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

run(host="0.0.0.0",port=8080, debug=True, reloader=True)
