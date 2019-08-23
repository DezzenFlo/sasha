import datetime
import time
import winsound

now = datetime.datetime.now()

datetime.time(now.hour, now.minute, now.second)

first = now.hour
three = now.minute
secondt = now.second



b= int(input("Через какое время вы хотите поставить таймер (в минутах): "))

min = b * 60
time.sleep(min)

winsound.Beep(3000,100)
winsound.Beep(2500,100)
winsound.Beep(2000,100)
winsound.Beep(1500,100)
winsound.Beep(1000,100)
winsound.Beep(500,100)