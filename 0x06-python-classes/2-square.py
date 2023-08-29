#!/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            type(size) = int
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size