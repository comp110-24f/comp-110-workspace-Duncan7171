"""Making a Tea Party"""

__author__ = "730745874"


def main_planner(guests: int) -> None:
    """Entry point of my code"""
    print("A Cozy Tea Party For " + str(guests) + " People")
    """Print start phrase"""
    print("Tea Bags: " + str(tea_bags(guests)))
    """Print amount of tea bags"""
    print("Treats: " + str(treats(guests)))
    """Print number of treats"""
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    """Print total cost of party"""
    return None


def tea_bags(people: int) -> int:
    """This is to simply say that people will be a number"""
    return people * 2
    """This tells us to multiply the number of people by 
    2 since each person needs 2 teabags"""


def treats(people: int) -> int:
    """Saying treats wil depend on people and it will retun an int"""
    return int((tea_bags(people=people) * 1.5))
    """This is turning people into int and making it so we get
    1.5 treats for every tea bag. Float not needed bc it will 
    always be whole number"""


def cost(tea_count: int, treat_count: int) -> float:
    """Defining tea and treats cost - will be returned as float"""
    return tea_count * 0.5 + treat_count * 0.75
    """This tells us the price of tea and treats"""


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    """This will make the program runable"""
