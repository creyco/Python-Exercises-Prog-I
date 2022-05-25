# 8. Pregunte al usuario su edad y muestre por pantalla 
# si es mayor de edad o no.

print("\x1b[1;33m" + "DETERMINO SI LA EDAD INGRESADA ES DE UNA MAYOR O MENOR" + "\x1b[0;m")

edad = int(input("Ingrese su edad: "))
print( ("MENOR" if edad < 18 else "MAYOR") + " de edad")
