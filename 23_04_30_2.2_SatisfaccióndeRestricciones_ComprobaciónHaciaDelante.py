# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 18:18:38 2023

@author: carlo

Un ejemplo de aplicación de la comprobación hacia delante podría ser la 
planificación de una fiesta de cumpleaños. Supongamos que se sabe que se necesitan 
20 cupcakes y se cuenta con una variedad de ingredientes limitados, como harina, huevos, 
mantequilla y azúcar. Las restricciones podrían incluir, por ejemplo, que se necesitan dos 
huevos por cada 6 cupcakes y que no se pueden utilizar más de 4 tazas de azúcar en total. 
Utilizando la comprobación hacia delante, se pueden ir descartando las opciones 
inviables y se puede encontrar la combinación de ingredientes que permita hacer los 
20 cupcakes.

comprobación hacia delante
"""
class NQueensFC:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.col_free = [True] * n
        self.up_free = [True] * (2 * n - 1)
        self.down_free = [True] * (2 * n - 1)

    def print_board(self):
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if self.board[row] == col:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    def solve(self, row):
        if row == self.n:
            self.print_board()
            return True
        else:
            for col in range(self.n):
                if self.col_free[col] and self.up_free[row + col] and self.down_free[row - col + self.n - 1]:
                    self.board[row] = col
                    self.col_free[col] = False
                    self.up_free[row + col] = False
                    self.down_free[row - col + self.n - 1] = False
                    if self.solve(row + 1):
                        return True
                    self.col_free[col] = True
                    self.up_free[row + col] = True
                    self.down_free[row - col + self.n - 1] = True
            return False

n_queens = NQueensFC(8)
n_queens.solve(0)
print("Solución encontrada para el problema de las {} reinas.".format(n_queens.n))

"""
En este ejemplo, la función solve utiliza la Comprobación Hacia Delante para encontrar 
la solución del problema de las n-reinas. Se utiliza la técnica de backtrack (retroceso) 
para explorar las posibles soluciones y se utiliza la Comprobación Hacia Delante para 
descartar las opciones inviable
"""