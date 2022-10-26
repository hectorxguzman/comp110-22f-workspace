from random import randint

question: str = input("Ask me a question...")
response: str = randint(0, 2)

if response == 0:
    print("Yes, absolutely")
elif response == 1:
        print("Fuck no")
elif response ==2:
        print("You betcha")
else:
        print("My sources say otherwise")
