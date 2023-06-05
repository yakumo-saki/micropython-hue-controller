# MicroPython Hue Controller for ESP8266

## how to develop

### basic

* boot.py is autostart script (by micropython)
* main.py is run after boot.py is finished (by micropython)

### transfer to board

`ampy -p /dev/ttyUSB0 put main.py`

### debugging

`ampy -p /dev/ttyUSB0 run main.py`

NOTE:

* This command is not transfer `main.py`. only run.
* After some seconds, ampy aborted with `'timeout waiting for first EOF reception'`. ignore this.

## TIPS

### ampy reset is not working

* `screen /dev/ttyUSB0 115200`
* hit `enter`
* prompt `>>>` is shown
* hit `ctrl+d` to soft reset
* exit screen by `ctrl+a -> k -> y`
