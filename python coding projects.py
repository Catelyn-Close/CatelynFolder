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
