#!/usr/bin/env python 

import sys 
import time 
import RPi.GPIO as io  
import subprocess 

io.setmode(io.BOARD) 
SHUTOFF_DELAY = 3 # секунды 
PIR_PIN=4 

def main(): 
    io.setup(PIR_PIN, io.IN) 
    turn_off = False 
    last_motion_time = time.time() 
    while True: 
        if io.input(PIR_PIN): 
            last_motion_time = time.time() 
            sys.stdout.flush() 
            if turn_off: 
                turn_off = False 
                turn_on() 
        else: 
            if not turn_off and time.time() > (last_motion_time + SHUTOFF_DELAY): 
                turn_off = True 
                turn_off() 
            if not turn_off and time.time() > (last_motion_time + 1): 
                time.sleep(.1) 
def turn_on(): 
    subprocess.call("sh /home/pi/MagicMirror/monitor_on.sh", shell=True) 

def turn_off(): 
    subprocess.call("sh /home/pi/MagicMirror/monitor_off.sh", shell=True) 

if __name__ == '__main__': 
    try: 
        main() 
    except KeyboardInterrupt: 
        io.cleanup()
