import datetime
import time
import winsound

now = datetime.datetime.now()

datetime.time(now.hour, now.minute, now.second)

first = now.hour
three = now.minute
secondt = now.second


a= int(input(": "))
b= int(input("Через сколько вы хотите встать(в секундах): "))

time.sleep(b)

for i in range(a):

    winsound.Beep(3000,100)
    winsound.Beep(2500,100)
    winsound.Beep(2000,100)    
    winsound.Beep(1000,100)    
    winsound.Beep(500,100)
