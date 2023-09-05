import json

print(json.dumps({"name": "John", "age": 30})) # dict
print(json.dumps(["apple", "bananas"])) # list 
print(json.dumps(("apple", "bananas"))) # tuple
print(json.dumps("hello")) # string
print(json.dumps(42)) # int
print(json.dumps(31.76)) # float
print(json.dumps(True)) # True 
print(json.dumps(False)) # False
print(json.dumps(None)) # None