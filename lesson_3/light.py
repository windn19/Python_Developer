from collections import defaultdict  # подключение метода объявления словарей

with open('text.txt', mode='r') as f:  # открытие файла в режиме чтения
    data = f.read()  # чтение файла и передача текста в переменную
s = ''  # объявление переменной

for i in data:  # перебор текста по символам
    if i.isalpha() or i == ' ':  # если символ это буква или пробел
        s += i  # то он добавляется в переменную
    else:
        s += ' '  # иначе добавляется пробел

s = s.split()  # преобразование строки в список путем разделенения по пробелам
s = list(map(lambda x: x.lower(), s))  # перевод каждого элемента списка к строчным символом
d = defaultdict(int)  # объявление словаря со значениями по умолчанию int
for i in s:  # перебор элементов словаря
    d[i] = d[i] + 1  # добавление единицы к каждому слову в списке
d = list(d.items())  # превращение  пар ключ значение в список

d.sort(key=lambda x: x[1], reverse=True)  # сортировка по значениям

for word, amount in d[:5]:  # перебор первых пяти значений
    print(word, ' -- ', amount)  # и вывод их на экран
print(len(d))  # количество пар ключ значение


#  https://www.w3schools.com/python/python_lambda.asp - по лямбде
#  https://pythonworld.ru/moduli/modul-collections.html - по defaultdict
#  https://py-my.ru/post/50b4448ebbddbd5c63000000/index.html - по defaultdict
#   хватит двух? или лучше переписать без них совсем?
