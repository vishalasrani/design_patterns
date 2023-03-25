from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def display(self):
        pass

    def print_color(self):
        self.color.get_color()


class Circle(Shape):
    def display(self):
        print("Circle")


class Square(Shape):
    def display(self):
        print("Square")



