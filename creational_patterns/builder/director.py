class Director:
    def __init__(self, car_builder):
        self.car_builder = car_builder

    def build_car(self):
        self.car_builder.add_name()
        self.car_builder.add_body()
        self.car_builder.add_engine()
        self.car_builder.add_wheels()
        return self.car_builder.build()
