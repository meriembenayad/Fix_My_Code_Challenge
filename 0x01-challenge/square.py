#!/usr/bin/python3
"""Class Square."""


class Square():
    """Modules square."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Loop through the keyword arguments
        and set the corresponding attribute
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the Square."""
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Permiter of the Square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Returns a string representation of the square.
        The format is "width/height".
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
