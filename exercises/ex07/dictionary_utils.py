"""EX07 Dictionary Test."""

__author__ = "730567965"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Empty Dictionary."""
    user_input: dict[str, str] = dict()
    assert invert(user_input) == dict()


def test_invert_repeat() -> None:
    """Keys repeated."""
    user_input: dict[str, str] = {"kris": "jordan", "michael": "jordan"}
    assert invert(user_input) == KeyError


def test_invert_normal() -> None:
    """Normal Test."""
    user_input: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(user_input) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_favorite_color_empty() -> None:
    """Empty Dictionary."""
    user_input: dict[str, str] = dict()
    assert favorite_color(user_input) == ''


def test_favorite_color_single() -> None:
    """All colors show up once."""
    user_input: dict[str, str] = {"Marc": "yellow", "Ezri": "blue"}
    assert favorite_color(user_input) == 'yellow'
    

def test_favorite_color_normal() -> None:
    """Normal Test."""
    user_input: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(user_input) == 'blue'


def test_count_empty() -> None:
    """Empty Test."""
    user_input: dict[str, str] = dict()
    assert count(user_input) == dict()


def test_count_single() -> None:
    """Each word shows up a single time."""
    user_input: dict[str, str] = ["hector", "jahn"]
    assert count(user_input) == {'hector': 1, 'jahn': 1}


def test_count_normal() -> None:
    """Normal test."""
    user_input: dict[str, str] = ["hector", "hector", "jahn", "hector"]
    assert count(user_input) == {'hector': 3, 'jahn': 1}
