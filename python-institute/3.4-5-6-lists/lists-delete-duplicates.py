my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print()
my_list_updated = []

for i in my_list:
    if(i not in my_list_updated):
        my_list_updated.append(i)

print(my_list_updated)

my_list = my_list_updated[:]

print("The list with unique elements only:")
print(my_list)