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

from bottle import post, route, request, run
import os, time, urllib

# Camera-specific parameters
param1 = '/main/capturesettings/f-number=f/'
param2 = '/main/capturesettings/shutterspeed2='
param3 = '/main/imgsettings/iso='
# Default gPhoto2 command
gphoto2_command = 'gphoto2 --capture-image-and-download --filename "%Y%m%d-%H%M%S-%03n.%C"'

@route('/')
@route('/', method='POST')
def release_control():
    if (request.POST.get("shutter_release")):
        os.system(gphoto2_command)
    if (request.POST.get("set-config")):
        aperture = request.forms.get('aperture')
        os.system('gphoto2 --set-config-value ' + param1 + aperture)
        shutterspeed = request.forms.get('shutterspeed')
        os.system('gphoto2 --set-config-value ' + param2 + shutterspeed)
        iso = request.forms.get('iso')
        os.system('gphoto2 --set-config-value ' + param3 + iso)
    if (request.POST.get("command")):
        cmd = urllib.unquote_plus(request.forms.get('cmd'))
        os.system('gphoto2 ' + cmd)
    if (request.POST.get("start")):
        number = int(request.forms.get('number'))
        interval = int(request.forms.get('interval'))
        os.system('gphoto2 --interval '+ str(interval) +' --frames ' + str(number) + ' --capture-image-and-download --filename "%Y%m%d-%H%M%S-%03n.%C"')
    if (request.POST.get("stop")):
            os.system("killall -KILL python")
    if (request.POST.get("shutdown")):
            os.system("sudo halt")
    return """
    <title>gPhoto2 Bottle</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <form method="POST" action="/">
    <div id="content"><p><input id="btn" class="green" name="shutter_release" type="submit" value="Shutter Release"></p>
    <p class="right">Aperture (e.g., 9): <input name="aperture" type="text" size="3"/></p>
    <p class="right">Shutter speed (e.g. 1/125): <input name="shutterspeed" type="text" size="3"/></p>
    <p class="right">ISO (e.g., 640): <input name="iso" type="text" size="2"/></p>
    <p><input id="btn" name="set-config" value="Set" type="submit" /></p>
    <p class="right">Command: <input name="cmd" type="text" size="25"/></p>
    <p><input id="btn" name="command" value="Command" type="submit" /></p>
    <p class="right">Photos: <input name="number" type="text" size="3"/> Interval: <input name="interval" type="text" size="3"/> sec.</p>
    <p><input id="btn" class="green" name="start" value="Start" type="submit" /></p>
    <p><input id="btn" class="orange" name="stop" value="Stop" type="submit" /></p>
    <p><input id="btn" class="red" name="shutdown" value="Shut down" type="submit" /></p>
    </form>
    <p class="left">Press <strong>Shutter Release</strong> for a single shot.</p>
    <p class="left">Use the approprite fields to specify aperture, shutter speed, and ISO values. Press <strong>Set</strong> to apply the settings.</p>
    <p class="left">Use the appropriate fields to specify the number of photos and the interval between them in seconds, then press <strong>Start</strong>.</p>
    <p class="left">To run a user-defined command, specify the desired command in the <em>Command</em> field and press the <strong>Command</strong> button.</p>
    <p class="left">Press <strong>Stop</strong> to terminate the app.</p>
    <p class="left">Press <strong>Shutdown</strong> to shut down the server.</p>
    </div>
    <style>
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,600,700' rel='stylesheet' type='text/css'>
    body {
        font: 15px/25px 'Open Sans', sans-serif;
    }
    p.left {
        text-align: left;
    }
    p.right {
        text-align: right;
    }
    #content {
        font: 15px/25px 'Open Sans', sans-serif;
        margin: 0px auto;
        width: 275px;
        text-align: left;
    }
    #btn {
        width: 11em;  height: 2em;
        background: #3399ff;
        border-radius: 5px;
        color: #fff;
        font-family: 'Open Sans', sans-serif; font-size: 25px; font-weight: 900;
        letter-spacing: 3px;
        border:none;
    }
    #btn.green {
        background: #009900;
    }
    #btn.orange {
        background: #ff9900;
    }
    #btn.red {
        background: #cc0000;
    }
    </style>
    """
run(host="0.0.0.0",port=8080, debug=True, reloader=True)
