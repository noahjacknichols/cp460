#--------------------------
# Noah Nichols
# CP460 (Fall 2019)
# Midterm Student Utilities File
#--------------------------

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


import string
import math

#-----------------------------------------------------------
#-----------------------------------------------------------
###########                                     ############
###########   PURPOSED FOR THE MIDTERM USE BY   ############
###########            noah nichols             ############
###########                                     ############
#-----------------------------------------------------------
#-----------------------------------------------------------

#MIDTERM:
# --> 1: Vigenere --> enough tools from past work.
# --> 2: Shift (some kind of shift, not caesar) --> try cryptanalysis and chi squared
# --> 3: mono alpha substitution --> like shift for each character
# --> 4: Another cipher.



#-----------------------------------------------------------
# Parameters:   text (string)
#               filename (string)
# Return:       none
# Description:  Utility function to write any given text to a file
#               If file already exist, previous content will be over-written
#-----------------------------------------------------------


def text_to_file(text, filename):
    outFile = open(filename, 'w')
    outFile.write(text)
    outFile.close()
    return

#-----------------------------------------------------------
# Parameters:   None
# Return:       alphabet (string)
# Description:  Return a string of lower case alphabet
#-----------------------------------------------------------


def get_lower():
    return "".join([chr(ord('a')+i) for i in range(26)])

#-----------------------------------------------------------
# Parameters:   None
# Return:       squqre (list of strings)
# Description:  Constructs Vigenere square as list of strings
#               element 1 = "abcde...xyz"
#               element 2 = "bcde...xyza" (1 shift to left)
#-----------------------------------------------------------


def get_vigenereSquare():
    alphabet = get_lower()
    return [shift_string(alphabet, i, 'l') for i in range(26)]

#-----------------------------------------------------------
# Parameters:   None
# Return:       list
# Description:  Return a list with English language letter frequencies
#               first element is frequency of 'a'
#-----------------------------------------------------------


def get_freqTable():
    freqTable = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
                 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
    return freqTable

#-----------------------------------------------------------
# Parameters:   text (str)
# Return:       list: wordCount
# Description:  Count frequency of letters in a given text
#               Returns a list, first element is count of 'a'
#               Counts both 'a' and 'A' as one character
#-----------------------------------------------------------


def get_charCount(text):
    return [text.count(chr(97+i))+text.count(chr(65+i)) for i in range(26)]

#-------------------------------------------------------------------
# Parameters:   s (string): input string
#               n (int): number of shifts
#               d (str): direction ('l' or 'r')
# Return:       s (after applying shift
# Description:  Shift a given string by n shifts (circular shift)
#               as specified by direction, l = left, r= right
#               if n is negative, multiply by 1 and change direction
#-------------------------------------------------------------------


def shift_string(s, n, d):
    if d != 'r' and d != 'l':
        print('Error (shift_string): invalid direction')
        return ''
    if n < 0:
        n = n*-1
        d = 'l' if d == 'r' else 'r'
    n = n % len(s)
    if s == '' or n == 0:
        return s

    s = s[n:]+s[:n] if d == 'l' else s[-1*n:] + s[:-1*n]
    return s

#-----------------------------------------------------------
# Parameters:   text (string)
# Return:       double
# Description:  Calculates the Chi-squared statistics
#               chiSquared = for i=0(a) to i=25(z):
#                               sum( Ci - Ei)^2 / Ei
#               Ci is count of character i in text
#               Ei is expected count of character i in English text
#               Note: Chi-Squared statistics uses counts not frequencies
#-----------------------------------------------------------


def get_chiSquared(text):
    freqTable = get_freqTable()
    #print("text is: '_",text, "_'")
    charCount = get_charCount(text)
    if(text.strip() != ''):
        #print("length is",len(charCount))
        result = 0
        for i in range(26):
            Ci = charCount[i]
            Ei = freqTable[i]*len(text)
            result += ((Ci-Ei)**2)/Ei
    else:
        result = math.inf
    return result


#-----------------------------------------------------------
# Parameters:   text (string), blockSize (int)
# Return:       list [floats]
# Description:  breaks a string up into chunks of blockSize
#-----------------------------------------------------------
def chunk(text, blockSize):
    return [text[i:i+blockSize] for i in range(0, len(text), blockSize)]

#-----------------------------------------------------------
# Parameters:   text (string), blockSize (int)
# Return:       list of chi values per block 
# Description:  Reads a given dictionary file
#-----------------------------------------------------------


def block_chiSquared(text, blockSize):
    print(text)
    textList = chunk(text, blockSize)
    chiValues = []
    for textChunk in textList:
        x = get_chiSquared(textChunk)
        print("x value is:",x)
        chiValues.append(x)
    
    return chiValues

#-----------------------------------------------------------
# Parameters:   dictFile (string): filename
# Return:       list of words (list)
# Description:  Reads a given dictionary file
#               dictionary file is assumed to be formatted: each word in a separate line
#               Returns a list of strings, each pertaining to a dictionary word
#-----------------------------------------------------------


