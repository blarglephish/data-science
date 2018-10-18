"""
@File = linear_algebra.py
@Author = Adam Betz
@Date = 10/17/2018

A bunch of functions that are useful for doing Linear Algebra operations:
 - Vector Algebra
 - Matrix Operations
"""

import math
from functools import reduce

"""
Vector Algebra
"""
def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    """sums all corresponding elements"""
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

    # The Above code could also have been added using 'reduce' (functools):
    # return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the ith elements of the input vector"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(w, v))

def sum_of_squares(v):
    """v1 * v1 + ... + v_n * v_n"""
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return math.sqrt(squared_distance(v, w))

    # Possibly clearer if we write this as (the equivalent):
    # return magnitude(vector_subtract(v, w))

"""
Matrix Operations

NOTE: We will represent matrices as 'lists of lists', with each inner list having the same size
and representing a row of the matrix. If A is a matrix, then A[i][j] is the element in the ith row
and the jth column.

For Example: 
A = [[1, 2, 3], # A has 2 rows and 3 columns
     [4, 5, 6]]
"""
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0    # number of elements in first row
    return num_rows, num_cols

def get_row(A, i):
    return A[i]                         # A[i] is already in the ith row

def get_column(A, j):
    return [A_i[j]                      # jth element of row A_i
            for A_i in A]               # for each row A_i

def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix
    whose (i,j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)             # given i, create a list
             for j in range(num_cols)]  #   [entry_fn(i, 0), ...]
            for i in range(num_rows)]   # create one list for each i

def is_diagonal(i, j):
    """1's on the diagonal, 0's everywhere else"""
    return 1 if i == j else 0

# Using the above as an entry_fn, we can call make_matrix to create an identity matrix:
# identity_matrix = make_matrix(5, 5, is_diagonal)  # creates a 5 x 5 identity matrix
