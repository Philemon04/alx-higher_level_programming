#!/usr/bin/python3
"""Further defining variable size: """

class Square:
    """Initialize Square with size = 0"""
    def __init__(self, size=0):
        """Check if size is integer and is greater than 0"""
        try:
            type(size) = int
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
