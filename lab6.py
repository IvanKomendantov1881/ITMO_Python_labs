class Figura:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self, a, b, c):
        V = a * b * c
        print('Объём:', V)

    def __str__(self):
        print(f'Высота: {self.a}, длина: {self.b}, ширина: {self.c}')

    def __add__(self, other):
        if isinstance(other, Figura):
            total_volume = self.volume() + other.volume()
            return total_volume
        else:
            raise TypeError("Можно складывать только объекты класса Figura")


class DepthFigure(Figura):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d
        self.figures = []

    def volume(self):
        first_figure = super().volume()
        second_figure = (self.a - self.d) * (self.b - self.d) * (self.c - self.d)
        third_figure = first_figure - second_figure
        return third_figure

    def totalvolume(self):
        return sum(fig.volume() for fig in self.figures)

    def __str__(self):
        return f'Стороны тела с внутренней полостью: a={self.a}, b={self.b}, c={self.c}, d={self.d}'


# Тестирование
if __name__ == "__main__":
    fig1 = Figura(2, 3, 4)
    fig2 = Figura(1, 2, 3)

    print("Фигура 1:", fig1)
    print("Объем фигуры 1:", fig1.volume())
    print("Фигура 2:", fig2)
    print("Объем фигуры 2:", fig2.volume())
    print("Сумма объемов:", fig1 + fig2)

    print("\n" + "=" * 50)

    depth_fig = DepthFigure(10, 10, 10, 2)
    print(depth_fig)
    print("Объем тела с полостью:", depth_fig.volume())

    depth_fig.figures.append(Figura(2, 2, 2))
    depth_fig.figures.append(Figura(3, 3, 3))
    depth_fig.figures.append(Figura(1, 1, 1))

    print(f"Количество фигур в массиве: {len(depth_fig.figures)}")
    print("Суммарный объем всех фигур в массиве:", depth_fig.totalvolume())
    raise TypeError("Можно складывать только объекты класса Figure")


class DepthFigure(Figura):
    def __int__(self, d):
        self.d = d

    def volume(self, a, b, c):
        first_figure = super().volume(a,b,c)
        second_figure = (self.a - self.d) * (self.b - self.d) * (self.c - self.d)
        third_figure = first_figure - second_figure
        print('Объем тела с внутренней вполостью:', third_figure)

    def __str__(self):
        print(f'Стороны тела с внутренней вполостью: a={self.a}, b={self.b}, c={self.c}, d={self.d}')
