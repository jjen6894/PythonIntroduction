import shelve

# blt = ["bacon", "eggs", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_egg = ["eggs", "butter", "milk"]
# soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]
pre_game_meal = ["greek yoghurt", "banana"]

with shelve.open('recipes') as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled egg"] = scrambled_egg
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta
    # recipes["prior to game meal"] = pre_game_meal
    #
    # buttered_blt = ["bacon", "eggs", "tomato", "bread", "butter"]
    # recipes["blt"] = buttered_blt
    for meal in recipes:
        print(meal, recipes[meal])



recipes.close()

