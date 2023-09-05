try:
  print(x)
except NameError: # type of exception
  print("Variable x is not defined")
except:
  print("Something else went wrong")