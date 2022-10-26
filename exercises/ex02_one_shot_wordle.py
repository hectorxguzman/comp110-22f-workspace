""""EX02 One Shot Wordle Assignment."""
__author__= "730567965"

secret: str = "python" 
user_input: str = input(f"What is your {len(secret)}-letter guess? ")

while(len(user_input) != len(secret)):
    user_input = str = input(f"That was not {len(secret)} letters! Try again: ")

wrong: str = "\U00002B1C"
correct: str = "\U0001F7E9"
right_wrong: str = "\U0001F7E8"
box: str = ""
i: int = 0

while i < len(secret):
    if user_input[i] == secret[i]:
        box = box + correct
    else:
        h: int = 0
        guess: bool = True
        while h < len(secret):
            if user_input[i] == secret[h]:
                box = box + right_wrong
                h = len(secret)
                guess = False
            else:
                h = h + 1
        if guess:
            box = box + wrong
    
    i = i + 1

print(box) 

if user_input != secret:
    print("Not quite. Play again soon!")

if user_input == secret:
    print("Woo! You got it!")