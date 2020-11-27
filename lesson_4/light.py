from random import randint  # подключение метода генератора целых числ из библиотеки random
from collections import defaultdict  # подключение метода defaultdict из библиотеки collections


def random_name(list_name, n=100):
    """
    нахожение списка случайных имен из списка list_name длиной n
    :param list_name: список имен
    :param n: длина результирующего списка
    :return: список случайных имен
    """
    result = []  # объявление списка для результатов
    for i in range(n):  # перебор значений от 0 до n-1
        idx = randint(0, len(list_name)-1)  # присвоение случайного индекса из индексов списка имен
        result.append(list_name[idx])  # добавление имени в результирущий массив
    return result  # возврат списка случайных имен


def counter_name(list_name):
    """
    Вывод самого часто встречающегося имени
    :param list_name: список имен
    :return: самое частое встречающееся ися
    """
    result = defaultdict(int)  # объявление словаря со целочисленным значением по умолчанию
    for i in list_name:  # перебор всех имен в списке
        result[i] += 1  # добавление по имени в словарь имени и количества
    result = list(result.items())  # перевод пар ключ значение в список
    result.sort(key=lambda x: x[1], reverse=True)  # сортировка его по значениям и с реверсом
    return result[0][0]  # возврат самого часто встречающегося имени


def rare_letter(list_name):
    """
    Функция выбора самой редкой первой буквы
    :param list_name: список имен
    :return: самая редкая буква
    """
    result = defaultdict(int)  # объявление словаря со целочисленным значением по умолчанию
    for i in list_name:  # перебор всех имен в списке
        result[i[0]] += 1  # составление словаря, где ключ первая имя, а значение количество появлений
    result = list(result.items())  # перевод пар ключ значение в список
    result.sort(key=lambda x: x[1])  # сортировка по количеству появлений в списке
    return result[0][0]  # возврат самой редкой буквы


# список имен
source = ['Иван', "Сергей", "Радмир", "Елена", "Ефим",
          "Дмитрий", "Ирина", "Федор", "Семен", "Кузьма", "Федот", "Анна", "Фёкла"]
list_new = random_name(source)  # нахождение списка случайных имен
print(counter_name(list_new))  # вывод самого часто встречающегося имени
print(rare_letter(list_new))  # вывод самой редкой первой буквы имени
