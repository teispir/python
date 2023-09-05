import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) # Print the part of the string where there was a match

print(x.group()) # Spain