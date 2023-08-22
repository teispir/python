thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# print all keys of a dictionary in a loop (1)
for x in thisdict:
    print(x)

print("---")

# print all keys of a dictionary in a loop (2)
for x in thisdict.keys():
    print(x)

print("---")

# print all values of a dictionary in a loop (1)
for x in thisdict:
    print(thisdict[x])

print("---")

# print all values of a dictionary in a loop (2)
for x in thisdict.values():
    print(x)

print("---")

# print both keys and values of a dictionary
for x, y in thisdict.items():
    print(x, y)