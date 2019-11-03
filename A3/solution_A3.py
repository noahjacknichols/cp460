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
    newKey = ''
    
    if(isinstance(key, str) == False):
        print("Error: Invalid Columnar Transposition Key ")
        return [0]

    for letter in str(key):
        if letter not in newKey and letter.isalpha() == True:
            newKey+=letter.lower()
    
    key = newKey
    if len(key) == 0:
        print("Error: Invalid Columnar Transposition Key ")
        return [0]
    
    keysSeen = [] #cheese everything
    
    for letter in key:
        
        if(letter not in keysSeen):
            sortedKey.append(tuple((alphabet.index(letter.lower()),letter)))
            keysSeen.append(letter)
        # else:
        #     # print("duplicate")
    
    sortedKey.sort(key=lambda tup: tup[0])
    #print(sortedKey)
    for x in  sortedKey:
        item = x
        #print(item)
        keyOrder.append(key.index(item[1]))
        
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
    ckey = get_keyOrder_columnarTrans(key)
    col = len(ckey)
    row = math.ceil(len(plaintext) / col)
    counter = 0
    matrix = [[''] * col for i in range(row)]
    # matrix = [[''] for x in range(row)] * col
    # print(matrix)
    # print(row,col)
    for i in range(row):
        for j in range(col):
            #print(i,j)
            matrix[i][j] = plaintext[counter] if counter < len(plaintext) else 'q'
            counter+=1

    #print(matrix)
    
    #print(ckey)
    for i in ckey:
        #print("ckey:", i)
        for j in range(row):
            #print("j:", j)
            
            ciphertext+= matrix[j][i]


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
    ckey = get_keyOrder_columnarTrans(key)
    col = len(ckey)
    row = math.ceil(len(ciphertext) / col)
    counter = 0
    matrix = [[''] * col for i in range(row)]
    newMatrix = [[''] * col for i in range(row)]
    #print(row,col)
    ckey = get_keyOrder_columnarTrans(key)
    for i in range(col):
        for j in range(row):
            #print(i,j)
            matrix[j][i] = ciphertext[counter] if counter < len(ciphertext) else 'Q'
            counter+=1
    c = 0
    for i in ckey:
        for j in range(row):
            newMatrix[j][i] = matrix[j][c]
        c+=1

    for j in range(row):
        for i in range(col):
            plaintext+= newMatrix[j][i]
    plaintext = plaintext.rstrip('q')

    return plaintext


#---------------------------------
#   Q2: Permutation Cipher       #
#---------------------------------

#-----------------------------------------------------------
# Parameters:   plaintext (str)
#               key(key,mode)
# Return:       ciphertext (str)
# Description:  Encryption using permutation cipher
#               mode 0: stream cipher --> columnar transposition
#               mode 1: block cipher --> block permutation
#               a padding of 'q' is to be used whenever necessary
#-----------------------------------------------------------
def e_permutation(plaintext, key):
    # your code here
    mode = key[1]
    print("MODE", mode)
    ciphertext = ''
    print("keyt is:", key)
    if(mode == 0):
        mkey = key[0]
        ckey = ''
        for i in range(len(mkey)):
            ckey+= chr(ord(mkey[i])+ 65)
            # print("CKEY:",ckey)
        ciphertext = e_columnarTrans(plaintext, ckey)
    elif(mode == 1):
        
        mkey = key[0]
        col = len(mkey)
        row = math.ceil(len(plaintext)/ col)
        
        counter = 0
        #matrix = [''] * row
        matrix = [[''] * col for i in range(row)]
        for j in range(row):
            for i in range(col):
                matrix[j][i] += plaintext[counter] if counter < len(plaintext) else 'q' 
                counter+=1
        
        #print(matrix)
        c = 0
        newMatrix = [[''] * col for i in range(row)]
        for j in range(row):
            for i in range(col):
                newMatrix[j][i] = matrix[j][int(mkey[c])-1]
                c+= 1
            c = 0
        #print(newMatrix)
        for j in range(row):
            for i in range(col):
                ciphertext+= newMatrix[j][i]
        

            
    else:
        print("Error (e_permutation): invalid mode")
        return ''
    return ciphertext

#----------------------------------------------------------S-
# Parameters:   ciphertext (str)
#               key(key,mode)
# Return:       plaintext (str)
# Description:  Decryption using permutation cipher
#               mode 0: stream cipher --> columnar transposition
#               mode 1: block cipher --> block permutation
#               a padding of 'q' is to be removed
#-----------------------------------------------------------


