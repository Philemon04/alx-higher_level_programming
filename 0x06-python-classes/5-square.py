#!/usr/bin/python3
class Square:
    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        try:
            type(value) = int
        except TypeError:
            print("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return(self.__size * self.__size)

    def my_print(self):
        if size = 0:
            print("")
        for i in range(0, self.__size):
            [print("#:", end="") for j in range(self.__size)]
            print("")
