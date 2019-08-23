import datetime
import time
import winsound
def(alarm):
    now = datetime.datetime.now()

    hour = int("%d" % now.hour)
    minute = int("%d" % now.minute)
    seconds = int("%d" % now.second)

    print("What time to set the alarm: ")
    print("")
    a = input("Hours: ")
    print("")
    b = input("Minuts: ")
    print("")

    while (hour != a and minute != b and seconds != 0):

        print(str(hour) + ":" + str(minute) + ":" + str(seconds))

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


    print("ПОДЪЁМ")
    winsound.Beep(3000,100)
    winsound.Beep(2500,100)
    winsound.Beep(2000,100)
    winsound.Beep(1500,100)
    winsound.Beep(1000,100)
    winsound.Beep(500,100)
alarm()
