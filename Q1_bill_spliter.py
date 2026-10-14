# this is the code of bill split into mambers
print("-- This is the code of bill split into mambers --")
bill= float( input("Enter the amount of bill"))
tip_=float(input("Enter the amount of tip you want to give"))
people=int(input("Enter the number of people"))
tip= bill * tip_ /100
t_bill = bill + tip
per_head= t_bill / people
print("The total bill is =", t_bill)
print("The tip is =" ,tip)
print(" The bill per person is =", per_head)
print("-- The prpgram End --")