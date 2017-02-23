# i = 0
# while i < 10:
#     print(i)
#     i += 1
#
# quitter = ['quit', 'Quit']
# options = ['left door, right door, middle door']
# right_option = 'left door'
# chosen_option = ''
# choice_counter = 0
# while chosen_option != right_option:
#     if choice_counter == 2:
#         print('GAME OVER.. Monster ate your guts!!')
#         break
#     print("You are in a room with four ways out... here are your options {}".format(options))
#     chosen_option = input('Chose an option: ')
#     choice_counter += 1
#     if chosen_option in quitter:
#         print('GAME OVER')
#         break
import random

highest = 1000
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print('Please guess higher')
    else:
        print('Please guess lower')
    guess = int(input())
    if guess == answer:
        print("Well done you guessed it!")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("Well done, got it in one!")
