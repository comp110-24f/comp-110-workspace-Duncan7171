"""Challenge question 3"""

__author__ = "730745874"


def num_instances(phrase: str, search_char: str) -> int:
    """Defining num_instances with 2 inputs that
    are both strings, it will return an integer"""
    count: int = 0
    # Here we are creating the local variable called count
    # This cariabel will start at 0 and go up when a the letter is detected in word
    index: int = 0
    # This is out index, we need it so we can tell the our code to stop when word done
    while index < len(phrase):
        # Telling code to run as long as index is less than the length of the phrase
        if search_char == phrase[index]:
            # If statement for asking if the letter is equal to each letter in the word.
            count += 1
            # If the letter is found this will ass one to count
        index += 1
        #  no matter what the index increases by one after each letter
    return count
    # This is our return statement telling us to return count
