'''
Scrivere un programma che esegua un ciclo con un contatore che va da 1
a 30, e ad ogni iterazione (cioè ad ogni esecuzione del ciclo) stampi a
schermo:

➢ “Fizz” se il contatore è multiplo di 3
➢ “Buzz” se il contatore è multiplo di 5
➢ “FizzBuzz” se il contatore è multiplo di entrambi
➢ il valore del contatore in tutti gli altri casi
'''
i = 1
while i <= 30:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

    i = i + 1