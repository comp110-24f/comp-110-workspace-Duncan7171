"""Making a Tea Party"""

__author__ = "730745874"


def main_planner(guests: int) -> None:
    """Entry point of my code so that it can can be output"""
    print("A Cozy Tea Party For " + str(guests) + " People")
    # This will print start phrase with imputed guest amount
    print("Tea Bags: " + str(tea_bags(guests)))
    # this will print amount of tea bags then number of tea bags
    print("Treats: " + str(treats(guests)))
    # This will print number of treats and then number of treats
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    """This will take into account the cost of the tea bags and 
    treasts to print  of party"""
    return None


def tea_bags(people: int) -> int:
    """This is to simply say that people will be a number"""
    return people * 2
    # This will multiply the number of people by
    # 2 since each person needs 2 bags"""


def treats(people: int) -> int:
    """Saying treats wil depend on people and it will retun an int"""
    return int((tea_bags(people=people) * 1.5))
    # Converting people into int and making it so we get 1.5 treats for each tea bag.
    # Float not needed bc it will always be whole number


def cost(tea_count: int, treat_count: int) -> float:
    """Defining tea and treats cost - will be returned as float"""
    return tea_count * 0.5 + treat_count * 0.75
    # This tells us the price of tea and treats
    # It will multiply the tea count by .5 and the treat count by .75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    """This will make the program runable running everything through one main source"""
