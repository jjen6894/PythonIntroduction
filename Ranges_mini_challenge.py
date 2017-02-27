o = range(0, 100, 4)
print(o)
p = o[::5]
# print all the values in the range that are multiples of 5
print(p)
for i in p:
    print(i)

range(1,10)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


a = range(1, 10)
for i in a:
    print(i)
print('='*50)
for a in range(21, -1, -2):
    print(a)

print(range(20, 0, -2))
# [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

k = range(10)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# cant use floats
for i in k[:-3]:
    print(i)
