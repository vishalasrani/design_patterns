from structural_patterns.bridge.color import Red, Blue
from structural_patterns.bridge.shape import Circle, Square


if __name__ == "__main__":
    red = Red()
    blue = Blue()

    print("*******************")
    red_circle = Circle(red)
    red_circle.display()
    red_circle.print_color()
    print("*******************")
    print("*******************")
    blue_square = Square(blue)
    blue_square.display()
    blue_square.print_color()
    print("*******************")
