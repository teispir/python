# definition of global var x
x = 300

def myfunc():
    # definition of variable x, local to myfunc()
    x = 200
    print(x)

print("about to print 200")
myfunc() # it prints 200

print("about to print 300")
print(x) # it prints 300