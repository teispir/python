# remove an element in a tuple

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")

thistuple = tuple(y)

print(thistuple)