# True and 1 are considered as the same item, they are treated as duplicates

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)