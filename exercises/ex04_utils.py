"""Fun with Lists"""

__author__ = "730745874"


def all(list_1: list[int], num: int) -> bool:
    """Signature for function looking to see if the list is composed entirely
    of the number inputed"""
    index: int = 0
    if len(list_1) == 0:
        return False
    while index < len(list_1):
        if list_1[index] != num:
            return False
            # If at any point the number doesnt equal number in, make false
        index += 1
    return True
    # If the funtion goes through and all number are same, make true


def max(list_2: list[int]) -> int:
    """Going through to see what the biggest number in the list is"""
    if len(list_2) == 0:
        raise ValueError("max() arg is an empty List")
        # If the lists doesnt have any values return an error
    index = 1
    largest_value = list_2[0]
    # Looking at the largest value in list
    while index < len(list_2):
        if list_2[index] > largest_value:
            largest_value = list_2[index]
            # If number found is bigger than the largest, make that new largest
        index += 1
    return largest_value


def is_equal(list_3: list[int], list_4: list[int]) -> bool:
    """Looking to see if two lists are equal"""
    if len(list_3) != len(list_4):
        return False
        # If the two functions are different lenghts they can't be equal
    index = 0
    while index < len(list_3):
        # Looking at while the index it greater than length of list 3
        if list_3[index] != list_4[index]:
            return False
            # If at any point a number doesn't equal the corresponding number
            # Return false because they are nor equal
        index += 1
    return True


def extend(list_5: list[int], list_6: list[int]) -> None:
    """Extending list 5 with numbers from list 6"""
    index = 0
    while index < len(list_6):
        list_5.append(list_6[index])
        # Adding each value from list 6 to list 5
        index += 1
    return None
