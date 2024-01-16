class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname) # by default the definition of __init__ function overrides the parent __init__
                                            # but doing so, the properties are kept also in Child class