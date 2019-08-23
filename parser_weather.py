import requests
from bs4 import BeautifulSoup 


base_url = 'https://yandex.by/search/?text=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0%20%D0%B2%20%D0%B3%D0%BE%D0%BC%D0%B5%D0%BB%D0%B5&clid=2186621&rdrnd=775817&lr=155&redircnt=1563653679.1'

def weather_parse(base_url):
	session = requests.Session()	
	request = session.get(base_url)
	soup = BeautifulSoup(request.content, 'html.parser')
	divs_1 = soup.find_all('div', class_='main__center')

	for div in divs_1:
		temperature = div.find('div', class_='weather-forecast__current-temp').text
		wind_numb = div.find('div', class_='weather-forecast__desc-value').text
		wind_title = div.find('div', class_='weather-forecast__desc-title').text
		weather = div.find('span', class_='text-cut2 typo typo_text_m typo_line_m').text
		
	a = 'Сейчас: ' + weather +", "+ wind_title +" "+ wind_numb 


	print(a)


	#print(divs)
weather_parse(base_url)
