# range of indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #2 included #5 excluded: ("cherry", "orange", "kiwi")

# if the first index is not specified, it starts from first elem: index 0
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #index 4 is excluded, so from "apple" to "orange"

# if the last index is not specified, it includes all elements to the end
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) #from "cherry" to the end ("mango")

# 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) # last index is -1 first is -7: ("orange", "kiwi", "melon")