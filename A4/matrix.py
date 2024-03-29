#--------------------------
# Noah Nichols (160554770)
# CP460 (Fall 2019)
# Assignment 4
#--------------------------

import math
import string
import mod

#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  checks if the given input is a valid vector
#               A valid vector is a list in which all elements are integers
#               An empty list is a valid vector
# Errors:       None
#-----------------------------------------------------------
def is_vector(A):
    # your code here
    if(type(A) is not list):
        return False
    else:
        for i in range(len(A)):
            if(type(A[i]) is not int):
                return False

    return True
#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  checks if the given input is a valid matrix
#               A matrix is a list in which all elements are valid vectors of equal size
#               Any valid vector is also a valid matrix
# Errors:       None
#-----------------------------------------------------------
def is_matrix(A):
    # your code here
    if(type(A) is not list):
        return 'Error'
    for x in range(len(A)):
        if(len(x)!= len(A)):
            return False
    return True

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       None
# Description:  Prints a given matrix, each row on a separate line
# Errors:       If A not a matrix --> print 'Error (print_matrix): Invalid input'
#-----------------------------------------------------------
def print_matrix(A):
    # your code here
    if(is_matrix(A)):
        for x in A:
            print(x)
    else:
        return 'Error (print_matrix): Invalid input'
    return

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       number of rows (int)
# Description:  Returns number of rows in a given matrix
# Examples:     [5,3,2] --> 1
#               [] --> 0
#               [[1,2],[3,4],[5,6]] --> 3
# Errors:       If A not a matrix -->
#                   return 'Error (get_rowCount): invalid input'
#-----------------------------------------------------------
def get_rowCount(A):
    # your code here
    if(is_matrix(A) != True):
        return 'Error (get_rowCount): invalid input'
    else:
        return len(A[0])

    return

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       number of columns (int)
# Description:  Returns number of columns in a given matrix
# Examples:     [5,3,2] --> 3
#               [] --> 0
#               [[1,2],[3,4],[5,6]] --> 2
# Errors:       If A not a matrix -->
#                   return 'Error (get_columnCount): invalid input'
#-----------------------------------------------------------
def get_columnCount(A):
    # your code here
    if(is_matrix(A) != True):
        return 'Error (get_columnCount): invalid input'
    
    x = A[0]
    if(type(x) is not list):
        return len(A)
    else:
        return len(x)
    return

#-----------------------------------------------------------
# Parameters:   A (a matrix)
# Return:       [number of rows (int), number of columns(int)]
# Description:  Returns number size of matrix [rxc]
# Examples:     [5,3,2] --> [1,3]
#               [] --> [0,0]
#               [[1,2],[3,4],[5,6]] --> [3,2]
# Errors:       If A not a matrix -->
#                   return 'Error (get_size): invalid input'
#-----------------------------------------------------------
def get_size(A):
    col = get_columnCount(A)
    row = get_rowCount(A)
    

    return [row,col]

#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  Checks if given input is a valid square matrix
# Examples:     [] --> True
#               [10] --> True
#               [[1,2],[3,4]] --> True
#               [[1,2],[3,4],[5,6]] --> False
# Errors:       None
#-----------------------------------------------------------
def is_square(A):
    # your code here
    col = get_columnCount(A)
    row = get_rowCount(A)

    return col==row

#-----------------------------------------------------------
# Parameters:   A (a matrix)
#               i (row number)
# Return:       row (list)
# Description:  Returns the ith row of given matrix
# Examples:     ([],0) --> Error
#               ([10],0) --> [10]
#               ([[1,2],[3,4]],0) --> [1,2]
# Errors:       If given matrix is empty or not a valid matrix -->
#                   return 'Error (get_row): invalid input matrix'
#               If i is outside the range [0,#rows -1] -->
#                   return 'Error (get_row): invalid row number'
#-----------------------------------------------------------
def get_row(A,i):
    # your code here
    if(is_matrix(A)!= True):
        return 'Error (get_row): invalid row number'
    elif(len(A) < 1):
        return 'Error (get_row): invalid input number'
    return A[i]

#-----------------------------------------------------------
# Parameters:   A (a matrix)
#               j (column number)
# Return:       column (list)
# Description:  Returns the jth column of given matrix
# Examples:     ([],0) --> Error
#               ([10],0) --> [10]
#               ([[1], [2]],0) --> [[1], [2]]
#               ([[1,2],[3,4]],1) --> [2,4]
# Errors:       If given matrix is empty or not a valid matrix -->
#                   return 'Error (get_column): invalid input matrix'
#               If i is outside the range [0,#rows -1] -->
#                   return 'Error (get_column): invalid column number'
#-----------------------------------------------------------
def get_column(A,j):
    # your code here
    if(is_matrix(A) != True):
        return 'Error (get_column): invalid input matrix'
    elif(len(A) < 1):
        return 'Error (get_column): invalid input matrix'
    elif(len(A[0]) < j or j < 0):
        return 'Error (get_column): invalid column number'
    col = []

    for x in range(A):
        col.append(x[j])
    return col

