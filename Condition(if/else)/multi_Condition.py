age = int(input("Enter your age :"))
has_license = False

if age>= 16:
    print("Elligible to drive")
    if has_license:
        print("You can drive")
    else:
        print("You can't drive")

else:
    print("You can't drive this car")