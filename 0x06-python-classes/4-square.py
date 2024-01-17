#!/usr/bin/python3

"""Define a class square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initiate a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

        @property
        def size(self):
            """Get/set current size of square."""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__self = value

        def area(self):
            """Return the current area of square."""
            return (self.__size * self.__size)
