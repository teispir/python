def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) # myfunc restituisce una funzione lambda che moltiplica l'argomento per 2
print(mydoubler) # questo oggetto è una funzione lambda, e bisogna passargli l'argomento a

print(mydoubler(11)) # restituisce 22

mytripler = myfunc(3)
print(mytripler(11)) # restituisce 33