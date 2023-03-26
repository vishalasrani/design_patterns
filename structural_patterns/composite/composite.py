from abc import ABCMeta, ABC, abstractmethod


class IProduct(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        """ Implemented in child class """

    @staticmethod
    @abstractmethod
    def print_price(self):
        """ Implemented in child class """


class Product(IProduct):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_price(self):
        print("Product Name: %s, Price: %s" % (self.name, self.price))


class Box(IProduct):

    def __init__(self, type, price):
        self.type = type
        self.price = price
        self.base_price = price
        self.products = []

    def add(self, product):
        self.products.append(product)
        self.price += product.price

    def print_price(self):
        print("Box Type: %s, Packaging Charges: %s" % (self.type, self.base_price))
        for product in self.products:
            product.print_price()
        print("Total Price of Box %s is %s" % (self.type, self.price))


if __name__ == "__main__":
    p1 = Product("MAC", 100)
    p2 = Product("Linux", 80)
    b1 = Box("B1", 10)
    b2 = Box("B2", 20)
    b3 = Box("B3", 10)
    b4 = Box("B4", 10)
    b1.add(p1)
    b3.add(p1)
    b4.add(p2)
    b2.add(b3)
    b2.add(b4)
    print("**************")
    p1.print_price()
    print("**************")
    p2.print_price()
    print("**************")
    b1.print_price()
    print("**************")
    b2.print_price()
    print("**************")
    b3.print_price()
    print("**************")
    b4.print_price()
    print("**************")