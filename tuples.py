t = 'a', 'b', 'c'
print(t)

print('a', 'b', 'c')
print(('a', 'b', 'c'))

welcome = "Welcome to the nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightening", "Metallica", 1984

print(metallica)
print(bad[0])
# welcome[0] = "Welcome to the Dream"
# tuple object does not support item assignment
print(welcome)
welcome = "Welcome to the Dream", welcome[1], welcome[2]
print(welcome)
