from random import randint


class A:

    def __init__(self):
        self.x = randint(0, 100)
        self.y = randint(0, 100)

    def go(self):
        return self.x*self.y

    def __str__(self):
        return f'Опеределены точки: {self.x} , {self.y}'


class B:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def go(self):
        return (self.x*self.y)**(1/2)

    def __str__(self):
        return f'Точка {self.x, self.y}'


b = B(3, 4)
a = A()

print(b)
print(a)
print(b.go())
print(a.go())
