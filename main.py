'''
using KY-020 tilt module connected to GPIO 0 
on ESP8266 
'''

import machine
import utime


def tilt_tester():
    tilt = machine.Pin(0, machine.Pin.IN)
    while True:
        tilt.value()
        utime.sleep(0.1)


'''
use the tilt_tester function to confirm the tilt sensor
is working and the angle is suitable for the application
'''

tilt_tester()


