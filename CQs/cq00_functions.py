"""First CQ"""

__author__ = "730745874"


def mimic(message: str) -> str:
    # This is used to simply mimic what is being input
    return message


def main() -> None:
    # this is the begining of the main function, pulls together function
    print(mimic(message=input("What is your message?")))
    # This is here to prompt a user response


if __name__ == "__main__":
    main()
    # This will allow the code to actually run
