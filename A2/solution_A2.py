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
    square = utilities_A2.get_vigenereSquare()
    ciphertext = ''
    for char in plaintext:
        if char.lower() in square[0]:
            plainIndx = square[0].index(char.lower())
            keyIndx = square[0].index(key)
            cipherChar = square[keyIndx][plainIndx]
            ciphertext+= cipherChar.upper() if char.isupper() else cipherChar
        else:
            ciphertext+= char
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
    square = utilities_A2.get_vigenereSquare()
    ciphertext = ''
    count = 0

    for char in plaintext:
        if char.lower() in square[0]:
            plainIndx = square[0].index(char.lower())
            keyIndx = square[0].index(key[count % len(key)])
            count += 1
            cipherChar = square[keyIndx][plainIndx]
            ciphertext += cipherChar.upper() if char.isupper() else cipherChar
        else:
            ciphertext += char
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
    square = utilities_A2.get_vigenereSquare()
    plaintext = ''
    for char in ciphertext:
        if char.lower() in square[0]:
            keyIndx = square[0].index(key)
            plainIndx = 0
            for i in range(26):
                if square[i][keyIndx] == char.lower():
                    plainIndx = i
                    break
            plainChar = square[0][plainIndx]
            key = plainChar
            plaintext += plainChar.upper() if char.isupper() else plainChar
        else:
            plaintext += char
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
    square = utilities_A2.get_vigenereSquare()
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
    blocks = []
    for i in range(0, len(text),size):
        if(i + size > len(text)):
            blocks.append(text[i:len(text)])
        else:
            blocks.append(text[i:i+size])

    return blocks

#-----------------------------------
# Parameters:   text (string)
# Return:       modifiedText (string)
# Description:  Removes all non-alpha characters from the given string
#               Returns a string of only alpha characters upper case
#-----------------------------------
def remove_nonalpha(text):
    modifiedText = ''
    for letter in text:
        if(letter.isalpha() == True):
            modifiedText += letter.upper()
        
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
    baskets = [''] * len(blocks[0])
    for block in blocks:
        for i in range(len(block)):
            baskets[i] +=(block[i])
    return baskets

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       I (float): Index of Coincidence
# Description:  Computes and returns the index of coincidence 
#               for a given text
#----------------------------------------------------------------
def get_indexOfCoin(ciphertext):
    # your code here
    I = 0
    cipherSet = list(set(ciphertext))
    #print(cipherSet)
    arr = [0] * len(cipherSet)
    # print(len(cipherSet))
    # print(len(arr))
    # print(len(ciphertext))
    for i in range(len(cipherSet)):
        for key in ciphertext:
            if(cipherSet[i] == key):
                # print(i)
                arr[i] +=1
    if(len(arr) > 0):

        max = arr[0]
        x = 0
        for i in range(len(arr)):
            I = I + (arr[i] / len(ciphertext)) * (((arr[i]) - 1) / (len(ciphertext)-1))

        #print(max)
        # I = max / (len(ciphertext) * (len(ciphertext) - 1))
        # print(cipherSet[x])

    else:
        I = 0
    return I

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key length (int)
# Description:  Uses Friedman's test to compute key length
#               returns key length rounded to nearest integer
#---------------------------------------------------------------
def getKeyL_friedman(ciphertext):
    # your code here
    I = get_indexOfCoin(ciphertext)
    k = math.ceil((0.067 - 0.0385) / (I - 0.0385))


    return k

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key length (int)
# Description:  Uses the Ciphertext Shift method to compute key length
#               Attempts key lengths 1 to 20
#---------------------------------------------------------------
def getKeyL_shift(ciphertext):
    # your code here
    x = utilities_A2.cryptanalysis_shift(ciphertext)
    y = list(x)
    k = y[0]
    
    return k


#---------------------------------
#   Q3:  Block Rotate Cipher     #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   key (b,r)
# Return:       updatedKey (b,r)
# Description:  Assumes given key is in the format of (b(int),r(int))
#               Updates the key in three scenarios:
#               1- The key is too big (use modulo)
#               2- The key is negative
#               if an invalid key is given print error message and return (0,0)
#-----------------------------------------------------------
def adjustKey_blockRotate(key):
    # your code here
    keyList = list(key)
    updatedKey = (0,0)
    if len(keyList) != 2:
        return updatedKey
    if keyList[1].is_integer == False:
        return updatedKey
    elif keyList[0] < keyList[1]:
        return updatedKey
    else:
        if(keyList[1] < 1):
            keyList[1] = 1
        else:
            keyList[1] = updatedKey[1] % updatedKey[0]
        updatedKey = (keyList[0], keyList[1])
    return updatedKey

#-----------------------------------
# Parameters:   text (string)
# Return:       nonalphaList (2D List)
# Description:  Analyzes a given string
#               Returns a list of non-alpha characters along with their positions
#               Format: [[char1, pos1],[char2,post2],...]
#               Example: get_nonalpha('I have 3 cents.') -->
#                   [[' ', 1], [' ', 6], ['3', 7], [' ', 8], ['.', 14]]
#-----------------------------------


def get_nonalpha(text):
    # your code here
    nonalphaList = []
    for i in range(len(text)):
        if(text[i].isalpha() == False):
            entry = [text[i], i]
            nonalphaList.append(entry)
    return nonalphaList

