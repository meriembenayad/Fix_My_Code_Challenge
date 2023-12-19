#!/usr/bin/python3
"""Class Square"""


class Square():
    """ Modules square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
            Loop through the keyword arguments
            and set the corresponding attribute
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def AreaOfMySquare(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Permiter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Returns a string representation of the square.
        The format is "width/height".
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=9, height=9)
    print(s)
    print(s.AreaOfMySquare())
    print(s.PermiterOfMySquare())
