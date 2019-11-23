import os
import sys
import time
import webbrowser 
import datetime
#from pydub import AudioSegment
#from pydub.playback import play
#import pyperclip
import keyboard
#import win32com.client
#from tkinter import * 
#from tkinter import messagebox
#from tkinter import Entry, Label,Tk
import psutil
import pyautogui
from pyautogui import press, typewrite, hotkey
import random


import time_timer
import time_alarm_clock
import parser_weather
import computer_off
import vk
import time_time_now
import socket



# слова Саши ----------------------------------------------------------------------------------------------------------------------
"""
song_da            = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster_2\\Voice of Lera\\Да.wav')
song_ay_ne_ponayla = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster_2\\Voice of Lera\\Повторите.wav')
song_govorite      = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster_2\\Voice of Lera\\Слушаю.wav')
song_odnu_minutku  = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster_2\\Voice of Lera\\Сечас.wav')
song_net           = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster_2\\Voice of Lera\\Нет.wav')
song_vi_skazali    = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster_2\\Voice of Lera\\Вы сказали.wav')
song_net_ne_mogu   = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster_2\\Voice of Lera\\Нет не могу.wav')
song_nu_poprobuy   = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster_2\\Voice of Lera\\Ну попробуй.wav')
song_odnu_minutku_1= AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster_2\\Voice of Lera\\Открываю.wav')


# графический интерфейс------------------------------------------------------------------------------------------------------------

root = Tk()
root.geometry('1280x720')
root.title('StayCool')
root.configure(background = '#202225')	

photo = PhotoImage(file="G:\\на новую винду\\сойдёт.png")
T = Text(root, height=20, width=117, bg='#292b2f', fg='#43b581',selectforeground='#000000',selectbackground='#708090',font = "Arial 14")




btn3 = Button(text="Settings",
				height=4, width=13,           
	            background="#292b2f",     
	            foreground="#43b581",     
	            padx="1",             
	            pady="1",              
	            font="16",
	            command = lambda:vk.new_1()
	            )
btn1 = Button(text="Settings",
				height=4, width=13,           
	            background="#292b2f",     
	            foreground="#43b581",     
	            padx="1",             
	            pady="1",              
	            font="16",
	           
	            )
btn2 = Button(text="Settings",
				height=4, width=13,           
	            background="#292b2f",     
	            foreground="#43b581",     
	            padx="1",             
	            pady="1",              
	            font="16",
	            
	            )
btn4 = Button(text="Settings",
				height=4, width=13,           
	            background="#292b2f",     
	            foreground="#43b581",     
	            padx="1",             
	            pady="1",              
	            font="16",
	            
	            )
btn5 = Button(text="Settings",
				height=4, width=13,           
	            background="#292b2f",     
	            foreground="#43b581",     
	            padx="1",             
	            pady="1",              
	            font="16",
	            
	            )



T.grid(row=0, column=1,rowspan=5)
btn3.grid(row=0, column=0)
btn1.grid(row=1, column=0)
btn2.grid(row=2, column=0)
btn4.grid(row=3, column=0)
btn5.grid(row=4, column=0)

"""


