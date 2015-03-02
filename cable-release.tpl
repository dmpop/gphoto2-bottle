<html>
<head>
    <title>Cable Remote</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="static/styles.css">
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,600,700' rel='stylesheet' type='text/css'>
</head>
<div id="content">
    <p class="center"><a href="help">Help</a></p>
    <form method="POST" action="/cr">
        <p><input id="btn" name="cable-release" type="submit" value="Shutter Release"></p>
        <p class="right">Photos: <input name="number" type="text" size="3"/> Interval: <input name="interval" type="text" size="3"/> sec.</p>
        <p><input id="btn" name="start" value="Start" type="submit" /></p>
        <p><input id="btn" class="orange" name="stop" value="Stop" type="submit" /></p>
        <p><input id="btn" class="red" name="shutdown" value="Shut down" type="submit" /></p>
    </form>
</div>
</html>
