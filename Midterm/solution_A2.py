#--------------------------
# Noah Nichols
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
    arr = [0] * len(cipherSet)
    for i in range(len(cipherSet)):
        for key in ciphertext:
            if(cipherSet[i] == key):
                arr[i] +=1
    if(len(arr) > 0):
        for i in range(len(arr)):
            I = I + (arr[i] / len(ciphertext)) * (((arr[i]) - 1) / (len(ciphertext)-1))
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
    n = len(ciphertext)
    I = get_indexOfCoin(ciphertext)
    k = math.ceil((0.027 * n) / (((n-1) * I) + 0.065 - (0.038 * n)))

    return k

#----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key length (int)
# Description:  Uses the Ciphertext Shift method to compute key length
#               Attempts key lengths 1 to 20
#---------------------------------------------------------------
def getKeyL_shift(ciphertext):
    # your code here
    counts = [0] * 21
    for i in range(1,21):
        s = utilities_A2.shift_string(ciphertext, i, 'r')
        matches = 0
        for j in range(i, len(s)):
            if ciphertext[j] == s[j]:
                matches += 1
                counts[i] = matches
    maxN = counts[0]
    for num in counts:
        if num > maxN:
            maxN = num
    k = counts.index(maxN)
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
    updatedKey = (0,0)
    if not type(key) == tuple:
        print("Error (adjustKey_blockRotate): Invalid Key")
        return updatedKey
    keyList = list(key)
    #print(key)
    


    if not type(key[0]) == int or not type(key[1]) == int:
        print("Error (adjustKey_blockRotate): Invalid Key")
        return updatedKey
    elif len(keyList) != 2:
        print("Error (adjustKey_blockRotate): Invalid Key")
        return updatedKey
    elif keyList[0] < 1:
        print("Error (adjustKey_blockRotate): Invalid Key")
        return updatedKey
    else:
        if(keyList[1] < 1):
            keyList[1] = 1
        else:
            
            keyList[1] = keyList[1] % keyList[0]
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
    if(len(nonAlpha) > 0):
        for i in range(len(nonAlpha)):
            modifiedText = modifiedText[:nonAlpha[i][1]] + nonAlpha[i][0] + modifiedText[nonAlpha[i][1]:]
    
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
    nonAlpha = get_nonalpha(plaintext)
    ciphertext =''
    plaintext = "".join([char for char in plaintext if char.isalpha()])

    blocks = text_to_blocks(plaintext, key[0])

    for _ in range(len(blocks[len(blocks)-1]),len(blocks[0]), 1):
        blocks[len(blocks)-1]+= 'q'
    
    for block in blocks:
        ciphertext += utilities_A2.shift_string(block, key[1], 'l')
    
    ciphertext = insert_nonalpha(ciphertext, nonAlpha)


        


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
    nonAlpha = get_nonalpha(ciphertext)
    ciphertext = "".join([char for char in ciphertext if char.isalpha()])
    
    blocks = text_to_blocks(ciphertext, key[0])

    for i in range(len(blocks)):
        blocks[i] = utilities_A2.shift_string(blocks[i], key[1], 'r')
        #print(blocks[i])
    
    temp = ''
    for letter in blocks[len(blocks)-1]:
        if(letter != 'q'):
            temp += letter
    blocks[len(blocks)-1] = temp
    
    for block in blocks:
        for j in range(len(block)):
            plaintext+= block[j]
    
    plaintext = insert_nonalpha(plaintext, nonAlpha)
    
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
        for possibleKey in range(1, blockSize,1):
            text = d_blockRotate(ciphertext, (blockSize,possibleKey))
            if (utilities_A2.is_plaintext(text, 'engmix.txt', 0.9)):
                
                plaintext = text
                key = (blockSize, possibleKey)
                print("Key found after", attempts+1, " attempts")
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



#MIDTERM: 
# --> 1: Vigenere --> enough tools
# --> 2: Shift (some kind of shift, not caesar) --> try cryptanalysis and chi squared
# --> 3: mono alpha substitution --> like shift for each character
# --> 4: Another cipher.
#-----------------------------------------------------------
#Scytale --> chi squared < 150
#Polybius 
#Vigenere --> I ( random (0.035) - E (0.065))
#Atbash/Shift --> I same as english, flip Atbash cipher run I again tells you Atbash


def get_cipherType(ciphertext):
    # your code here
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print()
    strippedCipher = remove_nonalpha(ciphertext)
    #print(strippedCipher)

    I_english = 0.065
    margin = 0.003

    cipherType = ''
    
    if(len(ciphertext) < 1):
        return 'Empty Ciphertext'
    I = get_indexOfCoin(ciphertext)
    #print("I is:", I)
    
    chi = utilities_A2.get_chiSquared(ciphertext)
    #print("chi is:", chi)
    if(chi < 400):
        return "Spartan Scytale Cipher"
    elif(I > I_english - margin and I < I_english + margin):
        #print("ATBASH OR SHIFT CIPHER")
        temp = ''
        for c in strippedCipher:
            temp += alphabet[25- alphabet.index(c)]

        
        I_temp = get_indexOfCoin(temp)
        chi_Temp = utilities_A2.get_chiSquared(temp)
        #print("flipped I is:", I_temp)
        #print(utilities_A2.get_chiSquared(strippedCipher))
        
        if(chi_Temp < 150):
            return("Atbash Cipher")
        else:
            return("Shift Cipher")
    elif(len(strippedCipher) == 0):
        return("Polybius Square Cipher")
    elif(I > 0.0415 and I < 0.062):
        return("Vigenere Cipher")
    else:
        return("Unknown")
        

    
    
        
    
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

