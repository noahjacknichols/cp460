#--------------------------
# Your Name and ID   <--------------------- Change this -----
# CP460 (Fall 2019)
# Midterm Student Utilities File
#--------------------------

#-----------------------------------------------
# Remember to change the name of the file to:
#               utilities.py
# Delete this box after changing the file name
# ----------------------------------------------

#----------------------------------------------
# You can not add any library other than these:
import math
import string
import random
#----------------------------------------------

#-----------------------------------------------------------
# Parameters:   fileName (string)
# Return:       contents (string)
# Description:  Utility function to read contents of a file
#               Can be used to read plaintext or ciphertext
#-----------------------------------------------------------
def file_to_text(fileName):
    inFile = open(fileName,'r')
    contents = inFile.read()
    inFile.close()
    return contents

#-----------------------------------------------------------
# Parameters:   None
# Return:       baseString (str)
# Description:  Returns base string for substitution cipher
#-----------------------------------------------------------
def get_baseString():
    #generate alphabet
    alphabet = ''.join([chr(ord('a')+i) for i in range(26)])    
    symbols = """.,; #"?'!:-"""     #generate punctuations
    return alphabet + symbols

#-----------------------------------------------------------
# Parameters:   key (str)
# Return:       key (str)
# Description:  Utility function for Substitution cipher
#               Exchanges '#' wiht '\n' and vice versa
#-----------------------------------------------------------
def adjust_key(key):
    if '#' in key:
        newLineIndx = key.index('#')
        key = key[:newLineIndx]+'\n'+key[newLineIndx+1:]
    else:
        newLineIndx = key.index('\n')
        key = key[:newLineIndx]+'#'+key[newLineIndx+1:]
    return key

# you can add any utility functions as you like
