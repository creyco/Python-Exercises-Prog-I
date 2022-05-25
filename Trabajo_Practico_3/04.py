#4. Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”], realizar lo siguiente: 
# a. Imprimir la cantidad de elementos que tiene la lista.
# b. Imprimir el primer y último elemento.
# c. Imprimir el resto.
# d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en la lista. 
#    Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
# e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de la lista. 
#    Quitar el elemento correspondiente de esa posición.
# f.Imprimir la lista en orden inverso.
# g. Vaciar la lista.

paises = ['Argentina','Brasil', 'Bolivia','Paraguay','Venezuela']
print("a) Paises de la lista " , paises , end=" ")
#(a)
l=len(paises)
print(" / nº de elementos ", l )

#(b)
print("b) Orden 1º ", paises[0] ,"|Ultimo" , paises[len(paises)-1]," de la lista")

#(c)
print("c) Resto de paises Func.slice" , end=" ")
print(paises[1:l-1])

#(d)
p=input("d) Ingrese un nombre de Pais de la lista: ")
#p="Bolivia"
if len(p) != 0:
    print(f"{p} Elemento Nº " , paises.index(p) , "de la lista" )
else:
    print("No existe el nombre ingresado")    

#(e)
for i in range(0,l):
    print(f"Nº {i}" , paises[i])  

k=int(input(f"e) Ingrese un nº de Pais a eliminar de la lista < {l}: "))
#k=2
if k < 0 or k > l:
    print("Fuera de rango")
else:
    print(f"Eliminando elemento nº {k}")
    del paises[k]
print("Nueva lista: " , paises)

#(f)
print("f) Func.Reversed " , end=" ")
for pais in reversed(paises):
    print(pais , end = " ")
print()    
# Otra opcion func. reverse()
inv_pais=paises
inv_pais.reverse()
print("   Func.reverse ", inv_pais)

#(g)
paises.clear()
print ("g) Vaciar lista paises", paises)
