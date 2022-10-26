"""Assignment 4 Utils."""

__author__ = "730567965"


def all(values: list[int], individual_value: int) -> bool:
    """Finding number in list."""
    i: int = 0
    if len(values) == 0:
        return False
    while i < len(values):
        if values[i] != individual_value:
            return False
        i += 1
    return True


def max(user_input: list[int]) -> int:
    """Return largest int."""
    if len(user_input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max: int = user_input[0]
    while i < len(user_input):
        if user_input[i] > max:
            max = user_input[i]
        i += 1
    return max


def is_equal(initial_list: list[int], second_list: list[int]) -> bool:
    """Return True if equal in both list."""
    smaller_list: int = len(initial_list)
    if len(initial_list) == len(second_list):
        i: int = 0
        while i < smaller_list:
            if initial_list[i] != second_list[i]:
                return False
            i += 1
        return True
    return False
