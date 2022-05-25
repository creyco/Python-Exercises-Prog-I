#!/usr/bin/env python
# coding: utf-8
# 12-fecha-valido.py

# string[inicio: fin: paso]    
def validar_fecha(dia, mes, anio):
    dias_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if anio%4==0 and (anio%100 != 0 or anio%400==0):
        dias_mes[2] = 29
    return (1 <= mes <= 12 and 1 <= dia <= dias_mes[mes])

fecha=input("Ingrese Fecha dd/mm/aaaa: ")

print("Dia:" , fecha[0:2] ,
      "Mes:" , fecha[3:5] ,   
      "Año:" , fecha[6:10])    

# validar
dia=int(fecha[0:2])
mes=int(fecha[3:5])  
anio=int(fecha[6:10])    

if validar_fecha(dia, mes, anio): 
    print("Fecha Correcta.")
else: 
    print("Fecha Incorrecta.!")
    

