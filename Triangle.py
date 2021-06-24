import math
class Triangle():

    a = 0
    b = 0
    c = 0

    def __init__(self, side1, side2, side3):
        self.a = side1
        self.b = side2
        self.c = side3
    
    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def scale(self, num):
        return Triangle(self.a * num, self.b * num, self.c * num)
    
    def is_valid(self):
        return self.a + self.b > self.c
    
    def is_right(self):
        return (self.a**2 + self.b**2 == self.c**2)