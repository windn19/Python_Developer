import requests  # подключение библиотеки для выполнения запросов
import json # подключение библиотеки для чтения формата json

url = 'https://www.cbr-xml-daily.ru/daily_json.js' # адрес, куда отправляются запросы
response = requests.get(url=url) # отправка запроса и запись ответа в переменную.
data = json.loads(response.text) # чтение ответа от страницы, как текста, и запись в результата в переменную
print(data) # вывод ответа от страницы на консоль
# вывод названия определенной валюты и его курса
print(f"Курс {data['Valute']['SGD']['Name']} - {data['Valute']['SGD']['Value']}")

