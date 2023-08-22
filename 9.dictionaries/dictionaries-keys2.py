car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) # before the change

car["color"] = "white" # change in the dictionary

# the change is reflected into the view of the dictionary (new key:value pair added)
print(x) #after the change

car["brand"] = "Volvo" # change in the value associated to key "brand"

print(car)