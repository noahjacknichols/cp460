#--------------------------
#Noah Nichols
# CP460 (Fall 2019)
# Assignment 3
#--------------------------

import math
import string
import utilities_A3

#---------------------------------
#  Q1: Columnar Transposition    #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   key (string)           
# Return:       keyOrder (list)
# Description:  checks if given key is a valid columnar transposition key 
#               Returns key order, e.g. [face] --> [1,2,3,0]
#               Removes repititions and non-alpha characters from key
#               If empty string or not a string -->
#                   print an error msg and return [0] (which is a)
#               Upper 'A' and lower 'a' are the same order
#-----------------------------------------------------------
def get_keyOrder_columnarTrans(key):
    # your code here
    keyOrder = []
    alphabet = utilities_A3.get_lower()
    sortedKey = []
    newKey = []

    for letter in key:
        if(letter.isalpha()):
            if letter not in newKey:
                newKey.append(letter)

    
    for letter in key:
        sortedKey.append(tuple((alphabet.index(letter.lower()),letter)))
    
    sortedKey.sort(key=lambda tup: tup[0])
    
    for x in  range(len(sortedKey)):
        item = x
        keyOrder.append(newKey.index(item[1]))
        
    return keyOrder

#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               kye (str)
# Return:       ciphertext (list)
# Description:  Encryption using Columnar Transposition Cipher
#-----------------------------------------------------------
def e_columnarTrans(plaintext,key):
    # your code here
    ciphertext = ''
    col = len(key)
    row = math.ceil(len(plaintext) / col)
    counter = 0
    matrix = [[''] for x in range(row)] * col
    for i in range(col):
        for j in range(row):
            matrix[i][j] = plaintext[counter]
            counter+=1

    for i in key:
        ciphertext += matrix[i]

    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               kye (str)
# Return:       plaintext (list)
# Description:  Decryption using Columnar Transposition Cipher
#-----------------------------------------------------------
def d_columnarTrans(ciphertext,key):
    # your code here
    plaintext = ''
    col = len(key)
    row = math.ceil(len(ciphertext) / col)
    counter = 0
    matrix = [[''] for x in range(row)] * col


    for i in range(col):
        for j in range(row):
            matrix[i][j] = ciphertext[counter]
            counter+=1
    
    for i in range(row):
        for j in range(col):
            plaintext+= matrix[j][i]

    return plaintext
