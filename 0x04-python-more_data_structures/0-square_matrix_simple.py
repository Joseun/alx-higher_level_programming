#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
'''using list comprehension to square contatents of a matrix'''
    if len(matrix) > 0:
        new_matrix = [[i*i for i in j] for j in matrix]
        return new_matrix
