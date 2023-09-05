f = open("myfile.txt", "x") # create a file if doesn't exist, an error is raised if exists

f = open("myfile.txt", "w") # create a file ONLY if doesn't exist, NO error is raised if exists