# Rule 1: if same row --> 2 chars to right
# Rule 2: if same col --> 2 chars 
# Rule 3: if not same row/col --> take the char above the pos of the other char

#-----------------------------------------------------------


def formatInput_playfair(plaintext):
    # your code here
    modifiedPlain = ''

    plaintext = remove_nonalpha(plaintext)
    n = len(plaintext)
    i = 0

    while i < n:
        if plaintext[i] == "W":
            plaintext = plaintext[:i] + "VV" + plaintext[i+1:]
            n+=1
        i+=1
    if(len(plaintext) % 2 > 0):
        plaintext+='X'
    for i in range(len(plaintext)):
        if i % 2 == 0 and i != 0:
            modifiedPlain += ' '
            modifiedPlain += plaintext[i]
        else:
            modifiedPlain += plaintext[i]
    for i in range(len(modifiedPlain)):
        if i != 0:
            if modifiedPlain[i-1] == modifiedPlain[i]:
                modifiedPlain = modifiedPlain[:i] + 'X' + modifiedPlain[i+1:]
    
    return modifiedPlain


#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key: playfair Square (2D List)
# Return:       ciphertext (string)
# Description:  Encryption using Wheatstone Playfair Cipher
#---------------------------------------------------------------------------------------


def e_playfair(plaintext, key):
    # your code here
    ciphertext=''
    plain = formatInput_playfair(plaintext)
    plainList = plain.split()
    size = len(key)
    for combo in plainList:
        Ax = -1
        Ay = -1
        Bx = -1
        By = -1
        
        for i in range(len(key)):
            for j in range(len(key[0])):
                if(combo[0] == key[i][j]):
                    Ax = j
                    Ay = i
                if(combo[1] == key[i][j]):
                    Bx = j
                    By = i
        if(Ax != -1 and Ay != -1 and Bx != -1 and By != -1):
            if(Ax == Bx):
                # print(Ax+1)
                # print(Ay)
                # print(Ax + 1 % size)
                #print("SAME ROW")
                ciphertext += key[(Ay+1) % size][Ax]
                ciphertext += key[(By+1) % size][Bx]
                ciphertext += ' '
            elif(Ay == By):
                #print("SAME COL")
                ciphertext += key[Ay][(Ax+1)%size]
                ciphertext += key[By][(Bx+1) % size]
                ciphertext += ' '
            else:
                #print("NOTHING SAME")
                ciphertext += key[Ay][Bx]
                ciphertext += key[By][Ax]
                
                ciphertext+= ' '

    return ciphertext

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key: playfair Square (2D List)
# Return:       ciphertext (string)
# Description:  Decryption using Wheatstone Playfair Cipher
#-------------------------------------------------------------------------------


def d_playfair(ciphertext, key):
    # your code here
    
    plaintext =''
    
    cipher = formatInput_playfair(ciphertext)
    cipherList = cipher.split()
    # print("CipherList:", cipherList)
    size = len(key)
    #print(cipher)
    for combo in cipherList:
        # print("d_playfair")
        Ax = -1
        Ay = -1
        Bx = -1
        By = -1

        for i in range(len(key)):
            for j in range(len(key[0])):
                if(combo[0] == key[i][j]):
                    Ax = j
                    Ay = i
                if(combo[1] == key[i][j]):
                    Bx = j
                    By = i
        if(Ax != -1 and Ay != -1 and Bx != -1 and By != -1):
            if(Ax == Bx):
                #print("SAME ROW")
                
                plaintext += key[(Ay-1+size) % size][Ax]
                plaintext += key[(By-1+size) % size][Bx]
                if(combo != cipherList[len(cipherList)-1]):
                    plaintext+= " "
                
            elif(Ay == By):
                #print("SAME COL")
                plaintext += key[Ay][(Ax-1+size) % size]
                plaintext += key[By][(Bx-1+size) % size]
                if(combo != cipherList[len(cipherList)-1]):
                    plaintext += " "
                
            else:
                #print("NOTHING SAME")
                plaintext += key[Ay][Bx]
                plaintext += key[By][Ax]
                if(combo != cipherList[len(cipherList)-1]):
                    plaintext += " "

            

    # if (plaintext[len(plaintext)-1]) == 'X':
    #     plaintext = plaintext[:len(plaintext)-1]

    # for i in range(len(plaintext)):
    #     if(i != 0):
    #         if(plaintext[i] == 'X'):
    #             plaintext = plaintext[:i] + plaintext[i-1] + plaintext[i+1:]

                

    
    return plaintext


#simple substitution (password)

#Base string: abc....xyz <-- lower
#Substring:   rfg....asp <-- random

#if basestring is known:
    #key: substring
#if basestring is unkown:
    #key: (basestring, substring)

#drawback: some characters are aligned.

def get_subKey(password, baseString):
    subkey = ''
    for passChar in password:
        if passChar not in subkey:
            subkey+= passChar
    for baseChar in baseString:
        if baseChar not in subkey:
            subkey+= baseChar
    return subkey

def e_substituion(plaintext, key):
    baseString = key[0]
    subString = key[1]

    ciphertext =''
    for plainChar in plaintext:
        upperFlag = True if plainChar.isupper() else False
        plainChar = plainChar.lower()
        if(plainChar in baseString):
            i = baseString.index(plainChar)
            cipherChar = subString[i]
            cipherChar = cipherChar.upper() if upperFlag else cipherChar
        else:
            cipherChar = plainChar
        ciphertext+= cipherChar

        
        
        
    
