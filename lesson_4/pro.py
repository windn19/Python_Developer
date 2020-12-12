from datetime import datetime  # подключение библиотеки для обработки даты-времени

with open('log', mode='r', encoding='utf-8') as file:  # открыть файл в режиме чтения и в кодировке utf-8
    last_date = 0  # объявление переменной для последней даты
    for line in file:  # перебрать файл построчно
        if not last_date:  # если последняя дата не равна нулю
            # прочитать первые 23 символа, как дату, по формату
            last_date = datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S,%f')
            continue  # перейти следующюю строку
        # прочитать первые 23 символа, как дату, по формату
        date = datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S,%f')
        if date > last_date:  # если дата больше, чем последняя дата
            last_date = date  # приравнять последнюю дату текущей.
print(last_date)  # вывести последнюю дату.
