# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 18:33:58 2023

@author: carlo

Un ejemplo de cómo se puede aplicar la propagación de restricciones en la vida diaria es 
en la planificación de un viaje. Supongamos que queremos planificar un viaje de una ciudad 
a otra y necesitamos reservar un vuelo y un hotel. Sin embargo, hay algunas restricciones 
que debemos tener en cuenta, como la disponibilidad de vuelos y habitaciones en el hotel. 
Podemos aplicar la propagación de restricciones para reducir el espacio de búsqueda y 
encontrar una solución factible más rápido, como por ejemplo, eliminando opciones inválidas 
para el vuelo o el hotel basados en la disponibilidad de las fechas deseadas.

propagación de restricciones
"""
class Sudoku:
    def __init__(self, puzzle):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] != 0:
                    self.grid[i][j] = puzzle[i][j]

    def print_grid(self):
        for i in range(9):
            for j in range(9):
                print(self.grid[i][j], end=" ")
                if (j + 1) % 3 == 0 and j != 8:
                    print("|", end=" ")
            print()
            if (i + 1) % 3 == 0 and i != 8:
                print("-" * 21)

    def is_valid(self, row, col, value):
        for i in range(9):
            if self.grid[row][i] == value or self.grid[i][col] == value:
                return False

        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.grid[i][j] == value:
                    return False
        return True

    def propagate(self):
        changed = True
        while changed:
            changed = False
            for i in range(9):
                for j in range(9):
                    if self.grid[i][j] == 0:
                        possible_values = set(range(1, 10))
                        for k in range(9):
                            possible_values.discard(self.grid[i][k])
                            possible_values.discard(self.grid[k][j])
                        row_start = (i // 3) * 3
                        col_start = (j // 3) * 3
                        for row in range(row_start, row_start + 3):
                            for col in range(col_start, col_start + 3):
                                possible_values.discard(self.grid[row][col])
                        if len(possible_values) == 1:
                            self.grid[i][j] = possible_values.pop()
                            changed = True

    def solve(self):
        self.propagate()
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    for k in range(1, 10):
                        if self.is_valid(i, j, k):
                            self.grid[i][j] = k
                            if self.solve():
                                return True
                            self.grid[i][j] = 0
                    return False
        return True

# Ejemplo de uso
puzzle = [[0, 6, 0, 0, 0, 0, 0, 9, 0],
          [0, 0, 0, 0, 5, 0, 0, 0, 0],
          [2, 9, 5, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 0],
          [5, 0, 0, 0, 0, 3, 0, 0, 0],
          [0, 0, 0, 0, 0, 9, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 6],
          [0, 0, 0, 0, 0, 0, 0, 5, 0],
          [0, 0, 0, 0, 0, 0, 4, 0, 0]]

sudoku = Sudoku(puzzle)
print("Puzzle inicial:")
sudoku.print_grid()

if sudoku.solve():
    print("Solución encontrada:")
    sudoku.print_grid()
else:
    print("No se encontró solución.")
