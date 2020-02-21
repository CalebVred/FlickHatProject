#Using python 3, circuitpython.
#@Author: Caleb vredevoogd (cvredevoogd99@gmai.com)

import time
import digitalio
import signal
import subprocess
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

def main():
    while True:
        s = subprocess.check_output(["python", "flickscroll.py"])
        #TODO: turn output from flickscroll into mouse data
