count = 1

while count <= 30:
    if count % 3 == 0 and count % 5 == 0:
        print(str(count) + ": FizzBuzz")
    elif count % 3 == 0:
        print(str(count) + ": Fizz")
    elif count % 5 == 0:
        print(str(count) + ": Buzz")
    else:
        print(count)
    count += 1
