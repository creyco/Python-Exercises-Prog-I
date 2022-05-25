# 14. Que pida un año y que escriba si es bisiesto o no. Les recordamos que 
# los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no 
# lo son, aunque los múltiplos de 400 sí. Algunos ejemplos de posibles 
# respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 
# 1800,1900,2100,2200 no son bisiesto.

def esBisiesto(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

while True:
    anio=input("Ingrese un año [0=Fin]: ")
    try:
        anio=int(anio)
    except ValueError:
        print("\x1b[1;33m" + "Debe ingresar un numero" + "\x1b[0;m") 
        continue  
    if anio == 0 or anio < 0 :
        break
    elif esBisiesto(anio):
        print(f"{anio} Si Es bisiesto")
    else:
        print(f"{anio} No Es bisiesto")  
