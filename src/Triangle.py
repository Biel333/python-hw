from Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.P = round(a+b+c, 2)
        self.p = (a + b + c) / 2
        self.S = round(math.sqrt(self.p * (self.p - a) * (self.p - b) * (self.p - c)), 2)
        super().__init__("Треугольник", self.P, self.S)
