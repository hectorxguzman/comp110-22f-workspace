"""EX07 Dictionary."""

__author__ = "730567965"


def invert(user_input: dict[str, str]) -> dict[str, str]:
    """Inverting users input keys and values."""
    inverted_input: dict[str, str] = dict()
    for key in user_input:
        if user_input[key] in inverted_input:
            raise KeyError
        inverted_input[user_input[key]] = key
    return inverted_input

        
def favorite_color(user_input: dict[str, str]) -> str:
    """Most frequently favorited color."""
    result: dict[str, int] = dict()
    i: int = 0
    names: str = ""
    for key in user_input:
        if user_input[key] in result:
            result[user_input[key]] += 1
        else:
            result[user_input[key]] = 1
    for key in result:
        if i < result[key]:
            i = result[key]
            names = key
    return names


def count(user_input: list[str]) -> dict[str, int]:
    """Counts strings."""
    result: dict[str, int] = dict()
    i: int = 0
    h: int = 0
    calc: int = 0
    value: str = ""

    while (h < len(user_input)):
        value = user_input[h]
        while (i < len(user_input)):
            if (user_input[i] == value):
                calc += 1
            i += 1
        result[user_input[h]] = calc
        calc = 0
        i = 0
        h += 1
    return result