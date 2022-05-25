# 9. Que el usuario ingrese dos números y muestre cuál de los dos es 
# menor. Considerar el caso en que ambos números son iguales.


print("\x1b[1;33m" + "COMPARO DOS NUMEROS INGRESADOS" + "\x1b[0;m")
a=int(input("Ingrese un Numero   a: "))
b=int(input("Ingrese otro Numero b: "))

if a == b:
    print("Son iguales")
elif a< b:
    print(f" {a} < {b}" )
else:        
    print(f" {a} > {b}" )

