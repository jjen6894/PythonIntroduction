locations = {0: {"desc": "You are sitting in front of a computer learning Python",
                 "exits": {},
                 "named_exits": {}},
             1: {"desc": "You are standing at the end of a road before a small brick building",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "named_exits": {"2": 2, "3": 3, "4": 4, "5": 5}},
             2: {"desc": "You are at the top of a hill",
                 "exits": {"N": 5, "Q": 0},
                 "named_exits": {"5": 5}},
             3: {"desc": "You are inside a building, a well house for a small stream",
                 "exits": {"W": 1, "Q": 0},
                 "named_exits": {"1": 1}},
             4: {"desc": "You are in a valley beside a stream",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "named_exits": {"1": 1, "2": 2}},
             5: {"desc": "You are in a forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "named_exits": {"2": 2, "1": 1}}
             }
vocabulary = {"NORTH": "N",
                       "SOUTH": "S",
                       "WEST": "W",
                       "EAST": "E",
                       "QUIT": "Q",
                       "ROAD": "1",
                       "HILL": "2",
                       "BUILDING": "3",
                       "VALLEY": "4",
                       "FOREST": "5"}
# print(locations[1])
# print(locations[1].get('exits'))

loc = 1
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
