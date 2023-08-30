#!/usr/bin/python3
"""Adding a variable to class Square: """
class Square:
    """Initialize Square with size"""
    def __init__(self, size=0):
        """private variable instance size"""
        try:
            type(size) = int
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
