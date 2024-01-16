x = 300

def myfunc():
    global x
    x = 200

myfunc() # set x to 200, and being declared with global keyword, it will be printed with 200 value

print(x)