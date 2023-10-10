x = 1
y = 1.0
z = "1"

if x == y: # python does conversion
    print("one")
if y == int(z): # this is true
    print("two")
elif x == y: # not evaluated since if is true
    print("three")
else: # not evaluated since if is true
    print("four")