"""Is the word big"""


def word() -> str:
    choice: str = input("What is your word:  ")
    if len(choice) > 7 and len(choice) < 25:
        print("Wow that is a long word")
    elif len(choice) < 7:
        print("That is not a long word")
    else:
        print("There is no way that is a real word")
    return choice


word()
