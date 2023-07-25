# workaround for using append() with tuples

thistuple = ("apple", "banana", "cherry")
y = list(thistuple) # convert into list
y.append("orange") # use append with list
thistuple = tuple(y) # convert it back into tuples

print(thistuple)