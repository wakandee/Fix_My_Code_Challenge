#!/usr/bin/python3

class Square:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        """ Return the area of the square """
        if self.width <= 0 or self.height <= 0:
            return 0
        return self.width * self.height

    def perimeter(self):
        """ Return the perimeter of the square """
        if self.width <= 0 or self.height <= 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)  # Should output: 12/9
    print(s.area())  # Should output: 108
    print(s.perimeter())  # Should output: 42
