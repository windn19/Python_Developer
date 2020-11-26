def square():
    print('Эта функция без параметров')


def cube(x):
    return x ** 3


s = lambda x: x ** 2
print(s(23))
square()
print(cube(54))
