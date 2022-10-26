"""EX05 Utils Test."""

__author__ = "730567965"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty_list() -> None:
    """Empty list."""
    list: list[int] = []
    assert only_evens(list) == []


def test_only_evens_odds() -> None:
    """Odd integers."""
    list: list[int] = [1, 3, 5]
    assert only_evens(list) == []


def test_only_evens_both() -> None:
    """Both even & odds."""
    list: list[int] = [1, 2, 3, 4]
    assert only_evens(list) == [2, 4]


def test_only_evens() -> None:
    """Only even integers."""
    list: list[int] = [4, 4, 4]
    assert only_evens(list) == [4, 4, 4]


def test_concat_combined() -> None:
    """Combination of lists."""
    list_one: list[int] = [1, 2, 3]
    list_two: list[int] = [4, 5, 6]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6]


def test_concat_empty_list_one() -> None:
    """Empty list."""
    list_one: list[int] = [1, 2, 3]
    list_two: list[int] = []
    assert concat(list_one, list_two) == [1, 2, 3]


def test_concat_empty_list_two() -> None:
    """Empty list."""
    list_one: list[int] = [1, 2, 3]
    list_two: list[int] = []
    assert concat(list_one, list_two) == [1, 2, 3]


def test_concat_empty_lists() -> None:
    """Both empty lists."""
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == []


def test_sub_empty_list() -> None:
    """Empty list and int."""
    a_list: list[int] = []
    first: int = 0
    last: int = 0
    assert sub(a_list, first, last) == []


def test_sub_start_end() -> None:
    """Start and end ints."""
    a_list: list[int] = [1, 2, 3]
    first: int = 0
    last: int = 0
    assert sub(a_list, first, last) == []


def test_sub_empty_start_end() -> None:
    """Empty list."""
    a_list: list[int] = []
    first: int = 1
    last: int = 3
    assert sub(a_list, first, last) == []


def test_sub_negative() -> None:
    """Negative first."""
    a_list: list[int] = [10, 20, 30, 40]
    first: int = -1
    last: int = 3
    assert sub(a_list, first, last) == [10, 20, 30]


def test_sub_greater() -> None:
    """Greater last."""
    a_list: list[int] = [10, 20, 30, 40]
    first: int = 0
    last: int = 5
    assert sub(a_list, first, last) == [10, 20, 30, 40]


def test_sub() -> None:
    """Regular sub."""
    a_list: list[int] = [10, 20, 30, 40]
    first: int = 1
    last: int = 3
    assert sub(a_list, first, last) == [20, 30]