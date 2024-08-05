##  Convert input to a boolean on input

license = input("Do you have your license? y/n ").lower() == 'y'
age = int(input("How old are you? "))


if age >= 16 and license: 

    print("You are old enough to drive.")
else:
    print("you are not able to drive.")

_______________________________________________________
#made madlib, formatted w/ list. hated it

noun1 = input("Choose a noun: ") 

pnoun1 = input("Choose a plural noun: ")

noun2 = input("Choose a noun: ")

place = input("Choose a place: ")

adjective = input("Choose an adjective Describing word: ")

madlib = "I love my {0}. They are very cool. I also like my  {1}. I take both of these everywhere I go, but i also like {2}! I take them many places like {3} for example! People look at me like im {4} but thats okay!"

Wordbank = [noun1, pnoun1, noun2, place, adjective]


formatted_madlib = madlib.format(*Wordbank)
print(formatted_madlib)
