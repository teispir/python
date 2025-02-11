def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s

print(list_sum([5,4,3]))
print("***")
print(list_sum(4)) # TypeError: 'int' object is not iterable