from creational_patterns.builder.director import Director
from creational_patterns.builder.mercedes_builder import MercedesBuilder
from creational_patterns.builder.tata_builder import TataBuilder


def main():
    tata_builder = TataBuilder()
    tata_director = Director(tata_builder)

    mercedes_builder = MercedesBuilder()
    mercedes_director = Director(mercedes_builder)

    car = tata_director.build_car()
    car.specifications()

    car = mercedes_director.build_car()
    car.specifications()

if __name__ == "__main__":
    main()
