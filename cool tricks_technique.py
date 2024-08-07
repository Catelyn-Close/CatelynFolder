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
________________________________________________________
# Take input from the user and convert it to a list of integers
my_list = [int(n) for n in input("Input a list of numbers: ").split()]

# Iterate through the list and print the even numbers
for x in my_list:
    if x % 2 == 0:
        print(x)
______________________________________________________________
# Take input from the user and convert it to a list of strings
countries_to_visit = input("Input a list of countries you would like to visit, separated by spaces: ").split()

# Iterate through the list and print countries containing the letter "p" (case-insensitive)
for country in countries_to_visit:
    if 'p' in country.lower():
        print(country)
