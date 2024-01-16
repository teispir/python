# this example generates an error

thistuple = ("apple", "banana", "cherry")

for i in len(thistuple): # TypeError: 'int' object is not iterable
  print(thistuple[i])