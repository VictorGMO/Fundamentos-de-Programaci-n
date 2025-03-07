#Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.

#Escribe un programa que incluya una matriz bidimensional con valores numéricos (puede ser una matriz pequeña de 3x3).

#Implementa una función que ordene una fila específica de la matriz en orden ascendente utilizando un algoritmo de ordenación de tu elección (por ejemplo, Bubble Sort o QuickSort).

#Muestra la matriz original y la matriz con la fila ordenada.

def bubble_sort(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio de valores
    return fila


# Definir la matriz 3x3
matriz = [
    [9, 2, 7],
    [4, 5, 1],
    [3, 8, 6]
]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Pedir al usuario la fila a ordenar
fila_index = int(input("Ingrese el índice de la fila a ordenar (0-2): "))

# Ordenar la fila elegida
if 0 <= fila_index < len(matriz):
    matriz[fila_index] = bubble_sort(matriz[fila_index])

    # Mostrar la matriz con la fila ordenada
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
else:
    print("Índice de fila fuera de rango.")
