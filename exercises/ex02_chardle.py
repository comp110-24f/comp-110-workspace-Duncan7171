"""Making a Tea Party"""

__author__ = "730745874"


def input_word() -> str:
    """Defining input_word, it will have no parameters and it will return a string"""
    start: str = input("Enter a 5-character word: ")
    # I am creating a local variable called start that is a string
    # It will promt the reader to enter a 5 letter word
    if len(start) != 5:
        # If statement saying that if the length is not 5 print statment below
        print("Error: Word must contain 5 characters.")
        exit()
    return start
    # If the user does input a 5 letter word it will simply return start


def input_letter() -> str:
    """Defining input_letter, no parameters and will return a string"""
    character: str = input("Enter a single character:")
    # Defining local variable of character,it will be a string and input statement above
    if len(character) != 1:
        # If length of the input is not one letter then it will print statement below
        print("Error: Character must be a single character.")
        exit()
    return character
    # If the user does input a 1 letter it will simply return start


def contains_char(word: str, letter: str) -> None:
    """Here we are defining contains_char it will have 2
    inputs both being a str, it will return none"""
    print("Searching for " + letter + " in " + word)
    # This is the starting statement that is printed
    number: int = 0
    # This is a local variable used later on to count letters found in word
    if word[0] == letter:
        # This is looking at the first character in the inputted word
        print(letter + " found at index 0")
        number += 1
        # Will print statment and add one to number of times letter is found in word
    if word[1] == letter:
        # This is looking at the second character in the inputted word
        print(letter + " found at index 1")
        number += 1
        # Same funtionalty as code in previous if statement
    if word[2] == letter:
        # This is looking at the third character in the inputted word
        print(letter + " found at index 2")
        number += 1
        # Same funtionalty as code in previous if statement
    if word[3] == letter:
        # This is looking at the fourth character in the inputted word
        print(letter + " found at index 3")
        number += 1
        # Same funtionalty as code in previous if statement
    if word[4] == letter:
        # This is looking at the fifth character in the inputted word
        print(letter + " found at index 4")
        number += 1
        # Same funtionalty as code in previous if statement
    print(str(number) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Here we are creating a main function for our code to run through"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    """Here we are actually calling the code"""
    main()
