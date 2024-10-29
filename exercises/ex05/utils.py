"""Lists!!"""

__author__ = "730745874"


def only_evens(imput_list: list[int]) -> list:
    """Pulling only the even numbers out of the list"""
    even_numbers = []
    # making an empty list for the even numbers to go in
    for num in imput_list:
        if num % 2 == 0:
            # if the remainder of num/2 is 0 it has to be even
            even_numbers.append(num)
            # Add that number to the list of even numbers
    return even_numbers


def sub(a_list: list[int], beginning: int, end: int) -> list:
    """Taking out a specific piece of the list"""
    sub_list = []
    # Making an empty list to put sub list
    if len(a_list) == 0 or beginning > len(a_list) or end < 0:
        return []
        # If the length is of the list is 0 return an empty list
    if beginning < 0:
        beginning = 0
        # Making it so it will work if beggining is less 0
    if end > len(a_list):
        end = len(a_list)
        # Changing in case end is above the length of list
    for index in range(beginning, end):
        sub_list.append(a_list[index])
        # Adding the numbers from a_list into sub_list that are within range
    return sub_list


def add_at_index(list_1: list[int], new_number: int, number_location: int) -> None:
    """Adding a new number into list"""
    list_1.append(1)
    list_1_copy = []
    # Making a copy list
    for i in list_1:
        list_1_copy.append(i)
    for x in range(number_location + 1, len(list_1)):
        # Shifting all the elements to the right
        list_1[x] = list_1_copy[x - 1]
    list_1[number_location] = new_number
    # Putting new number in the correct index
    if number_location < 0 or number_location > len(list_1):
        raise IndexError("Index is out of bounds for the input list")
        # Throwing an error if number location is out of range
