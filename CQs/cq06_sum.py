"""Summing the elements of a list using different loops"""

__author__ = "730745874"


def w_sum(vals: list[float]) -> float:
    """Adding up numbers with a while loop"""
    index = 0
    total = 0.0
    while index < len(vals):
        total += vals[index]
        index += 1
        # Using index to go through each value
    return total


def f_sum(vals: list[float]) -> float:
    """Adding numbers using a for loop"""
    total = 0.0
    for numbers in vals:
        total += numbers
        # Going through each number in vals and adding to total
    return total


def f_range_sum(vals: list[float]) -> float:
    """Adding numbers in for loop using range"""
    total = 0.0
    for numbers in range(len(vals)):
        total += vals[numbers]
        # Using range in for loop adding each number in list together
    return total
