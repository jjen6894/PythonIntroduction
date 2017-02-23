# string = '1234567890'
#
# for char in string:
#     print(char)
#
# print('-------------')
# string_iterated = iter(string)
# print(string_iterated)
# print(next(string_iterated))
# print(next(string_iterated))
# print(next(string_iterated))
# print(next(string_iterated))
# print(next(string_iterated))
# print(next(string_iterated))
# print(next(string_iterated))
# print(next(string_iterated))
# print(next(string_iterated))
# print(next(string_iterated))
#

# mini challenge
numbers = ['1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20']
iter_number = iter(numbers)

i = ''
x = len(numbers)

for i in range(0, x):
    print(next(iter_number))


