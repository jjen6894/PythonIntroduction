fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         'lime': "a sour, green citrus fruit"}

print(fruit)
print(fruit['orange'])
print(fruit['lime'])
print(fruit['lemon'])
fruit["pear"] = "an odd shaped apple"
print(fruit)
fruit["pear"] = "great with for cider"
# existing key overight save the new value
print(fruit)


del fruit["lemon"]
print(fruit)
fruit.clear()
print(fruit)