# 2. Que reciba un número entero positivo y una potencia a elevar y que 
# nos devuelva el resultado.

def potenciaNumero( a , b ):
    c=a**b
    print(f"una base '{a}' elevado a exponente '{b}' da '{c}' ")

print("Potencia de un número")
a = int(input("Ingrese base: "))
b = int(input("Ingrese exponente: "))

#print(f" {a} aqui {b} ")
potenciaNumero(a, b)