# настройки------------------------------------------------------------------------------------------------------------------------


 
# запуск



	
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.0.103', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
	print(sys.stderr, 'waiting for a connection')
	connection, client_address = sock.accept()
    
	print(sys.stderr, 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
    
	data = connection.recv(1024)
            #print(sys.stderr, 'received "%s"' % data)

            #sata = data.encode("utf-8")
	sata = data.decode('utf-8')
	print(sata)
	#os.system(sata)
	opts = {
    "alias": ('Саша', 'сашуля', 'александра', 'саня', 'санёк', 'Санек', 'сашуль', 'саша'),
    "tbr"  : ('скажи','расскажи','покажи','сколько','произнеси', 'включи', 'открой', 'создай','поставь', 'на'),
    "cmds": {
        "ctime"       : ('текущее время', 'сейчас времени', 'который час', 'времени', 'время'),
        "radio"       : ('музыку', 'музыка'),
        "stupid1"     : ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты'),
        "YouTube"     : ('ютуб', 'видео', 'любое видео', 'YouTube'),
        "vk"          : ('вк', 'в контакте', 'вконтакте', 'vk'),
        "serials"     : ('сериал', 'фансиреалс', 'фан сиреалс', 'фансериалс', 'фан ссериалс'),
        "kino"        : ('кино', 'киного', 'кино го', 'кино go', 'kinogo', 'kino go'),
        "elctroshop"  : ('зеон', 'zeon'),
        "koding"      : ('питон', 'саблайм', 'sublime', 'код', 'кодинг', 'сайт'),
        "firefox"     : ('browser', 'internet', 'браузер', 'интернет', 'яндекс'),
        "calkulaytor" : ('калькулятор'),
        "ccmmdd"      : ('cmd', 'цмд', 'c m d', 'ц м д ', 'system call', 'систем кол', 'систем колл'),
        "help"        : ('диспетчер задач'),
        "osu"         : ('osu', 'осу', 'o s y ', 'о с у'),
        "kalender"    : ('календарь', 'дата', 'дату', 'месяц', 'сегодняшнюю дату'),
        "notepack"    : ('заметки', 'блокнот', 'текстовый документ'),
        "setinks"     : ('настройки', 'параметры'),
        "photoshop"   : ('фотошоп', 'photoshop', 'фото редактор', 'фото redactor', 'photo redactor', 'photoredactor'),
        "megashop"    : ('куфар', 'рынок', 'место для барыг', 'беларусский авито', 'беларусский avito'),
        "github"      : ('git hub', 'github', 'гитхаб', 'гит хаб'),
        "АлиЭкспресс"  : ('алиэкспрес', 'АлиЭкспресс', 'алиекспрес', 'алиекспрэс', 'алиэкспрэс', 'али', 'ali', 'AliExpress', 'дом китайцев'),
        "repit"       : ('повтори за мной', 'повтори за мною', 'повтори', 'повторяй', 'повторяй за мной'),
        "выключи компьютер"         : ('выключи','выключи компьютер','офни','офни пк','пк на минус','оф', 'ебало на 0'),
        "programs"    : (),
        "photoshop"   : (),
        "sublime"     : (),
        "word"        : (),
        "exel"        : (),
    	"max"         : ('отправь алине', 'напиши алине', 'отправь алине сообщение', 'напиши алине сообщение', '', '', '', ''),
    	"timer"       : ('таймер','времязасекатель', 'время засекатель'),
    	"weather"     : ('пагода', 'пагоду'),
    	"kill"        : ('прогармму'),
    	"stone"       : ('давай поиграем в игру')

	    }
	}
# переменные которыми буду пользоваться в функциях


 
# функции

 


            # обращаются к Саше
	cmd = sata

	for x in opts['alias']:
		cmd = cmd.replace(x, "").strip()

	for x in opts['tbr']:
		cmd = cmd.replace(x, "").strip()

	            # распознаем и выполняем команду





	 
	 

	 

	if cmd == 'ctime':
			# сказать текущее время
		time_time_now.time_now()

	#if cmd == 'пауза' or 'паузу':
			# сказать текущее время
		#press('space')


	name_1="Максиму" or "максиму"
	name_2="Ване"    or "ване"
	name_3="Никите"  or "никите"
	name_4="Коле"    or "коле"
	name_5="Толику"  or "толику"
	name_6="маме"    or "Маме"
	name_7="Лере"    or "лере"
	if cmd == " напиши " + name_1 + " сообщение":
		os.system("mspaint")




			
	if cmd == 'radio':
			# воспроизвести музыку
		play(song_odnu_minutku)
		os.system("C:\\Users\\Nikita\\Desktop\\fall_out_boy_-_immortals.mp3")

	if cmd == 'stupid1':
			# рассказать анекдот
		speak("[***] Мой разработчик не научил меня анекдотам ... Ха ха ха")
		
	if cmd == 'YouTube':
			# открыть ютуб
		
		#print("do")
		url = 'https://www.youtube.com'
		webbrowser.open(url)
		#print("posle")

	if cmd == 'vk':
			# открыть вконтакте
		#play(song_odnu_minutku)
		url = 'https://vk.com/feed'
		webbrowser.open(url)

	if cmd == 'сериал':
			# открыть сайт с сериалами 
		#play(song_odnu_minutku)
		url = 'http://fanserials.tv'
		webbrowser.open(url)
		
	if cmd == 'кино':
			# открыть сайт с кино
		#play(song_odnu_minutku)
		url = 'https://kinogo.by'
		webbrowser.open(url)
		
	if cmd == 'zeon':
			# открыть сайт електротехники
		#play(song_odnu_minutku)
		url = 'https://www.777555.by'
		webbrowser.open(url)
		
	if cmd == 'АлиЭкспресс':
			# открыть алиэкспресс
		#play(song_odnu_minutku)
		
		url = 'https://ru.aliexpress.com/?src=yandex&albch=search&acnt=7443951&isdl=y&aff_short_key=UneMJZVf&yclid=4096793462919695618'
		webbrowser.open(url)


	if cmd == 'timer':
		time_timer.timerr()

	if cmd == 'weather':
		#play(song_odnu_minutku_1)
		parser_weather.weather_parse()

	if cmd == 'гитхаб':
			# открыть гитхаб
		#play(song_odnu_minutku)
		url = 'https://github.com/'
		webbrowser.open(url)
		


	if cmd == 'photoshop':
		#play(song_odnu_minutku)
		os.startfile('C:\\Program Files\\Adobe\\Adobe Photoshop CS6 (x64)\\Photoshop.exe')
		
	if cmd == 'выключи компьютер':
		os.system("shutdown -s")

	if cmd == 'отмотай':
		press('left')

	if cmd == 'перемотай':
		press('right')

	if cmd == 'паузу':
			# сказать текущее время
		press('space')
		




