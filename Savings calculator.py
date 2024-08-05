# create code for savings calculator. How many months should save to reach target goal
# assume salary is minimum wage


print("minimum Wage Savings Calculator")
print("The program will tell you many months you will need to work")
s = float(input("enter wanted savings:"))

m = 1257
a = s/m

print(round(a))
print("months")


____________________________________________
#made another, bit different

earningsgoal = int(input("How much money do you want to save? "))

months = round(earningsgoal/12, 2)

weeks = round(months/52, 2)

days = round(earningsgoal/365, 2)

print("To save up " + str(earningsgoal) + " per year, you will need to save " + str(months) + " dollars per month")
print("To save up " + str(earningsgoal) + " per year, you will need to save " + str(weeks) + " dollars per week")
print("To save up " + str(earningsgoal) + " per year, you will need to save " + str(days) + " dollars per day")


