#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
     if len(matrix) > 0:
          n = len(matrix)
          for i in range(n):
               print()
               for j in range(len(matrix[i])):
                    print("{:d}".format(matrix[i][j]), end=" ")
               print('')
     else:
          print()
                    
