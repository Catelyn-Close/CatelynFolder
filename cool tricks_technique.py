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
__________________________________________________________________
my_list = [int(n) for n in input("Enter integers separated by spaces: ").split()]

# Initialize the product variable to 1
product = 1

# Multiply all integers in the list
for num in my_list:
    product *= num

# Print the product
print(product)
___________________________________________________________________
extra = input("input 1 treats. ")
extra2 = input("input 1 treats. ")

treats = ["popcorn", "popsicles", "soda", "chips", "cookies"]

treats.append(extra)
treats.append(extra2)

print(treats)
_______________________________________________________________
games = ["swimming " + "triathalon " + "weightlifting "]
newgames = ["running " + "horse riding "]

games.extend(newgames)

print(games)
___________________________________________________________________
harvest = ["pumpkins", "apples", "corn", "squash", "carrots"]

treefruit = harvest.pop(1)

harvest.remove("squash")

print(harvest)
____________________________________________________________________
a = input("input a list of names ").split()


statement = " got the bronze medal"

print(a[2] + statement)
____________________________________________________________________
numbers = [int(n) for n in input().split()]
biggest = max(numbers)
print(biggest)
____________________________________________________________________

Total = 0
n = None
while n != 0:
    n = int(input("Input a number: "))
    if n != 0:
        Total += n
print(Total)

#if n != 0 :
#True if a is not equal to b, and False if a is equal to b.
#if statement is false then the total is added
_____________________________________________________________________
maximum = []

while True:
    n = int(input("Input a number: "))
    maximum.append(n)
    if n == 0:
        break
    
        
        
print(max(maximum))
__________________________________________________________________
shopping = {}

apple = int(input("How many apples? "))
banan = int(input("How many bananas? "))
strawb = int(input("How many strawberries? "))

if apple > 5:
    shopping["apples"] = apple

if banan > 7:
    shopping["bananas"] = banan

if strawb > 3:
    shopping["strawberries"] = strawb

#apples : 5,
#bananas : 7,
#strawberries : 3

print(shopping)
___________________________________________________________________
