#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in sortes(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
