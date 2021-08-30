from Figure import Figure
import math


class Circle(Figure):
    def __init__(self, a):
        self.a = a
        self.P = round(2*math.pi*a, 2)
        self.S = round(math.pi*(a**2), 2)
        super().__init__("Круг", self.P, self.S)
