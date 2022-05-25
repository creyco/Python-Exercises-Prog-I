#16. Que imprima el siguiente patrón:
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

print("\x1b[1;33m" + "IMPRIMO SECUENCIA INDICADA" + "\x1b[0;m")
renglon=""
for i in range(5 , 0, -1):
    for j in range(i , 0 , -1):
        renglon=renglon + str(j) + " "
    print(renglon)   
    renglon="" 