def load_dictionary(dictFile):
    inFile = open(dictFile, 'r', encoding=" ISO-8859-15")
    dictList = inFile.readlines()
    i = 0
    for word in dictList:
        dictList[i] = word.strip('\n')
        i += 1
    inFile.close()
    return dictList

#-------------------------------------------------------------------
# Parameters:   text (string)
# Return:       list of words (list)
# Description:  Reads a given text
#               Each word is saved as an element in a list.
#               Returns a list of strings, each pertaining to a word in file
#               Gets rid of all punctuation at the start and at the end
#-------------------------------------------------------------------


def text_to_words(text):
    wordList = []
    lines = text.split('\n')
    for line in lines:
        line = line.strip('\n')
        line = line.split(' ')
        for i in range(len(line)):
            if line[i] != '':
                line[i] = line[i].strip(string.punctuation)
                wordList += [line[i]]
    return wordList


#-----------------------------------------------------------
# Parameters:   ciphertext (string)
#               dictFile (string): dictionary file
# Return:       ciphertext (string)
# Description:  strips all trailing q's from a ciphertext
#-----------------------------------------------------------

def strip_trailing_Q(ciphertext):
    return ciphertext.rstrip('q')


#-----------------------------------------------------------
# Parameters:   text (string)
#               dictFile (string): dictionary file
# Return:       (#matches, #mismatches)
# Description:  Reads a given text, checks if each word appears in dictionary
#               Returns a tuple of number of matches and number of mismatches.
#               Words are compared in lowercase.
#-----------------------------------------------------------


def analyze_text(text, dictFile):
    dictList = load_dictionary(dictFile)
    wordList = text_to_words(text)
    matches = 0
    mismatches = 0
    for word in wordList:
        if word.lower() in dictList:
            matches += 1
        else:
            mismatches += 1
    return(matches, mismatches)

#-----------------------------------------------------------
# Parameters:   text (string)
#               dictFile (string): dictionary file
#               threshold (float): number between 0 to 1
# Return:       True/False
# Description:  Check if a given file is a plaintext
#               If #matches/#words >= threshold --> True
#                   otherwise --> False
#               If invalid threshold given, default is 0.9
#               An empty string is assumed to be non-plaintext.
#-----------------------------------------------------------


def is_plaintext(text, dictFile, threshold):
    if text == '':
        return False
    result = analyze_text(text, dictFile)
    percentage = result[0]/(result[0]+result[1])
    if threshold < 0 or threshold > 1:
        threshold = 0.9
    if percentage >= threshold:
        return True
    return False

#-------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key: (shifts,direction) (int,str)
# Return:       ciphertext (string)
# Description:  Encryption using Shfit Cipher (Monoalphabetic Substitituion)
#               The alphabet is shfited as many as "shifts" using given direction
#               Non alpha characters --> no substitution
#               Valid direction = 'l' or 'r'
#               Algorithm preserves case of the characters
#---------------------------------------------------------------------------------------


def e_shift(plaintext, key):
    alphabet = get_lower()

    shifts, direction = key
    if shifts < 0:
        shifts *= -1
        direction = 'l' if key[1] == 'r' else 'r'
    shifts = key[0] % 26
    shifts = shifts if key[1] == 'l' else 26-shifts

    ciphertext = ''
    for char in plaintext:
        if char.lower() in alphabet:
            plainIndx = alphabet.index(char.lower())
            cipherIndx = (plainIndx + shifts) % 26
            cipherChar = alphabet[cipherIndx]
            ciphertext += cipherChar.upper() if char.isupper() else cipherChar
        else:
            ciphertext += char
    return ciphertext

#-------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key: (shifts,direction) (int,str)
# Return:       ciphertext (string)
# Description:  Decryption using Shfit Cipher (Monoalphabetic Substitituion)
#               The alphabet is shfited as many as "shifts" using given direction
#               Non alpha characters --> no substitution
#               Valid direction = 'l' or 'r'
#               Algorithm preserves case of the characters
#               Trick: Encrypt using same #shifts but the other direction
#---------------------------------------------------------------------------------------


def d_shift(ciphertext, key):
    direction = 'l' if key[1] == 'r' else 'r'
    return e_shift(ciphertext, (key[0], direction))


def getFreq(ciphertext):

    freqList = [0] * 26
    alphabet = get_lower().upper()

    for c in ciphertext:
        if c.upper() in alphabet:
            freqList[alphabet.index(c.upper())] += 1
    
    for j in range(len(freqList)):
        freqList[j] = freqList[j] / len(ciphertext)


    returnList = []
    for i in range(len(alphabet)):
        returnList.append(tuple((alphabet[i], freqList[i])))
    
    return returnList




def compareFreq(engFreq, ciphFreq):
    matchingFreq = ['-']*26
    engFreq = get_freqTable()
    margin = 0.0005 #change this or pass it into the function

    for engLetter in engFreq:
        for ciphLetter in ciphFreq:
            if(engLetter - margin <= ciphLetter and engLetter + margin >= ciphLetter):
                matchingFreq[engFreq.index(engLetter)] = ciphLetter

    return matchingFreq



