# 17. Que muestre todos los números primos entre 0 y 100 e imprima 
# cuántos números primos hay.

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print("\x1b[1;33m" + "MUESTRO LOS Nº PRIMOS ENTRE 0 Y 100" + "\x1b[0;m")
hasta=100
contador = 0
primos="" 
n=0
for n in range(0 , hasta + 1):
    if es_primo(n):
        primos = primos + str(n) + " "
        contador += 1

print(f"{contador} Numeros primos encontrados")
print(primos)
