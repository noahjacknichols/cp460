#--------------------------
# CP460 (Fall 2019)
# Assignment 4
# Solution by Qutaiba Albluwi
#--------------------------

import math
import string
import mod
import matrix
import utilities_A4

#---------------------------------
# Q1: Modular Arithmetic Library #
#---------------------------------

# solution is available in mod.py

#---------------------------------
#     Q2: Decimation Cipher      #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key (str,int)
# Return:       ciphertext (str)
# Description:  Encryption using Decimation Cipher
#               key is tuple (baseString,k)
#               Does not encrypt characters not in baseString
#               Case of letters should be preserved
# Errors:       if key has no multiplicative inverse -->
#                   print error msg and return empty string
#-----------------------------------------------------------
def e_decimation(plaintext,key):
    # your code here
    ciphertext = ''
    # print("KEY 1:",key[1])
    scopeAlpha = key[0]
    # print(scopeAlpha)
    if(mod.has_mul_inv(key[1],len(key[0])) != True):
        print('Error (e_decimation): Invalid Key')
        return 'Error (e_decimation): Invalid Key'

    for i in range(len(plaintext)):
            # print(plaintext[i])
            if(plaintext[i].lower() in scopeAlpha):
                if(plaintext[i].isupper()):
                    upper = True
                else:
                    upper = False
                cVal = key[1] * (scopeAlpha.index(plaintext[i].lower())) % len(scopeAlpha)
                # print("CVAL:", cVal)
                cVal = cVal % len(scopeAlpha)
                # cVal = cVal + 26 if upper else cVal
            # print("CVAL:",cVal)
            # print("cVal is:", chr(cVal))
                ciphertext+= scopeAlpha[cVal].upper() if upper else scopeAlpha[cVal]
            else:
                ciphertext+=plaintext[i]


    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key (str,int)
# Return:       plaintext (str)
# Description:  Decryption using Decimation Cipher
#               key is tuple (baseString,k)
#               Does not decrypt characters not in baseString
#               Case of letters should be preserved
# Errors:       if key has no multiplicative inverse -->
#                   print error msg and return empty string
#-----------------------------------------------------------
def d_decimation(ciphertext,key):
    # your code here
    plaintext =''
    scopeAlpha = key[0]
    if(mod.has_mul_inv(key[1], len(key[0])) != True):
        print('Error (d_decimation): Invalid Key')
        return ('Error (d_decimation): Invalid Key')
    for i in range(len(ciphertext)):
        if(ciphertext[i].lower() in scopeAlpha):
            if(ciphertext[i].isupper()):
                upper = True
            else:
                upper = False
            cVal = key[1] * (scopeAlpha.index(ciphertext[i].lower())) % len(scopeAlpha)
            
            plaintext+=scopeAlpha[cVal].upper() if upper else scopeAlpha[cVal]
        else:
            plaintext+=ciphertext[i]

    return plaintext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
# Return:       plaintext,key
# Description:  Cryptanalysis of Decimation Cipher
#-----------------------------------------------------------
def cryptanalysis_decimation(ciphertext):
    #your code here
    return '',''

#---------------------------------
#      Q3: Affine Cipher         #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key (str,[int,int])
# Return:       ciphertext (str)
# Description:  Encryption using Affine Cipher
#               key is tuple (baseString,[alpha,beta])
#               Does not encrypt characters not in baseString
#               Case of letters should be preserved
# Errors:       if key can not be used for decryption
#                   print error msg and return empty string
#-----------------------------------------------------------
def e_affine(plaintext,key):
    # your code here
    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key (str,[int,int])
# Return:       plaintext (str)
# Description:  Decryption using Affine Cipher
#               key is tuple (baseString,[alpha,beta])
#               Does not decrypt characters not in baseString
#               Case of letters should be preserved
# Errors:       if key can not be used for decryption
#                   print error msg and return empty string
#-----------------------------------------------------------
def d_affine(ciphertext,key):
    # your code here
    return plaintext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
# Return:       plaintext,key
# Description:  Cryptanalysis of Affine Cipher
#-----------------------------------------------------------
def cryptanalysis_affine(ciphertext):
    # your code here
    return '',''

#---------------------------------
#      Q4: Matrix Library        #
#---------------------------------

# solution is available in matrix.py

#---------------------------------
#       Q5: Hill Cipher          #
#---------------------------------

#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key (str)
# Return:       ciphertext (str)
# Description:  Encryption using Hill Cipher, 2x2 (mod 26)
#               key is a string consisting of 4 characters
#                   if key is too short, make it a running key
#                   if key is too long, use first 4 characters
#               Encrypts only alphabet
#               Case of characters can be ignored --> cipher is upper case
#               If necessary pad with 'Q'
# Errors:       if key is not inveritble or if plaintext is empty
#                   print error msg and return empty string
#-----------------------------------------------------------
def e_hill(plaintext,key):
    #your code here
    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (str)
#               key (str)
# Return:       plaintext (str)
# Description:  Decryption using Hill Cipher, 2x2 (mod 26)
#               key is a string consisting of 4 characters
#                   if key is too short, make it a running key
#                   if key is too long, use first 4 characters
#               Decrypts only alphabet
#               Case of characters can be ignored --> plain is lower case
#               Remove padding of q's
# Errors:       if key is not inveritble or if ciphertext is empty
#                   print error msg and return empty string
#-----------------------------------------------------------
def d_hill(ciphertext,key):
    #your code here
    return plaintext
