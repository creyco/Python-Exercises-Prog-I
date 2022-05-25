# 1. Que al pasarle una cadena <nombre> nos muestre por pantalla el 
# saludo ¡Hola <nombre>!.

def mSaludo( n ):     # defino funcion
    print( "Hola" , n )                # imprimo nombre

nombre = input("Ingrese un nombre: ") # solicito un nombre
mSaludo( nombre.capitalize() )        # Funcion mSaludos 