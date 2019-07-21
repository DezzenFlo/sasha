import datetime
import time
import winsound

now = datetime.datetime.now()

datetime.time(now.hour, now.minute, now.second)

first = now.hour
three = now.minute
secondt = now.second


#a= int(input(": "))
b= int(input("Через сколько вы хотите встать(в минутах): "))

min = b * 60
time.sleep(min)

temp = 500
while True:

	winsound.Beep(temp, 100)
	temp = temp + 10
