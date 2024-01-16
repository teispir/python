my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
steps = 0
cycles = 0

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            steps+=1
    cycles +=1        
print(my_list)
print("Bubble Sort took these steps to complete", steps, " in this cycles", cycles)