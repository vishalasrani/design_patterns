class Car:
    def __init__(self):
        self.name = None
        self.body = None
        self.engine = None
        self.wheels = None

    def set_name(self, name):
        self.name = name

    def set_body(self, body):
        self.body = body

    def set_engine(self, engine):
        self.engine = engine

    def set_wheels(self, wheels):
        self.wheels = wheels

    def specifications(self):
        print("---------------------------------------------")
        print(f" Name: {self.name} \n body: {self.body.shape} \n engine: {self.engine.hoursepower} \n wheels: {self.wheels.size}")
        print("---------------------------------------------")
