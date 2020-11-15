import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url=url)
data = json.loads(response.text)
print(data)
print(f"Курс {data['Valute']['SGD']['Name']} - {data['Valute']['SGD']['Value']}")

