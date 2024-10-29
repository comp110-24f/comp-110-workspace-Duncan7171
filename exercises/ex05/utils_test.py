"""Lists!!"""

__author__ = "730745874"


from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_numbers_returned() -> None:
    """Testing that even numbers are returned"""
    a = [1, 2, 3]
    output = only_evens(a)
    result = [2]
    for index in range(len(output)):
        assert output[index] == result[index]


def test_only_evens_numbers_mutate() -> None:
    """Testing that list has all even numbers"""
    a = [1, 2, 3, 4, 5, 6]
    copy_list = [1, 2, 3, 4, 5, 6]
    only_evens(a)
    assert len(a) == len(copy_list)
    for index in range(len(a)):
        assert copy_list[index] == a[index]


def test_only_evens_all_odd_numbers_edge() -> None:
    """Testing to see if it returns an empty list if no even numbers"""
    a = [1, 3, 5, 7]
    output = only_evens(a)
    result = []
    for index in range(len(output)):
        assert output[index] == result[index]


def test_sub_returned_value() -> None:
    """Testing to see if correct values are returned"""
    a = sub([1, 2, 3, 4, 5], 2, 4)
    result = [3, 4]
    for index in range(len(a)):
        assert a[index] == result[index]


def test_sub_mutate() -> None:
    """Making sure the origional list is not mutated"""
    a = [1, 2, 3, 4, 5, 6]
    copy_list = [1, 2, 3, 4, 5, 6]
    sub(a, 2, 4)
    assert len(a) == len(copy_list)
    for index in range(len(a)):
        assert copy_list[index] == a[index]


def test_sub_edge() -> None:
    """Testing the sub function with indexes out of range of function"""
    lst = [1, 2, 3, 4, 5, 6]
    a = sub(lst, -100, 100)
    result = [1, 2, 3, 4, 5, 6]
    for index in range(len(a)):
        assert a[index] == result[index]


def test_add_at_index_return() -> None:
    """Testing to see if None is returned"""
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert add_at_index(test_list, new_number=9, number_location=2) == None


def test_add_at_index_mutate() -> None:
    """Testing to see that number is inserted at right index and is right number"""
    test_list: list[int] = [1, 2, 3, 4, 5]
    add_at_index(test_list, new_number=9, number_location=2)
    assert test_list[2] == 9


def test_add_at_index_raises_inedex_error():
    """Testing that function raises an index error if there is invalid index"""
    with pytest.raises(IndexError):
        add_at_index([], 4, 4)


def test_add_at_index_edge() -> None:
    """Testing to see if number is added in correct place with all same number"""
    test_list: list[int] = [1, 1, 1, 1, 1]
    add_at_index(test_list, new_number=1, number_location=1)
    assert test_list[1] == 1
