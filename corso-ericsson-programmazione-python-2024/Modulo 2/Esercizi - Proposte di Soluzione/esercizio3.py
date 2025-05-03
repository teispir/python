dividendo = int(input("Inserire dividendo: "))
divisore = int(input("Inserire divisore: "))

if dividendo % divisore == 0:
    print("Il numero " + str(dividendo) + " è divisibile per " + str(divisore))
else:
    print("Il numero " + str(dividendo) + " non è divisibile per " + str(divisore))
