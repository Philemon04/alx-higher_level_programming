#!/usr/bin/python3
""" A class that defines a square by its size"""

class Square:
    """ Method to initialize the square object"""
    def __init__(self, size=0):
        try:
            type(size) = int
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
         """ Method that returns the square area of the object"""
        return(self.__size * self.__size)
