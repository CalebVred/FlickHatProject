"""
@Author: Caleb Vredevoogd (cvredevoogd99@gmail.com)
A python program that uses CircuitPython and Flick to turn the Raspberry Pi into a gesture-controlled scroll wheel
"""

import flicklib
import signal
import time
import digitalio
import sys
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)
xpos = 0
ypos = 0

@flicklib.move()

def main():
    global xyztxt

    xyztxt = ''
while True:
    #string parsing source, using in[] and out[]: https://stackoverflow.com/questions/5749195/how-can-i-split-and-parse-a-string-in-python
    #x and y should remain between 0 and 1 to read finger input
    #z should remain below .200 to read finger input
    #read input by parsing xyztxt
    xyzlist = xyztxt.split(" ")
    xp = float(xyzlist[0])
    yp = float(xyzlist[1])
    zp = float(xyzlist[2])

    #Output xyzlist to stdout
    stdout_xyz = sys.stdout
    for coord in xyzlist:
        print coord,

main()
