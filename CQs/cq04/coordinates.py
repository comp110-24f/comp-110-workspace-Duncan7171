"""Challenge question 3"""

__author__ = "730745874"


def get_coords(xs: str, ys: str) -> None:
    """Here we are making a function called coords with 2 parameters returning None"""
    index_1: int = 0
    # Creating an index for xs
    index_2: int = 0
    # Creating an index for ys
    while index_1 < len(xs):
        # Creating a while loop for when the length of xs is less than index_1
        while index_2 < len(ys):
            # Adding a loop for when length of ys is longer than index_1
            print("(" + xs[index_1] + "," + ys[index_2] + ")")
            # Printing the compinations out
            index_2 += 1
            # Adding one to index 2
        index_1 += 1
        # Adding one to index 1 so it will move on past the first character in xs
        index_2 = 0
        # Setting index 2 back to 0
