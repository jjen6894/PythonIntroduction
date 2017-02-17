shopping_list = ["milk", "pasta","eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == "spam":
        print("I am ignoring {}".format(item))
        continue
    print("Buy " + item)

print("--------------------")
for item in shopping_list:
    if item == "spam":
        break
    print("Buy " + item)
print("-------------------")
meal = ["egg", "bacon", "spam", "sausages"]

for items in meal:
    if item == 'spam':
        nasty_food_item = item
        break
if nasty_food_item:
    print("Can't I have anything without spam in it")