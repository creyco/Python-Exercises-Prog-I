#2. Pedir al usuario que ingrese 5 números para luego almacenarlos 
# en una lista y ordenarlos. Imprimir por pantalla el resultado.

i=0        # contador
j=0
numero=[]  # lista de numeros ingresados
variable=0 
print("\x1b[1;33m" + "ORDENO LOS NUMEROS INGRESADOS" + "\x1b[0;m")
while True:
    i +=1        
    print(f"Nº {i}: " , end="" )  # end="" permite que no salte de linea
    variable=input("Ingrese Hasta 5 números [0=Fin]:" )  
    try:
        variable=int(variable)
    except ValueError:      
        break
    if variable==0:                         
        break    
    else:
        j += 1   
    numero.append(variable)  # agrego un elemento a la lista    

if j > 0:
    numero.sort()
    print("Lista Ordenada: " , numero)