def d_freqSubstitution(ciphertext):
    alphabet = get_lower().upper()
    ciphFreq = getFreq(ciphertext)
    engFreq = get_freqTable()
    matchingFreq = compareFreq(engFreq, ciphFreq)
    print(matchingFreq)

    
def get_cipherType(ciphertext):
    # your code here
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print()
    strippedCipher = remove_nonalpha(ciphertext)
    #print(strippedCipher)

    I_english = 0.065
    margin = 0.003

    
    if(len(ciphertext) < 1):
        return 'Empty Ciphertext'
    I = get_indexOfCoin(ciphertext)
    #print("I is:", I)
    
    chi = get_chiSquared(ciphertext)
    #print("chi is:", chi)
    if(chi < 400):
        return "Spartan Scytale Cipher"
    elif(I > I_english - margin and I < I_english + margin):
        #print("ATBASH OR SHIFT CIPHER")
        temp = ''
        for c in strippedCipher:
            if(c in alphabet):
                #print("C IS DEFINITELY:", c)
                temp += alphabet[25- alphabet.index(c)]
            else:
                temp += c

        
        I_temp = get_indexOfCoin(temp)
        chi_Temp = get_chiSquared(temp)
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
    #print(ciphertext)
    strippedCipher = remove_nonalpha(ciphertext)
    
    counts = [0] * 21
    for i in range(1,21):
        s = shift_string(strippedCipher, i, 'r')
        
        matches = 0
        for j in range(i, len(s)):
            if strippedCipher[j] == s[j]:
                matches += 1
                counts[i] = matches
            
    #print(counts)
    maxN = counts[0]
    for num in counts:
        if num > maxN:
            maxN = num
    k = counts.index(maxN)
    return k



def d_vigenere2(ciphertext, key):
    # your code here
    square = get_vigenereSquare()
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


def vigenereInDictionary(ciphertext, keySize):
    decrypted = ''
    dictionary = load_dictionary('engmix.txt')
    i = 1
    for word in dictionary:
        print(i)
        i+=1
        if(len(word) == keySize):
            #print("correct length")
            temp = d_vigenere2(ciphertext, word)
            I = get_indexOfCoin(temp)
            if( I >= 0.063 and I <= 0.067):
                
                return word, temp
                
    return decrypted

def e_substitution(plaintext,key):
    # your code here
    baseString = get_baseString()
    subString   = key
    ciphertext = ''
    for plainChar in plaintext:
        upperFlag = True if plainChar.isupper() else False
        plainChar = plainChar.lower()
        if plainChar in baseString:
            indx = baseString.index(plainChar)
            cipherChar = subString[indx]
            cipherChar = cipherChar.upper() if upperFlag else cipherChar
        else:
             cipherChar = plainChar
        ciphertext += cipherChar
    return ciphertext

def d_substitution(ciphertext,key):
    # your code here
    plaintext = ''
    alphabet = get_baseString()

    for cipherChar in ciphertext:
        upperFlag = True if cipherChar.isupper() else False
        cipherChar = cipherChar.lower()
        if cipherChar in alphabet:
            indx = key.index(cipherChar)
            plainChar = alphabet[indx]
            plainChar = plainChar.upper() if upperFlag else plainChar
        else:
            plainChar = cipherChar
        plaintext+= plainChar
    
    return plaintext


def cryptanalysis_substitution(ciphertext):
    decrypt = ''
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    freqTable = get_freqTable()
    engFreq = []
    ciphFreq = getFreq(ciphertext)
    for i in range(len(alpha)):
        engFreq.append(tuple((alpha[i], freqTable[i])))


    engFreq.sort(key=lambda tup:tup[1], reverse=True)
    ciphFreq.sort(key=lambda tup:tup[1], reverse=True)
    #print(ciphFreq)
    substring = ''
    for i in range(len(alpha)):
        indx = 0
        for element in engFreq:
            if(element[0] == alpha[i]):
                indx = i
        char = ciphFreq[indx]
        substring+=char[0]
    print(substring)
    return decrypt


def e_vigenere1(plaintext, key):
    # your code here
    square = get_vigenereSquare()
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
    square = get_vigenereSquare()
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


def text_to_blocks(text,size):
    # your code here
    blocks = []
    for i in range(0, len(text),size):
        if(i + size > len(text)):
            blocks.append(text[i:len(text)])
        else:
            blocks.append(text[i:i+size])

    return blocks

def blocks_to_baskets(blocks):
    # your code here
    baskets = [''] * len(blocks[0])
    for block in blocks:
        for i in range(len(block)):
            baskets[i] +=(block[i])
    return baskets

def compare(str1, str2):
    for i in range(len(str1)):
        if(str1[i] != str2[i]):
            print("str1:", str1[i], ", str2:", str2[i])
    