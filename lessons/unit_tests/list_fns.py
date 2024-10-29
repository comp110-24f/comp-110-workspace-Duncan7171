def get_first(input: list[str]) -> str:
    """Return first element"""
    return input[0]


# remove first takes a list[str] as input and removes first elmement
def remove_first(input: list[str]) -> None:
    """Remove first element"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Remove and return first element."""
    first_elem: str = input[0]
    input.pop(0)  # remove first_elem
    return first_elem
