from time import time


def check_time(f):
    def wrapper():
        t = time()
        f()
        print(f'Время выполнения функции {round(time() - t, 2)} сек')
    return wrapper


@check_time
def spisok():
    result =[]
    for x in range(1000000):
        result.append(x)
    return result


@check_time
def sp_gen():
    return (x for x in range(1000000))


spisok()
sp_gen()
