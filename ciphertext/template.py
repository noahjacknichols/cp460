#--------------------------
# Your Name and ID   <--------------------- Change this -----
# CP460 (Fall 2019)
# Midterm Student Solution File
#--------------------------

#-----------------------------------------------
# Remember to change the name of the file to:
#               solution.py
# Delete this box after changing the file name
# ----------------------------------------------

#----------------------------------------------
# You can not add any library other than these:
import math
import string
import random
import utilities
#----------------------------------------------

#---------------------------------
#           Q0: Matching         #
#---------------------------------
#-------------------------------------------------------
#                   EDIT THIS FILE
# change this function such that it makes the proper matching
# Also provide your description of how you found the matching. 
#-------------------------------------------------------
def match_files():
    # Files related to vigenere cipher
    cipher1 = 'ciphertext_yourname_qX.txt'  #<--- change this
    plain1  = 'plaintext_yourname_qX.txt'   #<--- change this
    vigenereFiles = [plain1,cipher1]
    print('The Vigenere ciphertext file is:',cipher1)
    print('I found that the above file is a vigenere cipher by ...') #<--- complete this
    print()
    
    # Files related to substitution cipher
    cipher2 = 'ciphertext_yourname_qX.txt'  #<--- change this
    plain2  = 'plaintext_yourname_qX.txt'   #<--- change this
    subFiles = [plain2,cipher2]
    print('The Substitution ciphertext file is:',cipher2)
    print('I found that the above file is a substitution cipher by ...') #<--- complete this
    print()
    
    # Files related to xshift cipher
    cipher3 = 'ciphertext_yourname_qX.txt'  #<--- change this
    plain3  = 'plaintext_yourname_qX.txt'   #<--- change this
    xshiftFiles = [plain3,cipher3]
    print('The xshift ciphertext file is:',cipher3)
    print('I found that the above file is an xshift cipher by ...') #<--- complete this
    print()
    
    # Files related to xcrypt cipher
    cipher4 = 'ciphertext_yourname_qX.txt'  #<--- change this
    plain4  = 'plaintext_yourname_qX.txt'   #<--- change this
    xcryptFiles = [plain4,cipher4]
    print('The xcrypt ciphertext file is:',cipher4)
    print('I found that the above file is an xcrypt cipher by ...') #<--- complete this
    print()
    
    return [vigenereFiles,subFiles,xshiftFiles,xcryptFiles]

#---------------------------------
#         Q1: Vigenere           #
#---------------------------------

#-----------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Enryption using Vigenere Cipher (Q1)
#-----------------------------------------------------------
def e_vigenere(plaintext, key):
    # your code here
    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Decryption using Vigenere Cipher (Q1)
#-----------------------------------------------------------
def d_vigenere(ciphertext, key):
    #your code here
    return plaintext

#-----------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key,plaintext
# Description:  Cryptanlysis of Vigenere Cipher (Q1)
#-----------------------------------------------------------
def cryptanalysis_vigenere(ciphertext):
    # yoru code here
    return key,plaintext

def comments_q1():
    print('Comments:')
    print('Explain here how you found the key length')  #<---- edit this
    print('Also explain how you found the keyword')     #<---- edit this
    return

#---------------------------------
#   Q2: Substitution Cipher      #
#---------------------------------
#-------------------------------------------------------
# Parameters:   plaintext(str)
#               key: subString (str)
# Return:       ciphertext (string)
# Description:  Encryption using substitution (Q2)
#-------------------------------------------------------
def e_substitution(plaintext,key):
    # your code here
    return ciphertext

#-----------------------------------------
# Parametes:    ciphertext (str)
#               key: subString (str)
# Return:       plaintext (str)
# Description:  Decryption using substitution (Q2)
#-----------------------------------------
def d_substitution(ciphertext,key):
    # your code here
    return plaintext

def cryptanalysis_substitution(ciphertext):
    key = '''yhribekafszmpxwojductnvlgq!-#;". '?,:'''   #<--- change this line with your key
    key = utilities.adjust_key(key)                     #<--- keep this line
    # add lines to decrypt the ciphertext
    # remember to write your plaintext to file
    return key,plaintext

def comments_q2():
    print('Comments:')
    print('See Qutaiba_Albluwi_sub_log.txt file') #<----- edit this
    return

#---------------------------------
#           Q3: Xshift           #
#---------------------------------

#-----------------------------------------
# Parametes:    plaintext (str)
#               key: (shiftString,shifts)
# Return:       ciphertext (str)
# Description:  Encryption using Xshift Cipher
#-----------------------------------------
def e_xshift(plaintext, key):
    # your code here
    return ciphertext

#-----------------------------------------
# Parametes:    ciphertext (str)
#               key: (shiftString,shifts)
# Return:       plaintext (str)
# Description:  Decryption using Xshift Cipher
#-----------------------------------------
def d_xshift(ciphertext, key):
    # your code here
    return plaintext

#-----------------------------------------
# Parametes:    ciphertext (str)
# Return:       key,plaintext
# Description:  Cryptanalysis of  Xshift Cipher
#-----------------------------------------
def cryptanalysis_xshift(ciphertext):
    #your code here
    return key,plaintext

def comments_q3():
    print('Comments:')
    print('Brute-force space is:')                  #<--- edit this
    print('Explain here your brute-force design')   #<--- edit this
    return

#---------------------------------
#           Q4: Xcrypt           #
#---------------------------------
#-------------------------------------------------------
# Parameters:   plaintext(string)
#               key (int)
# Return:       ciphertext (string)
# Description:  Encryption using xcrypt (Q4)
#-------------------------------------------------------
def e_xcrypt(plaintext,key):
    # your code here
    return ciphertext

#-------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (int)
# Return:       plaintext (string)
# Description:  Decryption using xcrypt (Q4)
#-------------------------------------------------------
def d_xcrypt(ciphertext,key):
    # your code here
    return plaintext

#-------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key (int),plaintext (str)
# Description:  cryptanalysis of xcrypt (Q4)
#-------------------------------------------------------
def cryptanalysis_xcrypt(ciphertext,key):
    # your code here
    return key,plaintext

#-------------------------------------------------------
# Parameters:   None
# Return:       None
# Description:  Your comments on Q4 solution
#-------------------------------------------------------
def comments_q4():
    print('My Comments:')
    print('Used threshold is: ',0)              # <---- edit this
    print('Cryptanalysis Method: blablalba')    # <---- edit this
    return
