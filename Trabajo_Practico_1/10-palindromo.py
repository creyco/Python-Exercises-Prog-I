#!/usr/bin/env python
# coding: utf-8
# 10-palindromo.py


# Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al
# derecho que al revés. Por ejemplo: rayar, kayak, somos.

texto=input("Ingrese un texto: ")

texto_inv=texto[::-1]

if texto==texto_inv:
    print("Es palindromo " , texto_inv)
else:
      print("No es palindromo")

