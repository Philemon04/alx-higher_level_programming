#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            divde = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divde = 0
        except ZeroDivisionError:
            print("division by 0")
            divde = 0
        except IndexError:
            print("out of range")
            divde = 0
        finally:
            new_list.append(divde)
    return (new_list)
