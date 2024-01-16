import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}' # JSON String

# parse x:
y = json.loads(x) # loads() method returns a dictionary

# the result is a Python dictionary:
print(y["age"])