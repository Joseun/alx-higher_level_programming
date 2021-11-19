#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
     n = len(matrix)
     for i in range(n):
          print()
          for j in range(n):
               print("{:d}".format(matrix[i][j]), end=" ")
          print()
                    
