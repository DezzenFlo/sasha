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
# слова Саши
song_da            = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\Новая папка (2)\\Голос Саши\\Да.wav')
song_ay_ne_ponayla = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\Новая папка (2)\\Голос Саши\\Я вас не поняла.wav')
song_govorite      = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\Новая папка (2)\\Голос Саши\\Говорите.wav')
song_odnu_minutku  = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\Новая папка (2)\\Голос Саши\\Одну минутку.wav')
song_net           = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\Новая папка (2)\\Голос Саши\\Нет.wav')
song_vi_skazali    = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\Новая папка (2)\\Голос Саши\\Вы сказали.wav')
song_net_ne_mogu   = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\Новая папка (2)\\Голос Саши\\Нет не могу.wav')
song_nu_poprobuy   = AudioSegment.from_wav('C:\\Users\\Nikita\\Desktop\\Новая папка (2)\\Голос Саши\\Ну попробуй.wav')
# настройки
opts = {
    "alias": ('саша', 'сашуля', 'александра', 'саня', 'санёк', 'санек', 'сашуль', 'саш'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси', 'включи', 'открой', 'создай'),
    "cmds": {
        "ctime"       : ('текущее время', 'сейчас времени', 'который час', 'времени', 'время'),
        "radio"       : ('музыку', 'музыка'),
        "stupid1"     : ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты'),
        "youtube"     : ('ютуб', 'видео', 'любое видео', 'youtube'),
        "vk"          : ('вк', 'в контакте', 'вконтакте'),
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
        "aliexpress"  : ('алиэкспрес', 'алиэкспресс' 'алиекспрес', 'алиекспрэс', 'алиэкспрэс', 'али', 'ali', 'aliexpress', 'дом китайцев'),
        "repit"       : ('повтори за мной', 'повтори за мною', 'повтори', 'повторяй', 'повторяй за мной'),
        "off":('выключи','выключи компьютер','офни','офни пк','пк на минус','оф')
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
		print("[***] Распознано: " + voice)

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
		

		
		elif voice.startswith(opts["tbr"]):
			cmd = voice
			for x in opts['tbr']:
				cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
			cmd = recognize_cmd(cmd)
			execute_cmd(cmd['cmd'])
 
	except sr.UnknownValueError:
		print("[$#$] Голос не распознан!")
	except sr.RequestError as e:
		print("[$#$] Неизвестная ошибка, проверьте интернет!")
 
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
		now = datetime.datetime.now()
		print("[***] Сейчас " + str(now.hour) + ":" + str(now.minute))
		speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
		
	if cmd == 'radio':
		# воспроизвести радио
		play(song_odnu_minutku)
		os.system("C:\\Users\\Nikita\\Desktop\\fall_out_boy_-_immortals.mp3")

	elif cmd == 'stupid1':
		# рассказать анекдот
		speak("[***] Мой разработчик не научил меня анекдотам ... Ха ха ха")
	
	elif cmd == 'youtube':
		play(song_odnu_minutku)
		url = 'https://www.youtube.com'
		webbrowser.open(url)

	elif cmd == 'vk':
		play(song_odnu_minutku)
		url = 'https://vk.com/feed'
		webbrowser.open(url)

	elif cmd == 'serials':
		play(song_odnu_minutku)
		url = 'http://fanserials.tv'
		webbrowser.open(url)
	
	elif cmd == 'kino':
		play(song_odnu_minutku)
		url = 'https://kinogo.by'
		webbrowser.open(url)
	
	elif cmd == 'elctroshop':
		play(song_odnu_minutku)
		url = 'https://www.777555.by'
		webbrowser.open(url)
	
	elif cmd == 'aliexpress':
		play(song_odnu_minutku)
		url = 'https://ru.aliexpress.com/?src=yandex&albch=search&acnt=7443951&isdl=y&aff_short_key=UneMJZVf&yclid=4096793462919695618'
		webbrowser.open(url)
	elif cmd == '':
		play(song_odnu_minutku)
		url = ''
		webbrowser.open(url)
	elif cmd == '':
		play(song_odnu_minutku)
		url = ''
		webbrowser.open(url)
	if cmd == 'photoshop':
		play(song_odnu_minutku)
		os.system("C:\\Program Files\\Adobe\\Adobe Photoshop CS6 (x64)\\Photoshop.exe")
	if cmd == 'off':
		os.system('shutdown -s')

	if cmd == 'repit':
		play(song_govorite)
		r = sr.Recognizer()
		with sr.Microphone() as source:
			#r.pause_threshold = 1
			r.adjust_for_ambient_noise(source, duration = 2)
			audio = r.listen(source)
		try:

			zadanie = r.recognize_google(audio, language="ru-RU").lower()
			speak('Вы сказали: ' + zadanie)

		except sr.UnknownValueError:
			play(song_ay_ne_ponayla)
			zadanie = command()
		return zadanie



	else:
		print('[$#$] Команда не распознана, повторите!')
 
# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)
 
with m as source:
    r.adjust_for_ambient_noise(source)
 
speak_engine = pyttsx3.init()

stop_listening = r.listen_in_background(m, callback)
while(True):
	time.sleep(0.1)
while(True):
	execute_cmd()
	
