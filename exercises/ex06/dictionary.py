"""Dictionaries!!"""

__author__ = "730745874"


def invert(origional_dict: dict[str, str]) -> dict[str, str]:
    """Funciton to switch the keys and the values of a dictionary"""
    inverted_dict = {}
    # Making an empty dict to store the dict of inverted values
    for key in origional_dict:
        value = origional_dict[key]
        # doing this so we can look through values associated with each key
        if value in inverted_dict:
            raise KeyError
            # Raising an error if two keys equal each other in new list
        else:
            inverted_dict[value] = key
            # Swithching the keys and the values
    return inverted_dict


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Looking through a dict of colors and looking for the most popular one"""
    color_count = {}
    # Making an empty dict to store colors as keys and frequency as values
    for color in names_and_colors:
        if names_and_colors[color] not in color_count:
            color_count[names_and_colors[color]] = 0
            # Adding a value to color_count dict if not already there
        else:
            color_count[names_and_colors[color]] += 1
            # adding one for a color added in the dictionary
    most_repeated_color = ""
    # making an empty string that will be filled by most used color
    max = 0
    # Highest color count is 0 to begin
    for color in color_count:
        if color_count[color] > max:
            most_repeated_color = color
            # setting this color to most_repeated_color
            max = color_count[color]
            # setting max to the number of times the color appears, so the code knows
            # only to replace most_repeated_color if it appears more than max
    return most_repeated_color


def count(imput: list[str]) -> dict[str, int]:
    """Taking a list and turning it into dict with key being a unique value
    given in the list and the value is the number ot times it appears."""
    new_dict: dict[str, int] = {}  # Creating an empty dict to store values
    for item in imput:
        if item in new_dict:
            # entering it the item is already in the new dict
            new_dict[item] += 1
            # adding to count for an item in list
        else:
            new_dict[item] = 1
            # if item not already in dict make it equal to 1
    return new_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Alphabetizing a list"""
    alphabetized_dict: dict[str, list[str]] = (
        {}
    )  # Making an empty dict to hold alphabetzed list
    for word in words:
        lower_case_first_letter = word[0].lower()
        # making the first letter of each word in list lower case
        if lower_case_first_letter not in alphabetized_dict:
            # entering if the letter is not already in alphabetized list
            alphabetized_dict[lower_case_first_letter] = []
            # if letter not already in dict, add it and a cooresponding empty list
        alphabetized_dict[lower_case_first_letter].append(word)
        # appending the word to the list to its corresponding letter
    return alphabetized_dict


def update_attendance(
    attendance_count: dict[str, list[str]], day: str, student: str
) -> None:
    """A function to mutate attendance of names and days of attendance"""
    if day in attendance_count:
        # If the day is already there add the name of student to the list
        if student not in attendance_count[day]:
            attendance_count[day].append(student)
        # If the name is already with the day do not add name again

    else:
        attendance_count[day] = [student]
        # If the day is not already there, make a new entry with student in list
