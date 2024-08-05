##  Convert input to a boolean on input

license = input("Do you have your license? y/n ").lower() == 'y'
age = int(input("How old are you? "))


if age >= 16 and license: 

    print("You are old enough to drive.")
else:
    print("you are not able to drive.")
