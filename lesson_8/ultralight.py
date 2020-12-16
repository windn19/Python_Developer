def describ(f):
    def wapper():
        print('Это начало декоратора')
        print(f())
        print('Это конец декоратора')
    return wapper


@describ
def square():
    return [x**2 for x in range(100)]


@describ
def phrase():
    return 'Кошка хочет гулять'


t = [10, 2, 5]
for i in t:
    s = 'yes' if i < 4 else 'no' if i > 6 else 'else'
    print(i, s)

square()
phrase()