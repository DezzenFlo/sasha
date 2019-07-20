import datetime
import time

first = input("Hour: ")
three = input("Minutes: ")
secondt = input("Second: ")

now = datetime.datetime.now()

datetime.time(now.hour, now.minute, now.second)

print(now.hour)
print(now.minute)
print(now.second)

alarm_hour = input("Alarm clock hour: ")
alarm_minutes = input("Alarm clock minutes: ")


while True:

    print(str(first) + ":" + str(three) + ":" + str(secondt))
    
    secondt = int(secondt) + 1
    time.sleep(1)
    
    if secondt == 60:
        secondt = 0
        three = int(three) + 1
        
    if three == 60:
        three = 0
        first = int(first) + 1
        
    if first == alarm_hour:
        print("Stand up!")
        #break
        
print("Out")