#Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.

#Escribe un programa que incluya una matriz bidimensional (puede ser una matriz pequeña de 3x3) con valores numéricos.

#Implementa una función que realice una búsqueda en la matriz para encontrar un valor específico que definas.

#Muestra un mensaje que indique si el valor se encontró o no, y muestra su posición en la matriz si se encontró.

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición del valor encontrado
    return None  # Retorna None si el valor no se encuentra

# Definir la matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_buscado = int(input("Ingrese el valor a buscar: "))

# Realizar la búsqueda
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar resultados
if posicion:
    print(f"El valor {valor_buscado} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_buscado} no se encuentra en la matriz.")
