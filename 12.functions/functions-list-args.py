def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"] # list
cars = ("volvo", "fiat") # tuple
players = {"ronaldo", "messi", "neymar"} # set

my_function(fruits)
my_function(cars)
my_function(players)

my_function("Pippo")