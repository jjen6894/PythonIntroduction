decimals = range(0, 100)
print(decimals)
my_range = decimals[3:40:3]
print(my_range)
print(my_range == range(3, 40, 3))
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

r = decimals
print(r)

for i in r[::-2]:
    print(i)

