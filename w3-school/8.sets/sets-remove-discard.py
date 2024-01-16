# remove() raises an error if item not preset

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") # remove ok
thisset.remove("mango") # remove not ok, with an error
print(thisset)


# discard() doesn't raise an error if item not present

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
thisset.discard("mango") # discard not ok, but no error
print(thisset)