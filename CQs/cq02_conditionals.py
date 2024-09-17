"""Challenge Question 2"""

__author__ = "730745874"


def guess_a_number() -> None:
    """Here we are defining a guess_a_number and saying tht it will take no
    inputs and have no return"""
    secret: int = 7
    # We create a local variabel called secret and say its an int = to 7
    x: str = input("Guess a number: ")
    # here we are creating a local variable x its a str with the input of guess a number
    print("Your guess was " + str(x))
    # printing your guess was plus the inputed x by user
    if int(x) == secret:
        # This the if statement looking for if the guess was the correct number
        print("You got it!")
        # Print statment for line above
    elif int(x) < 7:
        # this is the elif statement looking if the number is above 7
        print("Your guess was too low! The secret number is " + str(secret))
        # This is the above print statement and then printing secret number
    else:
        print("Your guess was too high! The secret number is " + str(secret))
        # If there is any other input not defined above then this statment is printed
    return None


if __name__ == "__main__":
    guess_a_number()
    # This is calling the function
