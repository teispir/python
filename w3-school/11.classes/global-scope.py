x = 300 # globale al programma e dunque anche alla myfunc

def myfunc():
    print(x)

print("print(x) from myfunc()")
myfunc()

print("print directly the global parameter")
print(x)