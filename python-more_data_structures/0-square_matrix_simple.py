#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Crear una nueva matriz vacía del mismo tamaño que la matriz de entrada
    result = [[0] * len(row) for row in matrix]

    # Iterar sobre cada elemento de la matriz de entrada
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Calcular el cuadrado del valor actual y asignarlo a la nueva matriz
            result[i][j] = matrix[i][j] ** 2

    # Devolver la nueva matriz
    return result
