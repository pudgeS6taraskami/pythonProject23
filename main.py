# 5.1
# 1 Задание
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# 2 Задание
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x_shift, y_shift):
        self.x += x_shift
        self.y += y_shift

    def length(self, point):
        return round(((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5, 2)
# 3 Задание
class RedButton:
    def __init__(self):
        self.counter = 0

    def click(self):
        print("Тревога!")
        self.counter += 1

    def count(self):
        return self.counter
# 4 Задание
class Programmer:
    def init(self, name, position):
        self.name = name
        self.position = position
        self.hoursworked = 0
        if position == 'Junior':
            self.salaryperhour = 10
        elif position == 'Middle':
            self.salaryperhour = 15
        elif position == 'Senior':
            self.salaryperhour = 20
            self.promotions = 0
        else:
            raise ValueError("Invalid position")

    def work(self, time):
        self.hoursworked += time

    def rise(self):
        if self.position == 'Junior':
            self.position = 'Middle'
            self.salaryperhour = 15
        elif self.position == 'Middle':
            self.position = 'Senior'
            self.salaryperhour = 20
            self.promotions = 0
        elif self.position == 'Senior':
            self.promotions += 1
            self.salaryperhour += 1

    def info(self):
        salary = self.hoursworked * self.salaryperhour
        if self.position == 'Senior':
            salary += self.promotions * 1000
        return f'{self.name} {self.hoursworked}ч. {salary}тгр.'
# 5 Задание
import math

class Rectangle:
    def __init__(self, point1, point2):
        self.x_min = min(point1.x, point2.x)
        self.x_max = max(point1.x, point2.x)
        self.y_min = min(point1.y, point2.y)
        self.y_max = max(point1.y, point2.y)

    def width(self):
        return self.x_max - self.x_min

    def height(self):
        return self.y_max - self.y_min

    def perimeter(self):
        return round(2 * (self.width() + self.height()), 2)

    def area(self):
        return round(self.width() * self.height(), 2)

    def __str__(self):
        return "(({:.1f}, {:.1f}), ({:.1f}, {:.1f}))".format(self.x_min, self.y_min, self.x_max, self.y_max)

    def __repr__(self):
        return "Rectangle({}, {})".format(repr(Point(self.x_min, self.y_min)), repr(Point(self.x_max, self.y_max)))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)


# проверка работы классов
p1 = Point(3.2, -4.3)
p2 = Point(7.52, 3.14)

rect = Rectangle(p1, p2)
print(rect.perimeter())
print(rect.area())

p1 = Point(7.52, -4.3)
p2 = Point(3.2, 3.14)

rect = Rectangle(p1, p2)
print(rect.perimeter())
print(rect.area())
# 6 Задание
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_pos(self):
        return (self.x, self.y)

    def get_size(self):
        return (self.width, self.height)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def resize(self, width, height):
        self.width = width
        self.height = height
# 7 Задание
import math

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_pos(self):
        return (self.x, self.y)

    def get_size(self):
        return (self.width, self.height)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def resize(self, width, height):
        self.width = width
        self.height = height

    def turn(self):
        cx = self.x + self.width / 2
        cy = self.y + self.height / 2
        dx = self.width / 2
        dy = self.height / 2

        x1 = self.x - cx
        y1 = self.y - cy

        x2 = x1 + dx
        y2 = y1 + dy

        x3 = -y2
        y3 = x2

        x4 = x3 - dx
        y4 = y3 - dy

        self.x = round(cx + x4)
        self.y = round(cy + y4)

    def scale(self, factor):
        cx = self.x + self.width / 2
        cy = self.y + self.height / 2

        w = round(self.width * factor, 2)
        h = round(self.height * factor, 2)

        x = round(cx - w / 2)
        y = round(cy - h / 2)

        self.x = x
        self.y = y
        self.width = w
        self.height = h



