from creational_patterns.builder.car_builder import CarBuilder
from creational_patterns.builder.car_parts import Body, Engine, Wheels


class TataBuilder(CarBuilder):
    def __init__(self):
        super().__init__()

    def add_name(self):
        self.car.set_name("Tata")
        return

    def add_body(self):
        body = Body("Sedan")
        self.car.set_body(body)
        return

    def add_engine(self):
        engine = Engine("400")
        self.car.set_engine(engine)
        return

    def add_wheels(self):
        wheels = Wheels("Type 1")
        self.car.set_wheels(wheels)
        return

    def build(self):
        return self.car
