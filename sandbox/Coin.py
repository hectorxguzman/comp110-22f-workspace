"""Flip a coin"""

from random import randint

response: str = randint(0, 1)

input("How can I help you?")
if response == 0:
    print("Heads")
elif response == 1:
        print("Tails")
