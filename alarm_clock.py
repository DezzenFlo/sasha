#from datetime import *
import time

hour = 12
minute = 59
seconds = 50

while True:

    print(str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(seconds).zfill(2))
    
    seconds = seconds + 1
    time.sleep(1)
    
    if seconds == 60:
        seconds = 0
        minute = minute + 1
        
    if minute == 60:
        minute = 0
        hour = hour + 1
        
    if hour == 24:
        hour = 0
        minute = 0
        seconds = 0