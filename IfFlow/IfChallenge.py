# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to gon on an 18-30 holiday must be over 18
# under 31
# if they are welcome them to the holiday otherwise print a polite message
# refusing them entry

name = input("What's your name? ")
age = int(input("Also, what's your age {0}? ".format(name)))

if 18 <= age < 31:
    print("Welcome {0}! You are entitled to go on this amazing lad or ladette holiday".format(name))
else:
    print("Sorry {0}, you aren't eligible to part-take in this holiday!".format(name))
