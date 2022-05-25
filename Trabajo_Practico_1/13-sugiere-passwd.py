#!/usr/bin/env python
# coding: utf-8
# 13-sugierepasswd.py

nombre=input("Ingrese su Nombre: ")
apellido=input("Ingrese su Apellido: ")

while True:
    anio=input("Ingrese su año de Nacimiento: ")
    if len(anio) !=4:
        print("año inaceptable")
    else:
       break;  
    
anio_inv=anio[::-1]
               
print("Nombre:", nombre.capitalize() , 
      "Apellido:", apellido.capitalize(), 
      "Contraseña: ", nombre[0:1] + apellido[0:1] + anio_inv)

