class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self): # __next__() method modified with StopIteration when a reaches 20
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)