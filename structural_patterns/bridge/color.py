from abc import ABC, abstractmethod


class Color(ABC):

    @abstractmethod
    def get_color(self):
        pass


class Red(Color):

    def get_color(self):
        print("Color Red")


class Blue(Color):

    def get_color(self):
        print("Color Blue")
