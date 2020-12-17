from psutil import Process  # импорт из библиотеки psutil класса для получения значений занятой памяти процесса
from os import getpid  # импорт из библиотеки os метода для получения идентификатора текущего процесса


def memory_func(func):
    """
    декоратор для замера памяти занимаемой функцией в оперативной памяти.
    """
    def wrapper(*args, **kwargs):
        proc = Process(getpid())  # получение идентификатора текущего процесса и объявление класса
        start_memory = proc.memory_info().rss  # сохранение начального значения занятой памяти
        result = func(*args, **kwargs)  # выполнение функции с параметрами
        end_memory = proc.memory_info().rss  # замер объема занятой памяти после выполнения функции
        print(f"Физ. память используемая функцией {func.__name__}: {end_memory-start_memory} байт")  # вывод результата
        return result
    return wrapper


@memory_func   # вызов декоратора для определения занимаемой функцией памяти
def spisok(n):
    """
       Функция создания списка числ на 1000000 элементов
       """
    result = []  # объявление результирующего списка
    for x in range(n):  # для каждого из чисел от 0 до 999999 делай
        result.append(x)  # добавление в результирующий список очередного элемента
    return result


@memory_func
def sp_gen(n):
    """
       Функция создания псевдогенератора
    """
    for i in range(n):
        yield i


spisok(10000000)  # вызов декорируемых функций
sp_gen(10000000)
