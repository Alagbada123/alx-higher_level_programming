#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)  # Validate size
        super().__init__(size, size)  # Initialize parent class with width and height
        self.__size = size  # Store size in private attribute

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"

