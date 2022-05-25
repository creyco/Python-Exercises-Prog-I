# 3. Que nos calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA
# a aplicar, y devolver el total de la factura. Si se invoca
# la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%

def calculaIVA(total , iva):   
    impuesto = total * (1 + iva / 100)    
    return impuesto

while True:             # Valido el input
    try:
        total=float(input("Ingrese el Total de la Factura [0=Fin]: "))
    except ValueError:
        print("\x1b[1;33m" + "Debe ingresar un numero" + "\x1b[0;m") 
        continue
    if total < 0:        
        print("Ingrese un importe positivo")
        continue
    else:
        break

while True: # Valido el input
    try:
        iva=float(input("Ingrese el IVA <o enter> Si es el %21: "))        
    except ValueError:        
        iva=21.0
        break
    if iva < 0:        
        print("\x1b[1;33m" + "Debe ingresar un numero positivo"+ "\x1b[0;m")        
        continue
    else:
        break

print (calculaIVA( total , iva ))