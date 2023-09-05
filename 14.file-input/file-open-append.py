f = open("demofile2.txt", "a") # open a file in append mode
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())