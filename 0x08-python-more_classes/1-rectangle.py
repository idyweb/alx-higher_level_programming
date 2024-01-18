#!/usr/bin/python3

"""Define a Rectangle class."""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of rectantgle.
            height (int): The height of rectangle.
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method: checks height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method: checks width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
