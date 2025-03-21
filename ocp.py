# Naruszona zasada OCP
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def draw(selfself):
        pass


class Square(Figure):
    def __init__(self, a):
        self.a = a

    def draw(self):
        for side in range(self.a):
            print(self.a * "o ")
        print()


class Triangle(Figure):
    def __init__(self,h):
        self.h = h

    def draw(self):
        for i in range(self.h):
            print(i * "o ")
        print()


class FigureDrawer:
    def draw(self, figure: Figure):
        figure.draw()


square = Square(5)
triangle = Triangle(5)

drawer = FigureDrawer()
drawer.draw(square)
drawer.draw(triangle)