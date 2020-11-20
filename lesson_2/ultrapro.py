"""
Написать программу “Угадай число”. Программа должна с помощью наводящих вопросов отгадать число.
"""

from random import randint

print('Загадайте число от 1 до 100:')
start = 1
end = 100
while True:
    n = randint(1, 101)
    s = input(f'{n}=')
    while s not in 'nNДднНyY':
        s = input(f'{n}=')
    while s not in 'ДдyY':
        s1 = input(f'{n}>')
        while s1 not in 'nNДднНyY':
            s1 = input(f'{n}>')
        if s1 in 'ДдyY':
            start = n
        else:
            end = n
    else:
        break
print(n)