"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730567965"

five: str = input("Enter a five-character word: ")

if len(five) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single: str = input("Enter a single-character: ")
if len(single) != 1:
    print("Error: Character must be a single character.")
    exit()
instance = 0
print("Searching for " + single + " in " + five)
if single == five[0]:
    print(single + " found at index 0")
    instance = instance + 1
if single == five[1]:
    print(single + " found at index 1")
    instance = instance + 1
if single == five[2]:
    print(single + " found at index 2")
    instance = instance + 1
if single == five[3]: 
    print(single + " found at index 3")
    instance = instance + 1 
if single == five[4]:
    print(single + " found at index 4")
    instance = instance + 1
if instance == 0:
    print("No instances of " + single + " found in " + five)
else:
    if instance == 1:
        print("1 instance of " + single + " found in " + five)

    else: 
        print(str(instance) + " instances of " + single + " found in " + five)
