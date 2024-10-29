"""Test CQ"""

__author__ = "730745874"


def find_and_remove_max(input_list: list[int]) -> int:
    """finding and removing biggest funtion"""
    if len(input_list) == 0:
        return -1
    max_number = input_list[0]

    for number in input_list:
        # Finding max number
        if number > max_number:
            max_number = number

    index = len(input_list) - 1
    while index >= 0:
        if max_number == input_list[index]:
            input_list.pop(index)
            # Getting rid of the max number
        index -= 1

    return max_number
