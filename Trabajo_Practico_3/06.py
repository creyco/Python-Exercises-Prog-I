# 6. Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir
# de una lista vacía:
opc=""
menu=[]
opcion=["a","b","c","d"]
menu=["a. Agregar un elemento al final","b. Agregar un elemento al principio","c. Quitar un elemento al final","d. Quitar un elemento al principio"]
lista_vacia=[]

def miLista(opc):
    i = opcion.index(opc)
    #print("Mi Lista=", end=" ")
    print("\x1b[1;33m" + "Mi Lista" + "\x1b[0;m" , end=" ")
    match i:
        case 0:
            lista_vacia.append("Al final")          #Agregar un elemento al final
            print("a)", lista_vacia)
        case 1:            
            lista_vacia.insert(0,"Al principio")    #Agregar un elemento al principio
            print("b" , lista_vacia)    
        case 2:
            if len(lista_vacia) != 0:
                lista_vacia.pop()                       #Quitar un elemento al final
                print("c" , lista_vacia)  
            else:
                print("\x1b[1;33m" + " ERROR " + "\x1b[0;m" )      
        case 3:
            if len(lista_vacia) != 0:
                lista_vacia.pop(0)                      #Quitar un elemento al principio
                print("d" , lista_vacia)    
            else:
                print("\x1b[1;33m" + " ERROR " + "\x1b[0;m" )          
while True:
    for m in menu:
        print(m)
        
    opc=input("Ingrese una opcion [0=Fin]: ").lower()
    if opc in opcion:                        
        miLista(opc)
    else:
        break    
