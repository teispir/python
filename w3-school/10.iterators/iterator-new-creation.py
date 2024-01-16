class MyNumbers:
  def __iter__(self):
    self.a = 1 # initialize a attribute to 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1 # __next__() method increment by 1 the a attribute
    return x

myclass = MyNumbers() # creation of a new object from class MyNumbers
myiter = iter(myclass) # creation of iterator from myclass object (it's an iterator since implement those two methods)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))