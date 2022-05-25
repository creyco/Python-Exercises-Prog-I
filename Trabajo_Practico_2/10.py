#10. Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
# a. Todos los números impares desde 1 hasta ese número separados por comas.
# b. La cuenta atrás desde ese número hasta cero separados por comas.
# c. Que indique si es primo o no.
# d. Por último, su factorial.
import math


numeros=[]
def miFact( n):
    for i in range(n , 1, -1):
        n = n * (i-1)
    return n    

def es_primo(n):
    if n <= 1:
        return False     # si es negativo
    for i in range(2 , n): # recorro los numeros hasta n
        print(i, n  )
        if n % i == 0:   # si funcion parte entera del numero es cero =>NO PRIMO
            return False
    return True # Es PRIMO

def es_impar(n):
    #print(n)
    return (True if (-1)**n < 0 else False)
   
# INGRESA un numero 
# VALIDA QUE EL NUMERO SEA > 0
print("\x1b[1;33m" + "FUNCIONES: LOS IMPARES, LISTA INVERTIDA, ES PRIMO?, FACTORIAL n!" + "\x1b[0;m")
while True:
    n=input("Ingrese un Nº positivo:")
    if n.isnumeric():
        n=int(n)
        break

# IMPARES
# Analiza si los numeros hasta n son impares y arma una lista de ellos  
for i in range(0, n  + 1):
      if es_impar(i):      
        numeros.append(i)
# imprime los impares encontrados     
print("IMPARES:" , numeros)    


#Imprime lista invertida
lista_inv=[]
for i in range(n , 0, -1):
    lista_inv.append(i)
print( f"Lista Invertida {lista_inv} ")

# PRIMOS
# Analiza si el Nº es primo
if es_primo(n):
    print(f" {n} ES PRIMO")
else:
    print(f"{n} NO ES PRIMO")    

# Factorial de un numero
print(f"Funcion MATH n!  {math.factorial(n)} ") # Pruebo con la funcipon math
print(f"miFactorial  {n}! {miFact(n)}" ) # applico miFact()

 