#-----------------------------------------------------------
# Parameters:   A (a matrix)
#               i (row number)
#               j (column number)
# Return:       element
# Description:  Returns element (i,j) of the given matrix
# Errors:       If given matrix is empty or not a valid matrix -->
#                   return 'Error (get_element): invalid input matrix'
#               If i or j is outside matrix range -->
#                   return 'Error (get_element): invalid element position'
#-----------------------------------------------------------
def get_element(A,i,j):
    # your code here
    if(is_matrix(A) != True):
        return 'Error (get_column): invalid input matrix'
    elif(len(A) < 1):
        return 'Error (get_column): invalid input matrix'
    elif(len(A[0]) < j or len(A) < i or j < 0 or i < 0):
        return 'Error (get_column): invalid element position'

    x = A[i]

    
    return x[j]

#-----------------------------------------------------------
# Parameters:   r: #rows (int)
#               c: #columns (int)
#               pad (int)
# Return:       matrix
# Description:  Create an empty matrix of size r x c
#               All elements are initialized to integer pad
# Error:        r and c should be positive integers
#               (except the following which is valid 0x0 --> [])
#                   return 'Error (new_matrix): invalid size'
#               pad should be an integer
#                   return 'Error (new_matrix): invalid pad'
#-----------------------------------------------------------
def new_matrix(r,c,pad):
    # your code here
    matrix = [[pad*c]*r] 
    return matrix

#-----------------------------------------------------------
# Parameters:   size (int)
# Return:       square matrix (identity matrix)
# Description:  returns the identity matrix of size: [size x size]
# Examples:     0 --> Error
#               1 --> [1]
#               2 --> [[1,0],[0,1]]
# Errors        size should be a positive integer
#                   return 'Error (get_I): invalid size'
#-----------------------------------------------------------
def get_I(size):
    # your code here
    if(size <1):
        return 'Error (get_I): invalid size'
    matrix = [[0 * size]*size]
    for i in range(size):
        for j in range(size):
            if(j==1):
                matrix[j][i] = 1
    
    return matrix

#-----------------------------------------------------------
# Parameters:   A (any input)
# Return:       True/False
# Description:  Checks if given input is a valid identity matrix
#-----------------------------------------------------------
def is_identity(A):
    # your code here
    if(type(A) is not list):
        return False
    if(len(A[0]) < 1):
        return False
    for i in range(len(A)):
        for j in range(len(A[i])):
            if(i != j and A[i][j] != 0):
                return False
            
    return True

#-----------------------------------------------------------
# Parameters:   c (int)
#               A (matrix)
# Return:       a new matrix which is the result of cA
# Description:  Performs scalar multiplication of constant c with matrix A
# Errors:       if A is empty or not a valid matrix or c is not an inger:
#                   return 'Error(scalar_mul): invalid input'
#-----------------------------------------------------------
def scalar_mul(c,A):
    # your code here
    if(type(A) is not list or len(A) <1):
        return 'Error(scalar_mul): invalid input'
    elif(type(c) is not int):
        return 'Error(scalar_mul): invalid input'

    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= c
    return A

#-----------------------------------------------------------
# Parameters:   A (matrix)
#               B (matrix)
# Return:       a new matrix which is the result of AxB
# Description:  Performs cross multiplication of matrix A and matrix B
# Errors:       if eithr A or B or both is empty matrix nor not a valid matrix
#                   return 'Error(mul): invalid input'
#               if size mismatch:
#                   return 'Error(mul): size mismatch'
#-----------------------------------------------------------
def mul(A,B):
    # your code here
    if(is_matrix(A) != True or is_matrix(B) != True):
        return 'Error(mul): invalid input'
    colA = max(A[i] for i in range(len(A)))
    colB = max(B[i] for i in range(len(B)))
    rowA = len(A)
    rowB = len(B)
    if(colA != colB or rowA != rowB):
        return 'Error(mul): size mismatch'

    matrix = []
    return

#-----------------------------------------------------------
# Parameters:   A (matrix)
#               m (int)
# Return:       A` (matrix)
# Description:  Returns matrix A such that each element is the 
#               residue value in mode m
# Errors:       if A is empty matrix or not a valid matrix
#                   return 'Error(matrix_mod): invalid input'
#               if m is not a positive integer:
#                   return 'Error(matrix_mod): invalid mod'
#-----------------------------------------------------------
def matrix_mod(A,m):
    # your code here
    return

#-----------------------------------------------------------
# Parameters:   A (matrix)
# Return:       determinant of matrix A (int)
# Description:  Returns the determinant of a 2x2 matrix
# Errors:       if A is empty matrix nor not a valid square matrix
#                   return 'Error(det): invalid input'
#               if A is square matrix of size other than 2x2
#                   return 'Error(det): Unsupported matrix size'
#-----------------------------------------------------------
def det(A):
    # your code here
    return

#-----------------------------------------------------------
# Parameters:   A (matrix)
#               m (int)
# Return:       a new matrix which is the inverse of A mode m
# Description:  Returns the inverse of a 2x2 matrix in mode m
# Errors:       if A is empty matrix or not a valid matrix
#                   return 'Error(inverse): invalid input'
#               if A is not a square matrix or a matrix of 2x2 with no inverse:
#                   return 'Error(inverse): matrix is not invertible'
#               if A is a square matrix of size other than 2x2
#                   return 'Error(inverse): Unsupported matrix size'
#               if m is not a positive integer:
#                   return 'Error(inverse): invalid mod'
#-----------------------------------------------------------
def inverse(A,m):
    # your code here
    return
