 # 4. Que dada la base y altura de un triángulo nos calcule su área.

# ADMINTE VARIABLES DE PUNTO FLOTANTE

def es_flotante(variable):
    try:
        variable=float(variable) 
        if variable < 0:
            print("\x1b[1;33m" + "Debe ingresar un numero > 0" + "\x1b[0;m")       
        return (True if variable > 0 else False)                     
    except ValueError:
        print("\x1b[1;33m" + "Debe ingresar un numero" + "\x1b[0;m") 
        return False    

   
def area( base, altura):
    return (base * altura)

while True:  
    base=input("Ingrese la BASE del triangulo: ")
    if es_flotante(base):
       base=float(base)
       break

while True:  
    altura=input("Ingrese la ALTURA del triangulo: ")
    if es_flotante(altura):
        altura=float(altura)
        break

#print (type(base) , type(altura))
print(area(base,altura) , "<Unidades> al cuadrado")

