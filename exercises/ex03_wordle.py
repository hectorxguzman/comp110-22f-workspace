"""EX03 Wordle Assignment."""

__author__ = "730567965"


def contains_char(secret: str, single_char: str) -> bool:
    """Test characters in secret word."""
    assert len(single_char) == 1
    i: int = 0
    while i < len(secret):
        if secret[i] == single_char:
            return True
        else:
            i += 1
    return False


def emojified(user_input: str, secret: str) -> str:
    """Return corresponding emoji boxes."""
    assert len(user_input) == len(secret)
    wrong: str = "\U00002B1C"
    correct: str = "\U0001F7E9"
    right_wrong: str = "\U0001F7E8"
    index: int = 0
    box: str = ""
    i: int = 0
    while i < 6:
        contains_char(secret, user_input[0])
        i += 1
        while index < len(secret):
            if user_input[index] == secret[index]:
                box = box + correct
                index = index + 1
            else:
                boolean: bool = False
                i = 0
                while boolean is False and i < len(secret):
                    if secret[i] == user_input[index]:
                        boolean = True
                    else:
                        i += 1
                if boolean is True:
                    box += right_wrong
                    index += 1
                else:
                    box += wrong
                    index += 1
    return (box)   


def input_guess(len_guess: int) -> str:
    """Guess return expected length."""
    user_input: str = input(f"Enter a {len_guess} character word: ")
    i: int = 0
    while i == 0:
        if (len(user_input) != len_guess):
            user_input = input(f"That wasn't {len_guess} chars! Try again: ")
        else: 
            i = 1
    return (user_input)


def main() -> None: 
    """Main game loop."""
    loop: int = 1
    correct_guess: str = "codes"
    while loop < 7:
        print(f"=== Turn {loop}/6 ===")
        guess: str = input_guess(5)
        print(emojified(guess, correct_guess))
        if (guess == correct_guess):
            print(f"You won in {loop}/6 turns!")
            return None
        loop += 1
    print("X/6 - Sorry, try again tomorrow!")
    return None


if __name__ == "__main__":
    main()