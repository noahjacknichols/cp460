#--------------------------
# Your Name and ID   <--------------------- Change this -----
# CP460 (Fall 2019)
# Assignment 2
#--------------------------

import math
import utilities_A2

#---------------------------------
#Q1: Vigenere Cipher (Version 2) #
#---------------------------------
#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): string of any length
# Return:       ciphertext (string)
# Description:  Genereic Encryption scheme using Vigenere Cipher
#               calls proper function depending on key length
#               if len(key) == 1 --> call e_vigenere1
#               else --> call e_vigenere2
#               If invalid key (not string or empty string or non-alpha string) -->
#                   print error and return '',''
#---------------------------------------------------------------------------------------
def e_vigenere(plaintext,key):
    if not isinstance(key,str) or key == '' or not key.isalpha():
        print('Error (e_vigenere): invalid key!')
        return ''
    key = key.lower()
    if len(key) == 1:
        return e_vigenere1(plaintext,key)
    else:
        return e_vigenere2(plaintext,key)

#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): string of anylength
# Return:       ciphertext (string)
# Description:  Genereic Encryption scheme using Vigenere Cipher
#               calls proper function depending on key length
#               if len(key) == 1 --> call d_vigenere1
#               else --> call d_vigenere2
#               If invalid key (not string or empty string or contains no alpha char) -->
#                   print error and return '',''
#---------------------------------------------------------------------------------------
def d_vigenere(ciphertext,key):
    if not isinstance(key,str) or key == '' or not key.isalpha():
        print('Error (d_vigenere): invalid key!')
        return ''
    key = key.lower()
    if len(key) == 1:
        return d_vigenere1(ciphertext,key)
    else:
        return d_vigenere2(ciphertext,key)

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): single character
# Return:       ciphertext (string)
# Description:  Encryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def e_vigenere1(plaintext, key):
    # your code here
    return ciphertext

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Encryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def e_vigenere2(plaintext, key):
    # your code here
    return ciphertext
    
#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): single character
# Return:       ciphertext (string)
# Description:  Decryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def d_vigenere1(ciphertext, key):
    # your code here
    return plaintext

#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Decryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------
def d_vigenere2(ciphertext, key):
    # your code here
    return plaintext


#-------------------------------------
#Q2: Vigenere Crytanalysis Utilities #
#-------------------------------------

#-----------------------------------------------------------------------------
# Parameters:   text (string)
#               size (int)
# Return:       list of strings
# Description:  Break a given string into strings of given size
#               Result is provided in a list
#------------------------------------------------------------------------------
def text_to_blocks(text,size):
    # your code here
    return blocks

#-----------------------------------
# Parameters:   text (string)
# Return:       modifiedText (string)
# Description:  Removes all non-alpha characters from the given string
#               Returns a string of only alpha characters upper case
#-----------------------------------
def remove_nonalpha(text):
    # your code here
    return modifiedText

#-------------------------------------------------------------------------------------
# Parameters:   blocks: list of strings
# Return:       baskets: list of strings
# Description:  Assume all blocks have same size = n (other than last block)
#               Create n baskets
#               In basket[i] put character #i from each block
#---------------------------------------------------------------------------------------
def blocks_to_baskets(blocks):
    # your code here
    return baskets

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       I (float): Index of Coincidence
# Description:  Computes and returns the index of coincidence 
#               for a given text
#----------------------------------------------------------------
def get_indexOfCoin(ciphertext):
    # your code here
    return I

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key length (int)
# Description:  Uses Friedman's test to compute key length
#               returns key length rounded to nearest integer
#---------------------------------------------------------------
def getKeyL_friedman(ciphertext):
    # your code here
    return k

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key length (int)
# Description:  Uses the Ciphertext Shift method to compute key length
#               Attempts key lengths 1 to 20
#---------------------------------------------------------------
def getKeyL_shift(ciphertext):
    # your code here
    return k


#---------------------------------
#Q3:  #
#---------------------------------
# stay tuned

#---------------------------------
#Q4:  #
#---------------------------------
# stay tuned

#---------------------------------
#Q5:  #
#---------------------------------
# stay tuned
