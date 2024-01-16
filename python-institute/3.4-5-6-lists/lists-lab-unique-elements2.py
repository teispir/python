my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for i in range(len(my_list)):
    num = my_list[i]
    if num in my_list[i+1:]:
        print("found, removing elem", num)
        my_list.remove(num)
    else:
        print("doing nothing")
    print("my_list length", len(my_list))
    print("i",i)
    print(my_list)

print("The list with unique elements only:")
print(my_list)