"""Copy of Chardle"""

__author__ = "730567965"

five: str = input("Enter a five-character word:")

if len(five) == 5:
    single: str = input("Enter a single-character:")
    if len(single) == 1:
        instance = 0
        print("Searching for " + single + " in " + five)
        if single == five[0, 1, 2, 3, 4]:
            if [0]:
                print(single + " found at index 0")
            instance = instance + 1
            if [1]:
                print(single + " found at index 1")
            instance = instance + 1
            if [2]:
                print(single + " found at index 2")
            instance = instance + 1
            if [3]: 
                print(single + " found at index 3")
            instance = instance + 1 
            if [4]:
                print(single + " found at index 4")
            instance = instance + 1
            if instance == 0:
                print("No instance of " + single + " found in " + five)
        else:
            if instance == 1:
                print("1 instance of " + single + " found in " + five)

            else: 
                print(instance, "instances of " + single + " in " + five)
    else:
        print("Error: Character must be a single character.")
else:
    print("Error: Word must contain 5 characters")