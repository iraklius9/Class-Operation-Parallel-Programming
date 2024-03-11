import concurrent.futures
import time


class Trapezoid:  # noqa
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def __str__(self):
        return f"Trapezoid: Base1={self.base1}, Base2={self.base2}, Height={self.height}"

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __mod__(self, other):
        return self.area() / other.area()


class Rectangle(Trapezoid):
    def __init__(self, width, height):
        super().__init__(width, width, height)

    def __str__(self):
        return f"Rectangle: Width={self.base1}, Height={self.height}"

    def area(self):
        return self.base1 * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square: Side={self.base1}"

    def area(self):
        return self.base1 ** 2


def calculate_area(shape):
    print(f"Area of {shape}: {shape.area()}")


def main():
    shapes = [] # noqa
    for _ in range(100):
        choice = random.choice(Digit_list)
        shape = Trapezoid(*choice)
        shapes.append(shape)

    rectangle = Rectangle(4, 5)
    square = Square(4)
    shapes.extend([rectangle, square])

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(calculate_area, shapes)

    end_time = time.time()
    print("Total time taken:", end_time - start_time, "seconds")


if __name__ == "__main__":
    import random

    Digit_list = [[random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)] for i in range(10)]
    main()

    # Total time taken: 0.01700139045715332 seconds
