# 4. Que dada la base y altura de un triángulo nos calcule su área.

# ESTA VERSION SOLO ADMITE ENTEROS

def es_entero(variable):
    try:
        int(variable)
        return True
    except:
        return False

def area( base, altura):
    return (base * altura)

while True:  
    try:
        base=int(input("Ingrese la base del triangulo: "))
    except ValueError:
        print("\x1b[1;33m" + "Debe ingresar un numero > 0" + "\x1b[0;m") 
        continue
    if base < 0:        
        print("\x1b[1;33m" + "Debe ingresar un numero positivo"+ "\x1b[0;m")        
        continue
    else:
        if es_entero(base):
            break

while True:  
    try:
        altura=int(input("Ingres la Altura del triangulo: "))
    except ValueError:
        print("\x1b[1;33m" + "Debe ingresar un numero > 0" + "\x1b[0;m") 
        continue
    if altura < 0:        
        print("\x1b[1;33m" + "Debe ingresar un numero positivo"+ "\x1b[0;m")        
        continue
    else:
        if es_entero(altura):
            break

print(area(base,altura) , "<Unidades> al cuadrado")

