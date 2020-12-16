import psutil
import os


def memory_func(func):
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        start_memory = proc.memory_info().rss
        result = func(*args, **kwargs)
        end_memory = proc.memory_info().rss
        print(f"Физ. память используемая функцией {func.__name__}: {end_memory-start_memory} байт")
        return result
    return wrapper


@memory_func
def spisok(n):
    result =[]
    for x in range(n):
        result.append(x)
    return result


@memory_func
def sp_gen(n):
    for i in range(n):
        yield i


spisok(10000000)
sp_gen(10000000)
