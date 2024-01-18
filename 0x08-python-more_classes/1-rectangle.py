#!/usr/bin/python3

"""Define a Rectangle class."""


class Rectangle:
    """Represents a rectangle"""

    def __init___(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of rectantgle.
            height (int): The heght of rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getting the current size of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
