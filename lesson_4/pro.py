from datetime import datetime

with open('log1', mode='r', encoding='utf-8') as file:
    last_date = 0
    for line in file:
        if not last_date:
            last_date = datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S,%f')
            continue
        date = datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S,%f')
        if date > last_date:
            last_date = date
print(last_date)
