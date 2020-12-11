import csv  # подключение библиотеки для работы с csv
import json  # подключение библиотеки для работы с json


car_data = [['brand', 'sup', 'year', 'price'],  # данные для работы
            ['Volvo', 1.5, 2017, 2345],
            ['Lada', 0.5, 2018, 5675],
            ['Audi', 2.0, 2018, 9877]]

with open('example.csv', 'w') as f:  # отрываем файл для работы на запись
    writer = csv.writer(f, delimiter=';')  # объявляем объект для записи и разделитель между данными
    writer.writerows(car_data)  # записываем в файл построчно
print('Writing complete!')

with open('example.csv', mode='r') as f:  # открытие файла для чтения
    data = csv.DictReader(f, delimiter=';')  # объявление объекта для чтения файла как словарь с разделителем ";"
    data = list(data)  # превращение прочитанных данных в словарь.

with open('example.json', mode='w') as f:  # открытия файла для чтения
    json.dump(data, f)  # загрузка данных в открытый файл
print('Json done!')
