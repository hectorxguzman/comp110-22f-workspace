"""EX05 Utils."""

__author__ = "730567965"


def only_evens(list: list[int]) -> int:
    """Returning new list of even int."""
    i: int = 0
    evens: list[int] = []
    while (i < len(list)):
        if (list[i] % 2 == 0):
            evens.append(list[i])
        i += 1
    return evens


def concat(list_one: list[int], list_two: list[int]) -> int:
    """Returning lists combined."""
    i: int = 0
    lists_combined: list[int] = []

    while (i < len(list_one)):
        lists_combined.append(list_one[i])
        i += 1

    i = 0

    while (i < len(list_two)):
        lists_combined.append(list_two[i])
        i += 1
    return lists_combined


def sub(a_list: list[int], first: int, last: int) -> int:
    """Returns list between start and end."""
    sub_list: list[int] = []

    if (len(a_list) == 0):
        return sub_list
    else:
        if (first < 0):
            first = 0
        if (last > len(a_list)):
            last = len(a_list)

        while (first < last):
            sub_list.append(a_list[first])
            first += 1
    return sub_list
