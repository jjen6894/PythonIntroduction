import shelve

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250

    del bike['engin_size']
    del bike['e_size']
    print(bike["engine_size"], bike["colour"])
    for key in bike:
        print(key)
