"""Challenge question 3"""

__author__ = "730745874"


def concat(x: str, y: str) -> str:
    """Here we are creating a function called concat"""
    return x + y
    # Returning the combination of x plus y


word1: str = "happy"
# Making a global variable called happy
word2: str = "tuesday"
# Making another global variabke called tuesday


def main() -> None:
    """Here we are creating a main funtion so we can call it later"""
    print(concat(word1, word2))
    return None


if __name__ == "__main__":
    """Making it so we only run full function if its in concatination file"""
    main()
