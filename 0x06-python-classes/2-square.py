#!/usr/bin/python3
"""Further defining variable size: """

class Square:
    """Initialize Square with size"""
    def __init__(self, size=0):
        """Check if size is integer"""
        try:
            type(size) = int
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
