# 13. Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos
# A y B de acuerdo al sexo y el nombre. El grupo A está formado 
# por las mujeres con un  nombre anterior a la M y los hombres con un 
# nombre posterior a la N y el grupo B por el resto. Escribir un programa 
# que pregunte al usuario su nombre y sexo y muestre por pantalla
# el grupo que le corresponde.

# grupo_A_F=[a-n]  # formado por las mujeres con un nombre anterior a la M
# grupo_A_M=[m-z] # y los hombres con nombre posterior a la N
# grupo_B_F=[m-z]  # Formado porel reso de personas o sea, 
# grupo_B_M=[a-n]  # mujeres con un nombre posterior a la M inclusive
                 # y los hombres con nombre anterior a la N inclusive


from ast import match_case
import re

def showGrupo(nombre, sexo, grupo):
    genero=["Femenino", "Masculino"]
    print(f"Nombre: {nombre.capitalize()} Sexo: {sexo} Grupo {grupo}")

nombre=input("Ingrese Nombre:" )
sexo=input("Sexo F|M: ").upper()   

match sexo:
        case "F":
            if re.findall("^[a-n|A-N]", nombre) :             
                showGrupo(nombre, sexo, "A")
            elif re.findall("^[m-z|M-Z]", nombre):
                showGrupo(nombre, sexo, "B")
        case "M":
            if re.findall("^[m-z|M-Z]", nombre):    
                showGrupo(nombre, sexo, "A")
            elif re.findall("^[a-n|A-N]", nombre) :
                showGrupo(nombre, sexo, "B")

