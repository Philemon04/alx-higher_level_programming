#!/usr/bin/python3
"""Adding a variable to class Square: """
class Square:
    """Initialize Square with size"""
    def __init__(self, size=0):
        """private variable instance size"""
        try:
        """private variable instance size"""
            type(size) = int
        except TypeError:
        """private variable instance size"""
            print("size must be an integer")
        if size < 0:
        """private variable instance size"""
            raise ValueError("size must be >= 0")
        self.__size = size
