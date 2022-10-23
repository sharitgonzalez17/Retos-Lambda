# Segundo Función lambda que clasifique números mayores a 10 en una lista
numeros = [1,2,3,8,7,10,80,100]
clasificar3 = lambda numero : numero>10
for numero in numeros:
    print(clasificar3(numero))