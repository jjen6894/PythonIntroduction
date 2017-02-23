parrot_list = ["non pinin' ", "no more", "a stiff", "bereft of life"]

parrot_list.append(("A Noreweigen Blue"))

for state in parrot_list:
    print("The parrot is: {}".format(state))


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = odd + even
numbers_in_order = sorted(numbers)
print(numbers)
print(numbers_in_order)
print(sorted(numbers))
print(numbers.sort())