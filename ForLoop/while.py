# i = 0
# while i < 10:
#     print(i)
#     i += 1
#
quitter = ['quit', 'Quit']
options = ['left door, right door, middle door']
right_option = 'left door'
chosen_option = ''
choice_counter = 0
while chosen_option != right_option:
    if choice_counter == 2:
        print('GAME OVER.. Monster ate your guts!!')
        break
    print("You are in a room with four ways out... here are your options {}".format(options))
    chosen_option = input('Chose an option: ')
    choice_counter += 1
    if chosen_option in quitter:
        print('GAME OVER')
        break