#-----------------------------------
# Parameters:   text (str)
#               2D list: [[char1,pos1], [char2,pos2],...]
# Return:       modifiedText (string)
# Description:  inserts a list of nonalpha characters in the positions
#-----------------------------------


def insert_nonalpha(text, nonAlpha):
    # your code here
    modifiedText = text
    for i in range(len(nonAlpha)):
        for j in range(len(text)):
            entry = nonAlpha[i]
            if(entry[1] == j):
                modifiedText = modifiedText[:j] + entry[0] + modifiedText[j:]
    return modifiedText

#-----------------------------------------------------------
# Parameters:   plaintext (string)
#               key (b,r): (int,int)
# Return:       ciphertext (string)
# Description:  break plaintext into blocks of size b
#               rotate each block r times to the left
#-----------------------------------------------------------


def e_blockRotate(plaintext, key):
    # your code here
    ciphertext =''
    mkey = list(key)
    blocks = [''] * mkey[0] 
    charPerBlock = math.ceil(len(plaintext) / mkey[0])
    for i in range(len(plaintext)):
        blocks[math.ceil(i/charPerBlock) -1].append(plaintext[i])
    
    for i in range(charPerBlock, len(blocks[len(blocks)], 1)):
        blocks[len(blocks)].append('q')
    
    for block in blocks:
        for j in range(len(block)):
            block.append(block.pop())
    
    for block in blocks:
        for i in range(len(block)):
            ciphertext+= block[i]



    return ciphertext

#-----------------------------------------------------------
# Parameters:   ciphertext (string)
#               key (b,r): (int,int)
# Return:       plaintext (string)
# Description:  Decryption using Block Rotate Cipher
#-----------------------------------------------------------


def d_blockRotate(ciphertext, key):
    # your code here
    plaintext = ''
    mkey = list(key)
    blocks = [''] * mkey[0] 
    charPerBlock = math.ceil(len(ciphertext) / mkey[0])
    for i in range(len(ciphertext)):
        blocks[math.ceil(i/charPerBlock) -1].append(ciphertext[i])
    
    for block in blocks:
        for j in range(len(block)):
            block = block.pop(len(block)) + block
    
    blocks[len(blocks)].strip('q')
    
    for block in blocks:
        for i in range(len(block)):
            plaintext+= block[i]



    return plaintext

#-----------------------------------------------------------
# Parameters:   ciphertext (string)
#               b1 (int): starting block size
#               b2 (int): end block size
# Return:       plaintext,key
# Description:  Cryptanalysis of Block Rotate Cipher
#               Returns plaintext and key (r,b)
#               Attempts block sizes from b1 to b2 (inclusive)
#               Prints number of attempts
#-----------------------------------------------------------


def cryptanalysis_blockRotate(ciphertext, b1, b2):
    # your code here
    plaintext=''
    key = (0,0)
    attempts = 0
    for blockSize in range(b1,b2,1):
        for possibleKey in range(blockSize, b2,1):
            text = d_blockRotate(ciphertext, (blockSize,possibleKey))
            if (utilities_A2.is_plaintext(text, 'engmix.txt', 0.8)):
                
                plaintext = text
                key = (blockSize, possibleKey)
                print("Key found after", attempts, " attempts")
                print("Key = ", key)
                print("Plaintext:",plaintext)

                return plaintext, key
            attempts+=1

    print("Block Rotate Cryptanalysis Failed. No Key was found")
    return plaintext, key

#---------------------------------
#       Q4: Cipher Detector     #
#---------------------------------
#-----------------------------------------------------------
# Parameters:   ciphertext (string)
# Return:       cipherType (string)
# Description:  Detects the type of a given ciphertext
#               Categories: "Atbash Cipher, Spartan Scytale Cipher,
#                   Polybius Square Cipher, Shfit Cipher, Vigenere Cipher
#                   All other ciphers are classified as Unknown.
#               If the given ciphertext is empty return 'Empty Ciphertext'
#-----------------------------------------------------------


def get_cipherType(ciphertext):
    # your code here
    return cipherType

#-------------------------------------
#  Q5: Wheastone Playfair Cipher     #
#-------------------------------------
#-----------------------------------------------------------
# Parameters:   plaintext (string)
# Return:       modifiedPlain (string)
# Description:  Modify a plaintext through the following criteria
#               1- All non-alpha characters are removed
#               2- Every 'W' is translsated into 'VV' double V
#               3- Convert every double character ## to #X
#               4- if the length of text is odd, add X
#               5- Output is formatted as pairs, separated by space
#                   all upper case
#-----------------------------------------------------------


def formatInput_playfair(plaintext):
    # your code here
     


    return modifiedPlain

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key: playfair Square (2D List)
# Return:       ciphertext (string)
# Description:  Encryption using Wheatstone Playfair Cipher
#---------------------------------------------------------------------------------------


def e_playfair(plaintext, key):
    # your code here
    return ciphertext

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key: playfair Square (2D List)
# Return:       ciphertext (string)
# Description:  Decryption using Wheatstone Playfair Cipher
#-------------------------------------------------------------------------------


def d_playfair(ciphertext, key):
    # your code here
    return plaintext
