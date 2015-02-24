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
import os, time

param1 = '/main/capturesettings/f-number=f/'
param2 = '/main/capturesettings/shutterspeed2='
param3 = '/main/imgsettings/iso='

@route('/')
@route('/', method='POST')
def release_control():
    if (request.POST.get("shutter_release")):
        os.system('gphoto2 --capture-image-and-download --filename "%Y%m%d-%H%M%S-%03n.%C"')
    if (request.POST.get("set-config")):
        aperture = request.forms.get('aperture')
        os.system('gphoto2 --set-config-value ' + param1 + aperture)
        shutterspeed = request.forms.get('shutterspeed')
        os.system('gphoto2 --set-config-value ' + param2 + shutterspeed)
        iso = request.forms.get('iso')
        os.system('gphoto2 --set-config-value ' + param3 + iso)
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
    <div id="content"><p><input id="btn" name="shutter_release" type="submit" value="Shutter Release"></p>
    <p class="right">Aperture (e.g., 9): <input name="aperture" type="text" size="3"/></p>
    <p class="right">Shutter speed (e.g. 1/125): <input name="shutterspeed" type="text" size="3"/></p>
    <p class="right">ISO (e.g., 640): <input name="iso" type="text" size="2"/></p>
    <p><input id="btn" name="set-config" value="Set" type="submit" /></p>
    <p class="right">Photos: <input name="number" type="text" size="3"/> Interval: <input name="interval" type="text" size="3"/> sec.</p>
    <p><input id="btn" name="start" value="Start" type="submit" /></p>
    <p><input id="btn" class="stop" name="stop" value="Stop" type="submit" /></p>
    <p><input id="btn" class="shutdown" name="shutdown" value="Shut down" type="submit" /></p>
    </form>
    <p class="justify">Press <strong>Shutter Release</strong> for a single shot.</p>
    <p class="justify">Use the approprite fields to specify aperture, shutter speed, and ISO values. Press <strong>Set</strong> to apply the settings.</p>
    <p class="justify">Use the appropriate fields to specify the number of photos and the interval between them in seconds, then press <strong>Start</strong>.</p>
    <p class="justify">Press <strong>Stop</strong> to terminate the app.</p>
    <p class="justify">Press <strong>Shutdown</strong> to shut down the server.</p>
    </div>
    <style>
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,600,700' rel='stylesheet' type='text/css'>
    body {
        font: 15px/25px 'Open Sans', sans-serif;
    }
    p.justify {
    text-align: justify;
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
    #btn.stop {
        background: #ff9900;
    }
    #btn.shutdown {
        background: #cc0000;
    }
    </style>
    """
run(host="0.0.0.0",port=8080, debug=True, reloader=True)
