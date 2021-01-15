class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Точка с координатами ({self.x}, {self.y})'

    def __len__(self):
        return int((self.x**2+self.y**2)**.5)

    def __add__(self, other):
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, int) or isinstance(other, float):
            self.x += other
            self.y += other
        return self

    def __sub__(self, other):
        if isinstance(other, Point):
            self.x -= other.x
            self.y -= other.y
        elif isinstance(other, int) or isinstance(other, float):
            self.x -= other
            self.y -= other
        return self

    def __pow__(self, other):
        if isinstance(other, Point):
            self.x **= other.x
            self.y **= other.y
        elif isinstance(other, int) or isinstance(other, float):
            self.x **= other
            self.y **= other
        return self

    def __call__(self, x, y):
        self.x = x
        self.y = y
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(1, 2)
point1 = Point(2, 3)
print(point)
print(len(point))
print(point + 0.37)
print(point + 2)
print(point + point1)
print(point1 - 0.123)
print(point ** 3)
print(point(4, 5))
print(point(4, 3) == point1(5, 4))
print(point1 > point)

