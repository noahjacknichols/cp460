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
# Parameters:   fileName (string)
# Return:       contents (string)
# Description:  Utility function to read contents of a file
#               Can be used to read plaintext or ciphertext
#-----------------------------------------------------------


def file_to_text(fileName):
    inFile = open(fileName, 'r')
    contents = inFile.read()
    inFile.close()
    return contents


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
    print("text is: '_",text, "_'")
    charCount = get_charCount(text)
    if(text.strip() != ''):
        print("length is",len(charCount))
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
    
    for indice in freqList:
        indice = indice / len(ciphertext)
    
    return freqList




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

    

    
