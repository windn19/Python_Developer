import csv
import json


car_data = [['brand', 'sup', 'year', 'price'],
            ['Volvo', 1.5, 2017, 2345],
            ['Lada', 0.5, 2018, 5675],
            ['Audi', 2.0, 2018, 9877]]

with open('example.csv', 'w') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(car_data)
print('Writing complete!')

with open('example.csv', mode='r') as f:
    data = csv.DictReader(f, delimiter=';')
    data = list(data)

with open('example.json', mode='w') as f:
    json.dump(data, f)
print('Json done!')
