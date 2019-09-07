import os
import sys
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import webbrowser 
import pyttsx3
import datetime
from pydub import AudioSegment
from pydub.playback import play
import pyperclip
import keyboard
import win32com.client
from tkinter import * 
from tkinter import messagebox
from tkinter import Entry, Label,Tk
import psutil
import pyautogui

import time_timer
import time_alarm_clock
import parser_weather
import computer_off
import vk
import time_time_now


# слова Саши ----------------------------------------------------------------------------------------------------------------------

song_da            = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster\\Голос Саши\\Да.wav')
song_ay_ne_ponayla = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster\\Голос Саши\\Я вас не поняла.wav')
song_govorite      = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster\\Голос Саши\\Говорите.wav')
song_odnu_minutku  = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster\\Голос Саши\\Одну минутку.wav')
song_net           = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster\\Голос Саши\\Нет.wav')
song_vi_skazali    = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster\\Голос Саши\\Вы сказали.wav')
song_net_ne_mogu   = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster\\Голос Саши\\Нет не могу.wav')
song_nu_poprobuy   = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster\\Голос Саши\\Ну попробуй.wav')
song_odnu_minutku_1= AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\sashamaster\\Голос Саши\\Одну минутку_1.wav')

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




# настройки------------------------------------------------------------------------------------------------------------------------



opts = {
    "alias": ('саша', 'сашуля', 'александра', 'саня', 'санёк', 'санек', 'сашуль', 'саш'),
    "tbr"  : ('скажи','расскажи','покажи','сколько','произнеси', 'включи', 'открой', 'создай'),
    "cmds": {
        "ctime"       : ('текущее время', 'сейчас времени', 'который час', 'времени', 'время'),
        "radio"       : ('музыку', 'музыка'),
        "stupid1"     : ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты'),
        "youtube"     : ('ютуб', 'видео', 'любое видео', 'youtube'),
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
        "aliexpress"  : ('алиэкспрес', 'алиэкспресс' 'алиекспрес', 'алиекспрэс', 'алиэкспрэс', 'али', 'ali', 'aliexpress', 'дом китайцев'),
        "repit"       : ('повтори за мной', 'повтори за мною', 'повтори', 'повторяй', 'повторяй за мной'),
        "off"         : ('выключи','выключи компьютер','офни','офни пк','пк на минус','оф', 'ебало на 0'),
        "programs"    : (),
        "photoshop"   : (),
        "sublime"     : (),
        "word"        : (),
        "exel"        : (),
    	"max"         : ('отправь коле', 'напиши коле', 'отправь коле сообщение', 'напиши коле сообщение', '', '', '', ''),
    	"timer"       : ('таймер','времязасекатель', 'время засекатель'),
    	"weather"     : ('пагода', 'пагоду'),
    	"kill"        : ('прогармму')




        
        #"":(),
        #"":(),
        #"":(),
        #"":(),
        #"":(),
        #"":(),
        #"":(),
        #"":(),
        #"":(),
        #"":(),
        #"":(),
        #"":(),
        #"":(),
        #"":(),
        #"":(),

    }
}
 
# функции
def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()
 
def callback(recognizer, audio):
	try:
		voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
		T.insert(INSERT, "\n[***] Распознано: " + voice)
		

		if voice.startswith(opts["alias"]):
            # обращаются к Кеше
			cmd = voice

			for x in opts['alias']:
				cmd = cmd.replace(x, "").strip()

			for x in opts['tbr']:
				cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
			cmd = recognize_cmd(cmd)
			execute_cmd(cmd['cmd'])



 
	except sr.UnknownValueError:
		T.insert(INSERT, "\n[$#$] Голос не распознан!")

	except sr.RequestError as e:
		T.insert(INSERT, "\n[$#$] Неизвестная ошибка, проверьте интернет!")	

 
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC
 
def execute_cmd(cmd):
	if cmd == 'ctime':
		# сказать текущее время
		time_time_now.time_now()
		
	if cmd == 'radio':
		# воспроизвести музыку
		play(song_odnu_minutku)
		os.system("C:\\Users\\Nikita\\Desktop\\fall_out_boy_-_immortals.mp3")

	elif cmd == 'stupid1':
		# рассказать анекдот
		speak("[***] Мой разработчик не научил меня анекдотам ... Ха ха ха")
	
	elif cmd == 'youtube':
		# открыть ютуб
		play(song_odnu_minutku)
		url = 'https://www.youtube.com'
		webbrowser.open(url)

	elif cmd == 'vk':
		# открыть вконтакте
		play(song_odnu_minutku)
		url = 'https://vk.com/feed'
		webbrowser.open(url)

	elif cmd == 'serials':
		# открыть сайт с сериалами 
		play(song_odnu_minutku)
		url = 'http://fanserials.tv'
		webbrowser.open(url)
	
	elif cmd == 'kino':
		# открыть сайт с кино
		play(song_odnu_minutku)
		url = 'https://kinogo.by'
		webbrowser.open(url)
	
	elif cmd == 'elctroshop':
		# открыть сайт електротехники
		play(song_odnu_minutku)
		url = 'https://www.777555.by'
		webbrowser.open(url)
	
	elif cmd == 'aliexpress':
		# открыть алиэкспресс
		play(song_odnu_minutku)
		url = 'https://ru.aliexpress.com/?src=yandex&albch=search&acnt=7443951&isdl=y&aff_short_key=UneMJZVf&yclid=4096793462919695618'
		webbrowser.open(url)
	
	elif cmd == 'max':

		play(song_govorite)
		
		r = sr.Recognizer()
		with sr.Microphone(device_index = 1) as source:
			
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
		try:

			zadanie = r.recognize_google(audio, language="ru-RU").lower()
			
	

			
			url = 'https://vk.com/im?peers=c29_c12_349445941&sel=229541795'
			webbrowser.open(url)


			shell = win32com.client.Dispatch("WScript.Shell")
			time.sleep(7)
			pyautogui.click(766, 1046,duration=1)
			time.sleep(3)
			pyautogui.typewrite(zadanie,interval=0.25)
			time.sleep(3)
			shell.SendKeys("{ENTER}")




		except sr.UnknownValueError:
			play(song_ay_ne_ponayla)
			zadanie = command()
		return zadanie

		my_file.write(zadanie)


		url = 'https://vk.com/im?peers=c29_c12_349445941&sel=229541795'
		webbrowser.open(url)

	













	elif cmd == 'programs':
		play(song_odnu_minutku)


	elif cmd == 'timer':
		time_timer.timerr()

	elif cmd == 'weather':
		play(song_odnu_minutku_1)
		parser_weather.weather_parse()





		




	



























	





















	elif cmd == 'github':
		# открыть гитхаб
		play(song_odnu_minutku)
		url = 'https://github.com/'
		webbrowser.open(url)
	


	if cmd == 'photoshop':
		play(song_odnu_minutku)
		os.startfile('C:\\Program Files\\Adobe\\Adobe Photoshop CS6 (x64)\\Photoshop.exe')
	
	if cmd == 'off':
		computer_off.off()


	









	
 
# запуск
	
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)
 
with m as source:
	r.adjust_for_ambient_noise(source)
 
speak_engine = pyttsx3.init()

stop_listening = r.listen_in_background(m, callback)
root.mainloop()
while(True):
	time.sleep(0.1)
while(True):
	execute_cmd()
	



