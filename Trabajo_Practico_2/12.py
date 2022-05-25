# 12. Pedir al usuario que ingrese un día de la semana e imprimir 
# un mensaje si es lunes, otro mensaje diferente si es viernes, 
# otro mensaje diferente si es sábado o domingo. Si el día
# ingresado no es ninguno de esos, imprimir otro mensaje.

dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabago","Domingo"]
j=0
for i in  dias:
    j+=1
    print(j, i)

# INGRESA un numero de la semana
# VALIDA QUE EL NUMERO SEA > 0 y este dentro de los dias
while True:
    d=int(input("Ingrese un Nº de Dia: "))
    if d > 0 and d <= len(dias):
        break

print("Usted eligio el día " , dias[d - 1] )

# La version 12_bis.py cumple la consigna