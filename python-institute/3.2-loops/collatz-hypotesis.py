c0 = int(input("Enter non negative and non zero integer: "))
steps = 0

while (c0 != 1):

    if (c0%2==0): # even number
        c0 = c0//2
    elif (c0%2==1): # odd number
        c0 = 3*c0+1
    else:
        print("impossible")
    print("c0",c0)
    steps+=1
print("steps",steps)
