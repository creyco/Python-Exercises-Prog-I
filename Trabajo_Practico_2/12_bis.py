# 12. Pedir al usuario que ingrese un día de la semana e imprimir 
# un mensaje si es lunes, otro mensaje diferente si es viernes, 
# otro mensaje diferente si es sábado o domingo. Si el día
# ingresado no es ninguno de esos, imprimir otro mensaje.

dias=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]

# INGRESA un dias de la semana
# Valida has que sea correcta
print("\x1b[1;33m" + "DETERMINO SI EL DIA DE LA SEMANA CORRESPONDE" + "\x1b[0;m")
while True:
    d=input("Ingrese un DIA de la semana: ")
    if dias.count( d.lower() ) > 0 :    # Verifica si ingreso un dia contenido en la lista
        break
    else:
        print("debe ingresar una dia de la semana")

print("Ingreso el dia " , d.upper())  # Imprime el dia en mayusculas