#5. Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el usuario ingrese la palabra “fin” el programa 
# deberá concluir con la carga de datos. Cada uno de los números ingresados por el usuario deberá ser almacenado en una lista. A continuación, 
# realice las siguientes tareas:

numero=[]  # crea lista de numeros a ingresar
#numero=[11,7,12,6,7,11,22,5,7,2,22]
variable ,resultado = 0,1
i,par,impar = 0,0,0
 
print("\x1b[1;33m" + "INGRESE VARIOS NUMEROS" + "\x1b[0;m")
while True:
    i +=1
    print(f"Nº {i}: " , end="" )  # end="" permite que no salte de linea
    variable=input("Ingrese un numero o escriba [fin]:" )  
    try:
        variable=int(variable)
    except ValueError:
        if variable.lower() == "fin":
            break
    if variable <= 0: 
        print("Ingrese un nº > 0 ")    
        i -= 1
        continue
    else:
        numero.append(variable)  # agrego un elemento a la lista

print("\x1b[1;33m" +"Lista Ingresada: " + "\x1b[0;m", numero)

# a)b)c) Determinar el máximo el preMax, el min
# uso funciones copy() sort() len()
ord=numero.copy()
ord.sort()
print("a)     Maximo: ", ord[len(ord)-1])
print("b) Pre-Maximo: ", ord[len(ord)-2])
print("c)     Minimo: ", ord[0]) 

# d. Calcular la multiplicación de todos los números de la lista.
for i in range(0, len(ord)):
    resultado = resultado * ord[i] 
print(f"d) Multiplicar los Nºs: {resultado:,}") 

# e. Contar los valores pares e impares.
print("e)" , end=" ")
for i in range(0, len(ord)):
    print (ord[i] , end=" ")
    if (ord[i] % 2 != 0 ):
        impar += 1        
    else:
        par += 1        
print(f"| Pares: {par} | Impares: {impar}" )

# f. Remover los elementos repetido
remover=set(numero) 
temp=list(remover)
temp.sort()
print("f) Sin números repetidos: " , temp ) 
