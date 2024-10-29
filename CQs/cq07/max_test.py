"""Test CQ"""

__author__ = "730745874"


from CQs.cq07.find_max import find_and_remove_max


def test_value_returned() -> None:
    """Testing that max value is returned"""
    a = [1, 2, 3, 4, 5]
    assert find_and_remove_max(a) == 5


def test_value_removed() -> None:
    """Testing max value is removed"""
    a = [1, 2, 3, 4, 5]
    find_and_remove_max(a)
    assert a == [1, 2, 3, 4]


def test_value_diff_input() -> None:
    """Looking into different case"""
    a = [5, 5, 5, 5]
    assert find_and_remove_max(a) == 5