def d_permutation(ciphertext, key):
    # your code here
    plaintext = ''
    mode = key[1]
    if(mode == 0):
        mkey = key[0]
        ckey = ''
        for i in range(len(mkey)):
            ckey += chr(ord(mkey[i]) + 65)
            # print("CKEY:",ckey)
        plaintext = d_columnarTrans(ciphertext, ckey)
    elif(mode == 1):
        mkey = key[0]
        col = len(mkey)
        row = math.ceil(len(ciphertext)/ col)
        
        counter = 0
        #matrix = [''] * row
        matrix = [[''] * col for i in range(row)]
        for j in range(row):
            for i in range(col):
                matrix[j][i] += ciphertext[counter] if counter < len(ciphertext) else 'q' 
                counter+=1
        
        #print(matrix)
        c = 0
        newMatrix = [[''] * col for i in range(row)]
        for j in range(row):
            for i in range(col):
                newMatrix[j][int(mkey[c])-1] = matrix[j][i]
                c+= 1
            c = 0
        #print(newMatrix)
        for j in range(row):
            for i in range(col):
                plaintext+= newMatrix[j][i]
        plaintext = plaintext.rstrip('q')


    else:
        print("Error (d_permutation): invalid mode")
        return ''
    return plaintext

#---------------------------------
#       Q3: ADFGVX Cipher        #
#---------------------------------
#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using ADFGVX cipher
#--------------------------------------------------------------


def e_adfgvx(plaintext, key):
    # your code here
    ciphertext = ''
    square = utilities_A3.get_adfgvx_square()
    adfgvx = 'ADFGVX'
    encr = ''
    for char in plaintext:
        if(char.isalpha()):
            for i in range(len(square)):
                for j in range(len(square)):
                    upper = False
                    if char.isupper():
                        upper = True
                    #print("char:", char.upper(), "square:", square[j][i])
                    if(square[j][i] == char.upper()):

                        encr+= adfgvx[j] if upper else adfgvx[j].lower()
                        encr+= adfgvx[i] if upper else adfgvx[i].lower()
                        #print(encr)
        else:
            encr+= char
    
    #print("ENCR:",encr)
    

    # print(adfgvx)
    # col = len(key)
    # row = math.ceil(len(encr) / col)
    # matrix = [[''] * col for i in range(row)]

    # for j in range(row):
    #     for i in range(col):
    #         matrix[j][i] = encr[counter] if counter < len(encr) else 'q' 
    #         print()

    # ckey = get_keyOrder_columnarTrans(key)
    ciphertext = e_columnarTrans(encr, key)

    return ciphertext

#--------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using ADFGVX cipher
#--------------------------------------------------------------


def d_adfgvx(ciphertext, key):
    # your code here
    plaintext = ''

    decr = d_columnarTrans(ciphertext, key)
    square = utilities_A3.get_adfgvx_square()
    adfgvx = 'ADFGVX'
    i = 0
    print("DECR IS:",decr)
    while(i < len(decr)):
        if(decr[i].isalpha() != True):
            plaintext+= decr[i]
            i+=1
        else:
            upper = False
            if(decr[i].isupper() == True):
                upper = True
                
            x = adfgvx.index(decr[i].upper())
            i+=1
            y = adfgvx.index(decr[i].upper())
            plaintext += square[x][y] if upper else square[x][y].lower()
            i+=1
        

    return plaintext

#---------------------------------
#       Q4: One Time Pad         #
#---------------------------------
#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using One Time Pad
#               Result is shifted by 32
#------------------------------------------------------python-------


def e_otp(plaintext, key):
    # your code here
    ciphertext = ''
    for i in range(len(plaintext)):
        if(plaintext[i] != '\n'):
            result = xor_otp(plaintext[i], key[i])
            result = chr(ord(result) + 32)
            ciphertext+= result
        else:
            ciphertext+='\n'
    
    return ciphertext

#--------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using One Time Pad
#               Input is shifted by 32
#--------------------------------------------------------------


def d_otp(ciphertext, key):
    # your code here
    plaintext =''

    for i in range(len(ciphertext)):
        c = chr(ord(ciphertext[i])-32)
        result = xor_otp(c, key[i])
        plaintext+=result
        
    return plaintext
#--------------------------------------------------------------
# Parameters:   char1 (str)
#               char2 (str)
# Return:       result (str)
# Description:  Takes two characters. Convert their corresponding
#               ASCII value into binary (8-bits), then performs xor
#               operation. The result is treated as an ASCII value
#               which is converted to a character
#--------------------------------------------------------------


def xor_otp(char1, char2):
    # your code here

    x = ord(char1)
    y = ord(char2)
    result = x^y
    result = chr(result)
    return result

#---------------------------------
#    Q5: Myszkowski Cipher      #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   key (string)
# Return:       keyOrder (list)
# Description:  checks if given key is a valid Myszkowski key
#               Returns key order, e.g. [meeting] --> [3,0,0,5,2,4,1]
#               The key should have some characters that are repeated
#               and some characters that are non-repeated.
#               if invalid key --> return [1,1,0]
#               Upper and lower case characters are considered of same order
#               non-alpha characters sould be ignored
#-----------------------------------------------------------


