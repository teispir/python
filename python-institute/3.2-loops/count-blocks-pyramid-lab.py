blocks = int(input("Enter the number of blocks: "))

height = 0

while (blocks > 0):

    if (blocks > height):
        height = height + 1
        blocks = blocks - height
        print("height",height)
        print("blocks",blocks)
        print("---")
    else:
        print("blocks",blocks)
        break
    
print("The height of the pyramid:", height)