# for i in range(1000):
#     print("{0:>2} in binary is {0:>08b} ".format(i))

with open("binary", "bw") as bin_file:
    bin_file.write(bytes(range(17)))

with open("binary", 'br') as bin_file:
    for b in bin_file:
        print(b)
