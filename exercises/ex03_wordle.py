"""Wordle!!!"""

__author__ = "730745874"


def input_guess(secret_word_length: int) -> str:
    """This is where we will make sure the user imputs a guess
    the same lenght as the secret word"""
    user_guess: str = input(f"Enter a {secret_word_length} character word: ")
    # Makeing a local variable for the users guess, and statement telling
    # user what to do
    while len(user_guess) != secret_word_length:
        # Starts a while loop looking at length of guess compared to length
        # of secret word
        user_guess = input(
            f"That wasn't {secret_word_length} chars! Try again: {user_guess}"
        )
        # Prompts user to make guess of correct length.
    return user_guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Goes through each letter of word to find any potentintial mathces
    with input letter"""
    assert len(char_guess) == 1
    # Saying that char_guess must be 1 character
    index: int = 0
    correct_char = False
    # Local vaiables to use in while statement, correct char set to false
    while index < len(secret_word):
        # While loop used to go through each letter of word
        if char_guess == secret_word[index]:
            correct_char = True
            # if the char is in the word correct char changes to True
        index += 1
    return correct_char


def emojified(guess: str, secret: str) -> str:
    """Going through and comparing letters of word and guess
    then returning emojies to tell what letters were correct"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    # Code for a white box emoji
    GREEN_BOX: str = "\U0001F7E9"
    # Code for a green box emoji
    YELLOW_BOX: str = "\U0001F7E8"
    # Code for yellow box emoji
    index: int = 0
    emojis: str = ""
    # This is where we will build out emojis together
    while index < len(guess):
        if guess[index] == secret[index]:
            emojis += GREEN_BOX
            # For correct guesses add green emoji
        elif contains_char(secret_word=secret, char_guess=guess[index]):
            emojis += YELLOW_BOX
            # For incorect guesses, but the character is in word, ad yellow
        else:
            emojis += WHITE_BOX
            # For characters that are not in word at all add white
        index += 1
    return emojis


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    won = False
    while turn < 7 and won is False:
        print(f"== Turn {turn}/6 ==")
        # Printing what turn user is on
        guess = input_guess(secret_word_length=len(secret))
        # Taking in imput guess and setting secret_word_length equal to
        # length of secret
        print(emojified(guess=guess, secret=secret))
        if secret == guess:
            print(f"You won in {turn}/6 turns!")
            won = True
        turn += 1
    if turn >= 7:
        print("X/6 - Sorry, try again tomorrow!")
        # If user goes through all 6 guesses it prints this
        return None


if __name__ == "__main__":
    main(secret="codes")
