__author__ = "Jack"
# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {}".format(18-age))

print("Please guess a number between 1 and 10: ")
guess = int(input())
if guess > 10:
    print("Idiot!")
if guess < 0:
    print("Fool! I said between 0 & 10")
if guess != 5:
    if guess < 5:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done you have guessed correctly!")
    else:
        print("Unlucky, you have failed!")
else:
    print("You got it in one!")
