<html>
<head>
    <title>gPhoto2 Bottle</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="static/styles.css">
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,600,700' rel='stylesheet' type='text/css'>
</head>
<div id="content">
    <form method="POST" action="/">
        <p class="center"><a href="config">View config</a> | <a href="help">Help</a></p>
        <p><input id="btn" class="green" name="shutter_release" type="submit" value="Shutter Release"></p>
        <p class="right">Aperture (e.g., 9): <input name="aperture" type="text" size="3"/></p>
        <p class="right">Shutter speed (e.g. 1/125): <input name="shutterspeed" type="text" size="3"/></p>
        <p class="right">ISO (e.g., 640): <input name="iso" type="text" size="2"/></p>
        <p><input id="btn" name="set-config" value="Set" type="submit" /></p>
        <p class="right">Command: <input name="cmd" type="text" size="21"/></p>
        <p><input id="btn" name="command" value="Command" type="submit" /></p>
        <p class="right">Photos: <input name="number" type="text" size="3"/> Interval:
            <input name="interval" type="text" size="3"/> sec.</p>
            <p><input id="btn" class="green" name="start" value="Start" type="submit" /></p>
            <p><input id="btn" class="orange" name="stop" value="Stop" type="submit" /></p>
            <p><input id="btn" class="red" name="shutdown" value="Shut down" type="submit" /></p>
        </form>
</div>
</html>
