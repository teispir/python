my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list=[]

for i in range(len(my_list)):
    num = my_list[i]
    if num in my_list[i+1:]:
        print(num," found")
    else:
        new_list.append(num)
    
print("The list with unique elements only:")
print(new_list)