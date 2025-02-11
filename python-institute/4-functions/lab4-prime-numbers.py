def is_prime(num):
    if num < 2:
        return False  # I numeri minori di 2 non sono primi
    for i in range(2, int(num ** 0.5) + 1): # Controllo fino alla radice quadrata di num
        if num % i == 0:
            return False  # Se è divisibile per un numero diverso da 1 e se stesso, non è primo
    return True  # Se non è stato diviso da nessun numero, è primo

for i in range(1, 300):
    if is_prime(i + 1):
        print(i + 1, end=" ")