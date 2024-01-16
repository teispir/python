def myfunc():
    global x
    x = 300

myfunc()

print(x) # property x is local to myfunc, but with global scope thanks to 'global keyword'