#!/usr/bin/python3
"""Define a class square"""

class Square():
    """The class being defined"""

    def __init__(self, size=0):
        """Initializing the class

        Args:
            size: The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0"
        self.__size = size
