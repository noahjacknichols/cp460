#--------------------------
# Noah Nichols
# CP460 (Fall 2019)
# Midterm Student Solution File
#--------------------------



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
    cipher1 = 'ciphertext_Noah_Nichols_q4.txt'  #<--- change this
    plain1  = 'plaintext_Noah_Nichols_q4.txt'   #<--- change this
    vigenereFiles = [plain1,cipher1]
    print('The Vigenere ciphertext file is:',cipher1)
    print('I found that the above file is a vigenere cipher by ...') #<--- complete this
    print()
    
    # Files related to substitution cipher
    cipher2 = 'ciphertext_Noah_Nichols_q3.txt'  #<--- change this
    plain2  = 'plaintext_Noah_Nichols_q3.txt'   #<--- change this
    subFiles = [plain2,cipher2]
    print('The Substitution ciphertext file is:',cipher2)
    print('I found that the above file is a substitution cipher by ...') #<--- complete this
    print()
    
    # Files related to xshift cipher
    cipher3 = 'ciphertext_Noah_Nichols_q2.txt'  #<--- change this
    plain3  = 'plaintext_Noah_Nichols_q2.txt'   #<--- change this
    xshiftFiles = [plain3,cipher3]
    print('The xshift ciphertext file is:',cipher3)
    print('I found that the above file is an xshift cipher by ...') #<--- complete this
    print()
    
    # Files related to xcrypt cipher
    cipher4 = 'ciphertext_Noah_Nichols_q1.txt'  #<--- change this
    plain4  = 'plaintext_Noah_Nichols_q1.txt'   #<--- change this
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
    if not isinstance(key,str) or key == '' or not key.isalpha():
        print('Error (e_vigenere): invalid key!')
        return ''
    key = key.lower()
    if len(key) == 1:
        return utilities.e_vigenere1(plaintext,key)
    else:
        return utilities.e_vigenere2(plaintext,key)
    

#-----------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Decryption using Vigenere Cipher (Q1)
#-----------------------------------------------------------
def d_vigenere(ciphertext, key):
    #your code here
    square = utilities.get_vigenereSquare()
    plaintext = ''
    count = 0
    for char in ciphertext:
        if char.lower() in square[0]:
            keyIndx = square[0].index(key[count % len(key)])
            count += 1
            plainIndx = 0
            for i in range(26):
                if square[i][keyIndx] == char.lower():
                    plainIndx = i
                    break
            plainChar = square[0][plainIndx]
            plaintext += plainChar.upper() if char.isupper() else plainChar
        else:
            plaintext += char
    return plaintext


#-----------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key,plaintext
# Description:  Cryptanlysis of Vigenere Cipher (Q1)
#-----------------------------------------------------------
def cryptanalysis_vigenere(ciphertext):
    # yoru code here
    alphabet = utilities.get_lower()
    key = ''
    values=[0] * 26
    x = 0
    keyLength = utilities.getKeyL_shift(ciphertext)
    nonalpha = utilities.remove_nonalpha(ciphertext)
    blocks = utilities.text_to_blocks(nonalpha, keyLength)
    baskets = utilities.blocks_to_baskets(blocks)
    for text in baskets:
        for x in range(26):
            values[x] = utilities.get_chiSquared(utilities.d_shift(text, (x,'l')))
        index = values.index(min(values))
        key = key + alphabet[index]
    plaintext = d_vigenere(ciphertext, key)
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

    baseString = utilities.adjust_key(utilities.get_baseString())
    subString  = utilities.adjust_key(key)
    ciphertext = ''
    for plainChar in plaintext:
        upperFlag = True if plainChar.isupper() else False
        plainChar = plainChar.lower()
        if plainChar in baseString:
            indx = baseString.index(plainChar)
            cipherChar = subString[indx]
            cipherChar = cipherChar.upper() if upperFlag else cipherChar
        else:
             cipherChar = plainChar.upper() if upperFlag else plainChar
        ciphertext += cipherChar
    # if('#' in ciphertext):
    ciphertext = utilities.adjust_key(ciphertext)

    return ciphertext

