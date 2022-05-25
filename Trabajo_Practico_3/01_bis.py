# 1. Crear un programa que almacene en una lista las materias de esta u otra 
# carrera y que las muestre por pantalla. (La lista debe ser predefinida, 
# no debe ser ingresada por el usuario).

carreras=["01 TDW",
          "02 ING", 
          "03 LIC",
          "04 CPN"]

materias=[   
    [["01 Introd.Informat","02 Programacion I      ","                  "], 
     ["03 Diseño Gráfico ","04 Arq.Computadoras    ","05 Programación II"]],
    [["06 Sistemas Opert ","07 Intr.Desarrollo Web ","08 Bases de Datos "],
     ["09 Redes de Datos ","10 Programación III    ","                  "]],
    [["11 Ing. Software  ","12 Des.Aplicacones Web ","                  "],
     ["13 Des Sis Móviles","14 Multimedia v Juegos ","                  "]]]

print("ELIJA LA CARRERA QUE DESEA CONSULTAR")
print("\n".join(map(str,carreras)) + "\n")
while True:
    try:
        c=int(input("Indique Nº Carrera 0=FIN: "))        
    except ValueError:        
        print("\x1b[1;33m" + "Debe ingresar un numero " + "\x1b[0;m") 
        continue
    if c == 0:
        break
    elif c > len(carreras) or c < 0: 
        print("\x1b[1;33m" + "Ingresar un numero en el rango " + "\x1b[0;m") 
        continue    
    else:
        print(carreras[c - 1])          
        c=0     # LO PONGO EN CERO X Q NO TENGO MAS LISTAS DE MATERIAS
        for i in range(len(materias) ):            
            print(materias[i])
        print()
