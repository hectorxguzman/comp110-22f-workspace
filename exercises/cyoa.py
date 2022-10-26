"""Choose your own adventure EX06."""

__author__ = "730567965"

# Setting a global variables for points and player name
from random import randint

points: int = 0
player: str
final_score: int = 0
STAR_CODE: str = "\U0001F31F"
 

def greet() -> None:
    """This is where the game starts and the player is greeted."""
    global player
    player = str(input("What would you like to be called: "))
    print(f"Greetings {player}, welcome to the start of a new relationship! ")
    print("In this Pet simulator, you will choose between a dog or cat and caring for the pet based on the given options.")


def main() -> None: 
    """This is where we give the player three options."""
    global final_score
    greet()
    game_running: bool = True
    while game_running:
        print(f"Your total score is: {int(final_score)}")
        player_choice = input("Choose your pet: Dog\U0001F415	or Cat\U0001F431 or Quit. 'Type as Presented' ")
        if player_choice == str("Dog"):
            dog_life()
        elif player_choice == str("Cat"):
            cat_life()
        elif player_choice == str("Quit"):
            game_running = False
    quit_game()


def random_emotion() -> None:
    """Random emotion from your pet."""
    random_action: int = randint(0, 2)
    if random_action == 0:
        print("Your pet is happy.\U0001F601")
    elif random_action == 1:
        print("Your pet is sad.\U0001F97A")
    elif random_action == 2:
        print("Your pet is hungry.\U0001F37D")


def dog_life() -> None:
    """Player chooses different actions for pet."""
    global points
    global final_score
    global STAR_CODE
    dog_life_running: bool = True
    while dog_life_running:
        player_action: str = input("Choose a number: 0 - Cuddle your pet 1 - Feed your pet 2 - Ignore your pet 3 - Leave pet at home 4 - Give pet a treat 5 - Abandon pet ")
        if player_action == "0":
            print(f"Pet has been cuddled. +5 points!{STAR_CODE}")
            points += 10
            random_emotion()
        elif player_action == str("1"):
            print(f"Pet has been fed. +5 points!{STAR_CODE}")
            points += 5
            random_emotion()
        elif player_action == str("2"):
            print("Pet is lonely :( -5 points.")
            points -= 5
            random_emotion()
        elif player_action == str("3"):
            print("Pet has been left alone. -10 points.")
            points -= 10
            random_emotion()
        elif player_action == str("4"):
            print(f"Pet is happy after reciving treat :) +10 points!{STAR_CODE}")
            points += 10
            random_emotion()
        elif player_action == str("5"):
            dog_life_running = False
            final_score = int(str(points))


def cat_life() -> None:
    """Player chooses different actions for pet."""
    global points
    global final_score
    global STAR_CODE
    cat_life_running: bool = True
    while cat_life_running:
        player_action: str = input("Choose a number: 0 - Cuddle your pet 1 - Feed your pet 2 - Ignore your pet 3 - Leave pet at home 4 - Give pet a treat 5 - Abandon pet ")
        if player_action == "0":
            print(f"Pet has been cuddled. +5 points!{STAR_CODE}")
            points += 10
            random_emotion()
        elif player_action == str("1"):
            print(f"Pet has been fed. +5 points!{STAR_CODE}")
            points += 5
            random_emotion()
        elif player_action == str("2"):
            print("Pet is lonely :( -5 points.")
            points -= 5
            random_emotion()
        elif player_action == str("3"):
            print("Pet has been left alone. -10 points.")
            points -= 10
            random_emotion()
        elif player_action == str("4"):
            print(f"Pet is happy after reciving treat :) +10 points!{STAR_CODE}")
            points += 10
            random_emotion()
        elif player_action == str("5"):
            cat_life_running = False
            final_score = int(str(points))


def points_accumulated(points: int) -> int:
    """Returning points."""
    global final_score
    return final_score


def quit_game() -> None:
    """User calls to quit the game."""
    global player
    print(f"""Thanks for playing {player}. \nFinal Score: {points_accumulated(points)}""")


if __name__ == "__main__":
    main()