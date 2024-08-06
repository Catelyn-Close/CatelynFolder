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
__________________________________________________________________________________________________________
#searching writing for keywords and counting strings
string1 = "3 pets ot og eulc txen eht dnif oT"
reverse = string1[::-1]
print(reverse)





string2 = "Alexandra, her father often said to himself, was like her grandfather; which was his way of saying that she was intelligent. John Bergson's father had been a shipbuilder, a man of considerable force and of some fortune. Late in life he married a second time, a Stockholm woman of questionable character, much younger than he, who goaded him into every sort of extravagance. On the shipbuilder's part, this marriage was an infatuation, the despairing folly of a powerful man who cannot bear to grow old. In a few years his unprincipled wife warped the probity of a lifetime. He speculated, lost his own fortune and funds entrusted to him by poor seafaring men, and died disgraced, leaving his children nothing. But when all was said, he had come up from the sea himself, had built up a proud little business with no capital but his own skill and foresight, and had proved himself a man. In his daughter, John Bergson recognized the strength of will, and the simple direct way of thinking things out, that had characterized his father in his better days. He would much rather, of course, have seen this likeness in one of his sons, but it was not a question of choice. As he lay there day after day he had to accept the situation as it was, and to be thankful that there was one among his children to whom he could entrust the future of his family and the possibilities of his hard-won land."

check = "gold" in string2






string3 = "When Anne reached the school that morning . . . for the first time in her life she had traversed the Birch Path deaf and blind to its beauties . . . all was quiet and still. The preceding teacher had trained the children to be in their places at her arrival, and when Anne entered the schoolroom she was confronted by prim rows of shining morning faces and bright, inquisitive eyes. She hung up her hat and faced her pupils, hoping that she did not look as frightened and foolish as she felt and that they would not perceive how she was trembling. She had sat up until nearly twelve the preceding night composing a speech she meant to make to her pupils upon opening the school. She had revised and improved it painstakingly, and then she had learned it off by heart. It was a very good speech and had some very fine ideas in it, especially about gold and earnest striving after knowledge. The only trouble was that she could not now remember a word of it.After what seemed to her a year. . .about ten seconds in reality . . .she said faintly, Take your Testaments, please, and sank breathlessly into her chair under cover of the rustle and clatter of desk lids that followed. While the children read their verses Anne marshalled her shaky wits into order and looked over the array of little pilgrims to the Grownup Land.Most of them were, of course, quite well known to her. Her own classmates had passed out in the preceding year but the rest had all gone to school with her, excepting the primer class and ten newcomers to Avonlea. Anne secretly felt more interest in these ten than in those whose possibilities were already fairly well mapped out to her. To be sure, they might be just as commonplace as the rest; but on the other hand there might be a genius among them. It was a thrilling idea.Sitting by himself at a corner desk was Anthony Pye. He had a dark, sullen little face, and was staring at Anne with a hostile expression in his black eyes. Anne instantly made up her mind that she would win that boy's affection and discomfit the Pyes utterly.In the other corner another strange boy was sitting with Arty Sloane. . .a jolly looking little chap, with a snub nose, freckled face, and big, light blue eyes, fringed with whitish lashes. . . probably the Donnell boy."

check2 = "gold" in string3
_________________________________________________________________________________________________
#for list loop
list = ["tree ", "trees ", "leaves ", "leaf ", "cone ", "cat ", "dog ", "table ", "desk ", "mouse "]

for x in list:
    print("While I was taking my " + x + "for a walk, another giant " + x + "came out of nowhere and chased me all the way home!")

