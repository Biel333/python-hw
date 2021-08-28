from Figure import Figure


class Square(Figure):

    def __init__(self, a):
        self.a = a
        self.P = a*4
        self.S = a**2
        super().__init__("Квадрат", self.P, self.S)