def get_keyOrder_myszkowski(key):
    # your code here
    keyOrder = []
    
    alphabet = utilities_A3.get_lower()
    sortedKey = []
    newKey = ''

    if(isinstance(key, str) == False):
        print("Error: Invalid Myszkowski Key [1, 1, 0]")
        return [1,1,0]
    for i in key:
        if(i.isalpha() == True):
            newKey += i
    key = newKey.lower()
    if(len(key)==0):
        print("Error: Invalid Myszkowski Key [1, 1, 0]")
        return [1,1,0]
    # if(isinstance(int(key), int) == True):
    #     print("Error: Invalid Myszkowski Key [1, 1, 0]")
    #     return [1,1,0]
    

    unique = False
    nonUnique = False
    newKey = ''

    #print(key)
    for i in range(len(key)):
        for j in range(len(key)):
            if(i!= j):
                #print("i:", key[i], "j:", key[j])
                # print(key[i] == key[j])
                if(key[i] == key[j]):
                    nonUnique = True
                    #print(nonUnique)
    
    for i in range(len(key)):
        found = False
        for j in range(len(key)):
            if(i!= j):
                if(key[i] == key[j]):
                    found = True
        if found == False:
            unique = True

    # print("UNIQUE:", unique, "NONUNIQUE:", nonUnique)
    if(unique == True and nonUnique == True):
        #we have a valid key
        # print("WE GOT HERE")
        sortedKeys = []
        for letter in key:
            sortedKey.append(tuple((alphabet.index(letter.lower()),letter)))
    
        sortedKey.sort(key=lambda tup: tup[0])
        #print("sortedkey:",sortedKey)
        ref = ''
        for x in sortedKey:
            if x[1] not in ref:
                ref+=x[1]
        for x in key:
            
            keyOrder.append(ref.index(x))
        #print("keyorder:",keyOrder)
    else:
        print("Error: Invalid Myszkowski Key [1, 1, 0]")
        return [1, 1, 0]

        

    return keyOrder

#--------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (string)
# Return:       ciphertext (string)
# Description:  Encryption using Myszkowsi Transposition
#--------------------------------------------------------------


def e_myszkowski(plaintext, key):
    # your code here
    ciphertext =''
    order = get_keyOrder_myszkowski(key)
    col = len(order)
    row = math.ceil(len(plaintext)/ col)
    matrix = [[''] * col for i in range(row)]
    counter = 0
    for j in range(row):
        for i in range(col):
            matrix[j][i] = plaintext[counter] if counter < len(plaintext) else 'q'
            counter+=1

    # print(matrix)
    c = 0
    keysSeen = []
    newMatrix = [[''] * col for i in range(row)]
    c = 0
    ord2 = []
    for i in order:
        ord2.append(i)
    ord1 = []
    for i in ord2:
        ord1.append(i)
    ord2.sort()
    for i in ord2:
        for j in range(row):
            #print("I IS:",i)
            x = ord1.index(i)
            #print("X IS:",x)
            
            newMatrix[j][c] = matrix[j][x]
        ord1.insert(ord1.index(i), 'L')
        ord1.remove(i)
        
        c+=1
    # print(newMatrix)
    # print(ord2)

    for x in ord2:
        #print("X IS:", x)
        if(x not in keysSeen):
            for j in range(row):
                #print("X NOT IN ", keysSeen)
                for l in range(ord2.count(ord2[ord2.index(x)])):
                    #print("COUNT IS",ord2.count(ord2[x]))
                    ciphertext+= newMatrix[j][ord2.index(x)+l]
                    #print(ciphertext)
        keysSeen.append(x)
        # print(keysSeen)



    return ciphertext

#--------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (string)
# Return:       plaintext (string)
# Description:  Decryption using Myszkowsi Transposition
#--------------------------------------------------------------


def d_myszkowski(ciphertext, key):
    # your code here
    plaintext = ''
    order = get_keyOrder_myszkowski(key)
    col = len(order)
    row = math.ceil(len(ciphertext) / col)
    matrix = [[''] * col for i in range(row)]
    counter = 0
    ord1=[]
    for i in order:
        ord1.append(i)
    ord1.sort()
    keysSeen = []
    for x in ord1:
        if(x not in keysSeen):
            for j in range(row):
                for l in range(ord1.count(ord1[ord1.index(x)])):
                    matrix[j][ord1.index(x)+l] = ciphertext[counter]
                    counter+=1
        keysSeen.append(x)

    newMatrix = [[''] * col for i in range(row)]
    c = 0
    for i in ord1:
        for j in range(row):
            x = order.index(i)

            newMatrix[j][x] = matrix[j][c]
        order.insert(order.index(i), 'L')
        order.remove(i)
        c += 1

    for i in range(row):
        for j in range(col):
            plaintext+= newMatrix[i][j]

    plaintext = plaintext.rstrip('q')
 

    return plaintext
