# 1. Crear un programa que almacene en una lista las materias de esta u otra carrera y que las
# muestre por pantalla. (La lista debe ser predefinida, no debe ser ingresada por el usuario).
# -------------------------------------------------------------------VARIABLES
anios = 3     # max anios de carrera
cua_a = 2     # nº cuatrimetres x año
mat_c = 3     # nº de materias x cuatrimetre
x, y = 0, 0
i,j,k =0,0,0
ncarreras = 4
opc = 0
# --------------------------------------------------------------------TABLAS
# Años, Cuatrimestres, nºMaterias
acm = [[3, 2, 3], [4, 2, 3], [5, 2, 3], [6, 2, 3]]
nom_car = ["TUDW", "CONTADOR", "INGENIERIA", "MEDICINA"]
carreras = [f" {x} Carrera de {nom_car[x]}" for x in range(0, ncarreras)]
materias=[]
# 1=si 0=n0 se dicta curso
# sedicta  = [[["1" for k in range(mat_c)] for j in range(cua_a)] for i in range(anios)]  # PROBADO PARA 3 AÑOS, HAY Q CARGAR MAS LA TABLA
# Materias que no se dictan, 0=No
# sedicta[0][0][2] = "0"
# sedicta[0][0][2] = "0"
# sedicta[1][0][2] = "0"
# sedicta[1][1][2] = "0"
# sedicta[2][1][2] = "0"
# print(sedicta[2][1][2])
# x=input("esperando...")
# Lista de Materias de la Carrera
#

materias = [[["   " for k in range(mat_c)] for j in range(cua_a)] for i in range(anios)]
# def genMatriz(anios, cua_a, mat_c):        
#     materias = [[["   " for k in range(mat_c)] for j in range(cua_a)] for i in range(anios)]
#
def matrizMaterias(cc, a, c, m):
    print("\x1b[1;33m" +
          f"Carrera: {nom_car[cc]} Años={a} Cuatrimestres_año={c} Materias_Cuatrimestre={m}" + "\x1b[0;m")
    for i in range(0, a):                    # año
        for j in range(0, c):                # cuatrimetre
            for k in range(0, m):            # Materias x cuatrimestre
                materias[i][j][k] = "Mat.Cod. A"+str(i)+"C"+str(j)+"/"+str(k)+"|"
                # d=sedicta[i][j]
                #print(i ,j ,k ,d[k])
                # if d[k] == "1":
                # print(d,"si=",k)
                # Carga en Año,Cuatrimeste la materia correspondiente                                     
                #    materias[i][j][k] = "Mat.Cod. A"+str(i)+"C"+str(j)+"/"+str(k)+"|"
                # else:
                #    materias[i][j][k]="-NUll"                 # cuando sedicta="0", se pone NULL
                # print(d,"No=",k)
#
def verMaterias( a, c, m):
    xx="Materia Año Cuat|" * c * m
    print(xx) 
    for i in range(a):
        for j in range(c):
            for k in range(m):                
                #print( materias[i][j][k] , end=" ")    
                print("{:>17}".format( materias[i][j][k]) , end="")
            #print()
        print()    
#
def verCarreras():
    for cx in carreras:
        print(cx)
#
while True:
    print("\x1b[1;33m" + "INGRESE OPCION" + "\x1b[0;m")
    for i in carreras:
        print(i)
    opc = input("Ingrese un Nº de carrera [9=Ver] o [fin]:")
    try:
        opc = int(opc)
    except ValueError:
        break
    if opc == 9:
        verCarreras()
    if opc in range(0, len(carreras)):    # verifica q la carrera exista
        anios = int(acm[opc][0])
        cua_a = int(acm[opc][1])
        mat_c = int(acm[opc][2])        
        materias = [[["   " for k in range(mat_c)] for j in range(cua_a)] for i in range(anios)]
        matrizMaterias(opc,anios, cua_a, mat_c)
        verMaterias(anios, cua_a, mat_c)



