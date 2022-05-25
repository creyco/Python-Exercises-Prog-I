# 7. Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings
# con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al usuario:
# a. Agregar nuevas tareas pendientes.
# b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar de la lista de pendientes a la de terminadas.
# Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas listas.

# Precargada J A R D I N E R I A como ejemplo
PEND = ["Plantar","Regar","Abonar","Podar","Desmalezar"]
TERM = ["Comprar"]
menu = ["1. Agregar una tarea Pendiente", "2. Terminar una Tarea Pendiente"]

def imp_Tareas(x, y, z):   # Imprimo ambas listas a la par uso comando format()
    print("{:<3} {:<20} {:<20}".format(x, y, z))

def status():
    n = len(PEND)
    l = len(TERM)
    print("\x1b[1;33m" + "    T O D A S - L A S - T A R E A S " + "\x1b[0;m")    
    print("{:<3} {:<20} {:<20}".format("Nº", "PENDIENTES", "TERMINADAS"))
    if n == l:          # listas de igual tamaño
        for n1, n2 in zip(PEND, TERM):
            i = PEND.index(n1)
            j = TERM.index(n2)
            imp_Tareas(i, PEND[i], TERM[j])
    elif l > n:
        for ll in range(l):
            if ll < n:
                imp_Tareas(ll, PEND[ll], TERM[ll])
                #print(f"{ll}   " , PEND[ll] , "\t" , TERM[ll])
            else:
                imp_Tareas(ll, "  ", TERM[ll])
                #print(f"{ll}   " , "  ", "\t", TERM[ll])
    else:   # n > l
        for nn in range(n):
            if nn < l:
                imp_Tareas(nn, PEND[nn], TERM[nn])
                #print(f"{nn}   " , PEND[nn] ,"\t", TERM[nn])
            else:
                imp_Tareas(nn, PEND[nn], "  ")
                #print(f"{nn}" ,PEND[nn],"\t", "  ")
#
def ingresaTarea(opc):
    status()
    if opc == 1:     # tarea PEND
        # Agregar nuevas tareas pendientes
        PEND.append(input("Ingrese una nueva Tarea Pendiente: "))
        status()
    elif opc == 2:      # Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar
        while True:     # de la lista de pendientes a la de terminadas
            xx = input("Ingrese una Tarea a terminar: ")
            if xx in PEND:
                PEND.remove(xx)
                TERM.append(xx)
                status()
                break
            else:
                print("\x1b[1;33m" + "Debe ingresar una tarea PENDIENTE existente"+ "\x1b[0;m" )
                break
                # luego buscar si esta en las PEND
                # Si se encuenta eliminar de la lista
                # si no se encuentra, decir que no esta en PEND
#
opc = ""
while True:
    print("\x1b[1;33m" + "INGRESE OPCION" + "\x1b[0;m")
    for i in menu:
        print(i)
    opc = input("Ingrese una opcion [0=ver] [fin]:")
    try:
        opc = int(opc)
    except ValueError:
        break
    if opc == 0:
        status()
    if opc == 1 or opc == 2:  # tarea oendiente o a terminar
        ingresaTarea(opc)
#