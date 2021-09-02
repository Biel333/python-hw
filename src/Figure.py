class Figure:
    def __init__(self, name, P, S):
        self.name = "Фигура: " + name
        self.P = "Периметр: " + str(P)
        self.S = "Площадь: " + str(S)

    @property
    def info(self):
        return self.name, self.S, self.P

    def add_area(self, figure):
        if isinstance(figure, Figure):
            print("ETO FIGURA")
        else:
            raise ValueError("You can create only Figure!")
