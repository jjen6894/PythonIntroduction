# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
# for animal in farm_animals:
#     print(animal)
#
# print("-"*50)
#
# wild_animals = {"Lion", "Tiger", "Panther", "Elephant", "Hare"}
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# empty_set = set()
# empty_set.add("a")
# doesn't create a set makes a dictionary
# empty_set_2 = {}
# empty_set_2.add("a")
#
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
#
# print("-"*50)
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)
even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(sorted(squares.difference(even)))
print(sorted(squares - even))




