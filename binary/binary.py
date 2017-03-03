# for i in range(1000):
#     print("{0:>2} in binary is {0:>08b} ".format(i))
#
# with open("binary", "bw") as bin_file:
#     bin_file.write(bytes(range(17)))
#
# with open("binary", 'br') as bin_file:
#     for b in bin_file:
#         print(b)

a = 65534 # FF FE
b = 65535  #FF FF
c = 65536   # 00 01 00 00
x = 2998302 # 02 2D C0 1E

with open("binary2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little'))
