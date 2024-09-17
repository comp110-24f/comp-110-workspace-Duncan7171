"""Practicing my conditionals"""

# def less_than_10(num: int) -> None:
"""Tell us if num <10"""
# if num < 10:  # check if this is true
# print("Small number!")  # Then Block
# else:
# print("Big number!")
# print("This is the end of the function")
# return None


# def wake_up(alarm: bool) -> str:
"""Return a message based on if alarm is going off."""
# if alarm is True:
# return "Wake up! Go to Comp 110!"
# else:
# return "Keep sleeping. You deserve it. :)"


# print(wake_up(alarm=False))


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
