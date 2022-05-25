 #11. Que solicite al usuario ingresar una frase. 
 # Luego, que imprima la cantidad de vocales que se encuentran 
 # en dicha frase.

vocales=["a","e","i","o","u"]

def es_vocal(a):
    for i in vocales:
        if a == i:
            return True
    return False
            
print("\x1b[1;33m" + "DETERMINO LAs VOCALES DE LA FRASE INGRESADA" + "\x1b[0;m")
texto=input("ingrese una frase: ")
x=0
for i in texto:
    if es_vocal(i.lower()):
       x += 1 
       print(i)

print(f"Hay {x} vocales")      