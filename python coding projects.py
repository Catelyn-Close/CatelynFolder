#small counter thing
student = 10

classroom = student*30

print(classroom)

school = classroom*12

print(school)

goal = 10000

pagesperstudent = goal/360

print(pagesperstudent)
__________________________________________________________
#team roster printout
string1 = "Welcome to the team {}! Your team number is {}"

# Define a list of tuples with player names and their numbers
players = [
    ("Jane", "1"),
    ("Doe", "2"),
    ("Smith", "3"),
    ("John", "4"),
    ("David", "5"),
    ("Tennant", "6"),
    ("River", "7"),
    ("Amy", "8"),
    ("Rory", "9"),
    ("Bill", "10")
]

# Print each player's name and number using the format method
for player in players:
    print(string1.format(player[0], player[1]))
_____________________________________________________________________
#story concatenation




string1 = "One day "
string2 = "This morning "
string3 = "Yesterday "
string4 = "my shoelace "
string5 = "my pet gopher "
string6 = "my teacher "
string7 = "my mom "
string8 = "my eyeball "
string9 = "wasn't feeling well "
string10 = "slipped on a banana peel "
string11 = "had a little too much sugar "
string12 = "won a trophy because "
string13 = "drove a racecar "
string14 = "in "
string15 = "under "
string16 = "on top of "
string17 = "next to "
string18 = "a hedgehog "
string19 = "an orange beetle "
string20 = "a snail "
string21 = "a kangaroo "
string22 = "a radish "
string23 = "got braces "
string24 = "a golden tooth "
string25 = "went to the circus "
string26 = "attacked "
string27 = "looked "
string28 = "rescued "
string29 = "created "
string30 = "trapped "
string31 = "invented "
string32 = "promised "
string33 = "their "
string34 = "his "
string35 = "her "
string36 = "a "
string37 = "and "
string38 = "then "
string39 = "meanwhile "
string40 = "unfortunately "
string41 = "because "
string42 = "got "
string43 = "who "
string44 = "he "
string45 = "she "








story = string1 + string7 + string10 + string16 + string8 + string39 + string5 + string31 + string24 + string37 + string13

story2 = string3 + string6 + string40 + string26 + string24 + string17 + string18 + string43 + string12 + string11

print(story2.lower())

print(story.upper())

string2.replace("this morning", "this night")
