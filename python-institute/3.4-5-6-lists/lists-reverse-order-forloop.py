my_list = [10, 1, 8, 3, 5]
length = len(my_list)
print("length",length)
print("my_list before",my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print("my_list after",my_list)