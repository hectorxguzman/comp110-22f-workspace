"""Change weight between KG or LBS."""

weight = float(input("Weight: "))

unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    convert = weight * 2.205
    print("Weight in lbs: " + str(convert))
else:
    convert = weight / 2.205
    print("Weight in Kg: " + str(convert))
