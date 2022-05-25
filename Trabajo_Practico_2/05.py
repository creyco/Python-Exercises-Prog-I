# 5. Que dado tres números ingresados por el usuario nos devuelva 
# el promedio.
#--------------------------------------------------------------------
# Se uso una lista, los elementos de la lista incrementan, a decision
# del operador


i=0        # contador
j=0
numero=[]  # lista de numeros ingresados
promedio=0
variable=0
 
print("\x1b[1;33m" + "SACO EL PROMEDIO DE LOS NUMEROS INGRESADOS" + "\x1b[0;m")
while True:
    i +=1
    print(f"Nº {i}: " , end="" )  # end="" permite que no salte de linea
    variable=input("Ingrese un numero [0=Fin]:" )  
    try:
        variable=int(variable)
    except ValueError:
        print("Ingrese un nº > 0 ")    
        i -= 1
        break    
    if variable==0 or variable < 0:
        while j < i - 1:
            promedio = promedio + numero[j]
            #print( j+1  , numero[j] ,  promedio )
            j += 1            
        break        
    numero.append(variable)  # agrego un elemento a la lista

if j > 0:
    promedio = promedio / j
    print(j , "Promedio: " , promedio )
