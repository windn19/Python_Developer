from random import randint
from collections import defaultdict


def random_name(list_name, n=100):
    result = []
    for i in range(n):
        idx = randint(0, len(list_name)-1)
        result.append(list_name[idx])
    return result


def counter_name(list_name):
    result = defaultdict(int)
    for i in list_name:
        result[i] += 1
    result = list(result.items())
    result.sort(key=lambda x: x[1], reverse=True)
    return result[0][0]


def rare_letter(list_name):
    result = defaultdict(int)
    for i in list_name:
        result[i[0]] += 1
    result = list(result.items())
    result.sort(key=lambda x: x[1])
    return result[0][0]


source = ['Иван', "Сергей", "Радмир", "Елена", "Ефим",
     "Дмитрий", "Ирина", "Федор", "Семен", "Кузьма", "Федот", "Анна", "Фёкла"]
list_new = random_name(source)
print(counter_name(list_new))
print(rare_letter(list_new))
