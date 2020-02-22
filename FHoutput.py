#Using python 3, circuitpython.
#@Author: Caleb vredevoogd (cvredevoogd99@gmai.com)

#import time
#import digitalio
#import signal
import subprocess
import usb_hid
from adafruit_hid.mouse import Mouse

m = Mouse(usb_hid.devices)

def main():
    while True:
        s = subprocess.check_output(["python", "FHinput.py"])
        xyzlist = s.split(" ")
        
        #Take input and store into variables
        xp = xyzlist[0]
        yp = xyzlist[1]
        zp = xyzlist[2]

        if zp <.200:
            if xp<.5:
                m.move(0,0,-1)
            if xp > .5:
                m.move(0,0,1)
            else:
                m.move(0,0,0)
