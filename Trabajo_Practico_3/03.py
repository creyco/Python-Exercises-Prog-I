#3. Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3
# frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y
# debajo la misma lista pero sólo con las frutas que añadió el usuario.
#--------------------------------------------------------------------------------------------------
f=6     # Nº Total de elementos del vector
frutas=['banana', 'manzana', 'pera']
print("Hay estas frutas: " , frutas )

def impFru(frutas):    
    print( "Ud.Ingreso: " , frutas[3:f] )
    print( " Ahora Hay: " , frutas[0:f] )

for i in range(3,f):
    x=f-i
    print("\x1b[1;33m" + f"Ingrese {x} futas mas" + "\x1b[0;m" )
    print(f"Nº {i+1}", end=" ")
    fruta=input("Ingrese una Fruta: ")    
    if len(fruta) > 0:
        frutas.insert(i,fruta)
impFru(frutas)