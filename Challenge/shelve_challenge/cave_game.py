import shelve

game = shelve.open("game")
loc = game['loc']
locations = game['locations']
vocabulary = game['vocabulary']

while True:
    available_exits = ', '.join(locations[loc]["exits"].keys())

    print(locations[loc]["desc"])

    if loc == 0:
        break
    else:
        all_exits = locations[loc]['exits'].copy()
        all_exits.update(locations[loc]["named_exits"])

    direction = input("Available exits are " + available_exits).upper()
    print()
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in all_exits:
        loc = all_exits[direction]
    else:
        print("You cannot go in that direction")
game.close()