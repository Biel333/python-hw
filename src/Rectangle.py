from Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.P = (a+b)*2
        self.S = a*b
        super().__init__("Прямоугольник", self.P, self.S)
