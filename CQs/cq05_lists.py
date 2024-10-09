"""Mutating functions."""

__author__ = "730745874"


def manual_append(x: list[int], y: int) -> None:
    """Making the function manual append with parmeters above"""
    x.append(y)
    # Makeing it so we can add int to list


def double(z: list[int]) -> None:
    """Creating a double function to double each aspect of list"""
    index: int = 0
    while index < len(z):
        z[index] *= 2
        # Going through and doubling each number in list
        index += 1


list_1: list[int] = [1, 2, 3]
# Setting list equal to 1,2,3
list_2: list[int] = list_1
# Setting list_2 equal to list_1
double(list_2)
# calling the double function
print(list_1)
print(list_2)
