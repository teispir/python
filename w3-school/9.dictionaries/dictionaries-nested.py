# keys are child1,2.3 and values are dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

child1a = {
  "name" : "Emil",
  "year" : 2004
}
child2a = {
  "name" : "Tobias",
  "year" : 2007
}
child3a = {
  "name" : "Linus",
  "year" : 2011
}

myfamily2 = {
  "child1" : child1a,
  "child2" : child2a,
  "child3" : child3a
}

print(myfamily2)