#-----------------------------------------
# Parametes:    ciphertext (str)
#               key: subString (str)
# Return:       plaintext (str)
# Description:  Decryption using substitution (Q2)
#-----------------------------------------
def d_substitution(ciphertext,key):
    # your code here
    plaintext = ''
    alphabet = utilities.adjust_key(utilities.get_baseString())


    for cipherChar in ciphertext:
        upperFlag = True if cipherChar.isupper() else False
        cipherChar = cipherChar.lower()
        if cipherChar in alphabet:
            indx = key.index(cipherChar)
            plainChar = alphabet[indx]
            plainChar = plainChar.upper() if upperFlag else plainChar
        else:
            plainChar = cipherChar.upper() if upperFlag else cipherChar
        plaintext+= plainChar
    
    return plaintext

def cryptanalysis_substitution(ciphertext):
    key = '''yhribekafszmpxwojductnvlgq!-#;". '?,:'''   #<--- change this line with your key
    key = utilities.adjust_key(key)                     #<--- keep this line
    plaintext =''
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
    ciphertext = ''
    shift_string = key[0]
    shift_value = key[1] % 52
    for c in plaintext:
        if c in shift_string:
            pi = shift_string.index(c)
            ci = (pi + shift_value)%52
            cipherChar = shift_string[ci]
            ciphertext+= cipherChar
        else:
            ciphertext+=c
    return ciphertext

#-----------------------------------------
# Parametes:    ciphertext (str)
#               key: (shiftString,shifts)
# Return:       plaintext (str)
# Description:  Decryption using Xshift Cipher
#-----------------------------------------
def d_xshift(ciphertext, key):
    # your code here
    return e_xshift(ciphertext, (key[0], 52 - (key[1] % 52)))


#-----------------------------------------
# Parametes:    ciphertext (str)
# Return:       key,plaintext
# Description:  Cryptanalysis of  Xshift Cipher
#-----------------------------------------
def cryptanalysis_xshift(ciphertext):
    #your code here
    key = 0
    plaintext = ''
    regLower = 'abcdefghijklmnopqrstuvwxyz'
    regUpper = regLower.upper()
    atbashLower = regLower[::-1]
    atbashUpper = atbashLower.upper()
    possibilities = [regLower+regUpper, regLower+atbashUpper, atbashLower+regUpper, atbashLower+atbashUpper]
    listTuples = []
    for possible in possibilities:
        for i in range(26):
            decr = d_xshift(ciphertext, tuple((str(possible), i)))
            chi = utilities.get_chiSquared(decr)
            listTuples.append(tuple((decr, chi, i, possible)))
    
    listTuple = sorted(listTuples, key=lambda tup: tup[1])

    for item in listTuple:
        if(utilities.is_plaintext(item[0], 'engmix.txt', 0.8)):
            key = tuple((item[3], item[2])) 
            plaintext = item[0]
            return key, plaintext

    return key, plaintext


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
    ciphertext = ''

    row = key
    col = math.ceil(len(plaintext) /row)
    matrix = [[''] * col for i in range(row)]
    counter = 0
    for i in range(col):
        for j in range(row):
            matrix[j][i] = plaintext[counter] if counter < len(plaintext) else 'q'
            counter+=1
    
    for i in range(row):
        for j in range(col):
            ciphertext+= matrix[i][j]


    return ciphertext

#-------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (int)
# Return:       plaintext (string)
# Description:  Decryption using xcrypt (Q4)
#-------------------------------------------------------
def d_xcrypt(ciphertext,key):
    # your code here
    plaintext=''
    row = key
    col = math.ceil((len(ciphertext))/row)
    matrix = [[''] * col for i in range(row)]
    counter = 0
    if(row * col != len(ciphertext)):
        return ''
    for i in range(row):
        for j in range(col):
            matrix[i][j] = ciphertext[counter]
            counter+=1
    
    for i in range(col):
        for j in range(row):
            plaintext+= matrix[j][i]
    notQ = True
    while(notQ == True):
        if(plaintext[len(plaintext)-1] == 'q'):
            plaintext = plaintext[:len(plaintext)-1]
        else:
            notQ = False
    return plaintext

#-------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key (int),plaintext (str)
# Description:  cryptanalysis of xcrypt (Q4)
#-------------------------------------------------------
def cryptanalysis_xcrypt(ciphertext):
    # your code here
    plaintext = ''
    i = 0
    for i in range(1,501):
        plain = d_xcrypt(ciphertext, i)
        is_plain = utilities.is_plaintext(plain, "engmix.txt", 0.8)
        if(is_plain == True):
            return i, plain
    return i, plaintext

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
