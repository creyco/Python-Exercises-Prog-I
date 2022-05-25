# 15. Que solicite al usuario una letra y, si es una vocal, muestre el 
# mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un 
# carácter. Si ingresa un string de más de un carácter, 
# informarle que no se puede procesar el dato.


print("\x1b[1;33m" + "VERIFICO SI INGRESA UNA VOCAL" + "\x1b[0;m")
while True:
    letra=input("Ingrese un caracter [0=Fin]: ")
    if letra.lower() in "aeiou" and len(letra) != 0:
        print(f" {letra} Es una vocal")        
    elif letra=="0":
        break
    elif len(letra) == 1:
            print(" No es una vocal")     
            continue          
    elif len(letra) > 1:   
            print("Ingrese Solo un caracter")            
            continue
    else:
        break