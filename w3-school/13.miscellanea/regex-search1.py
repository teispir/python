import re

txt = "The rain in Spain"
x = re.search("\s", txt) # search returns a Match Object

print("The first white-space character is located in position:", x.start()) 