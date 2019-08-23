import os, sys

def off():
	a_0 = int(input('[&&&] Через сколько минут выключить твой компьютер? : '))
	a_1 = a_0 * 60
	a_2 = str(a_1)
	os.system('shutdown -s -t ' + a_2)
off()
