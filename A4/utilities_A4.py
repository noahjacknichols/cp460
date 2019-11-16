#--------------------------
# CP460 Fall 2019
# Assignment 4
# Utilities
# DO NOT CHANGE THIS FILE
#--------------------------

import string
import math

# Included Functions
#   1- get_lower()
#   2- get_baseString()
#   3- load_dictionary(dictFile)
#   4- analyze_text(text, dictFile)
#   5- text_to_words(text)
#   6- is_plaintext(text, dictFile, threshold)
#   7- file_to_text(fileName)
#   8- text_to_file(fileName)
#   9- compare_files(file1,file2)
#   10- text_to_blocks(text,size)
#   11- remove_nonalpha(text)
#   12- get_nonalpha(text)
#   13- insert_nonalpha(text, nonAlpha)

#-----------------------------------------------------------
# Parameters:   None 
# Return:       alphabet (string)
# Description:  Return a string of lower case alphabet
#-----------------------------------------------------------
def get_lower():
    return "".join([chr(ord('a')+i) for i in range(26)])

#-----------------------------------------------------------
# Parameters:   None 
# Return:       baseString (string)
# Description:  Return a string composed of:
#               alphabet (lower case) (26 symbols)
#               space
#               digits (10 symbols)
#               punctuations (defined in string library) (32 symbols)
#               new line character
#               Total number of characters = 70

#-----------------------------------------------------------
def get_baseString():
    alphabet = get_lower() # 26 symbols
    nums = ''.join([str(i) for i in range(10)]) #10 sybmols
    punctuations = string.punctuation #32 sybmols
    return alphabet + ' '+nums + punctuations + '\n'  #70 symbols

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
# Parameters:   text (string)
#               filename (string)            
# Return:       none
# Description:  Utility function to write any given text to a file
#               If file already exist, previous content will be over-written
#-----------------------------------------------------------
def text_to_file(text, filename):
    outFile = open(filename,'w')
    outFile.write(text)
    outFile.close()
    return

#-----------------------------------------------------------
# Parameters:   dictFile (string): filename
# Return:       list of words (list)
# Description:  Reads a given dictionary file
#               dictionary file is assumed to be formatted: each word in a separate line
#               Returns a list of lists, list[0] contains all words starting with 'a'
#               list[1] all words starting with 'b' and so forth.
#-----------------------------------------------------------
def load_dictionary(dictFile):
    alphabet = get_lower()
    inFile = open(dictFile, 'r',encoding=" ISO-8859-15") 
    dictWords = inFile.readlines()
    dictList = [[] for i in range(26)]
    for w in dictWords:
        word = w.strip('\n')
        dictList[alphabet.index(word[0])]+=[word]
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
                wordList+=[line[i]]
    return wordList

#-----------------------------------------------------------
# Parameters:   text (string)
#               dictList (list of lists)
# Return:       (#matches, #mismatches)
# Description:  Reads a given text, checks if each word appears in dictionary
#               Returns a tuple of number of matches and number of mismatches.
#               Words are compared in lowercase.
#-----------------------------------------------------------
def analyze_text(text, dictList):
    wordList = text_to_words(text)
    alphabet = get_lower()
    matches = 0
    mismatches = 0
    for w in wordList:
        if w.isalpha():
            listNum = alphabet.index(w[0].lower())
            if w.lower() in dictList[listNum]:
                matches+=1
            else:
                mismatches+=1
        else:
            mismatches+=1
    return(matches,mismatches)

#-----------------------------------------------------------
# Parameters:   text (string)
#               dictList (list of lists)
#               threshold (float): number between 0 to 1
# Return:       True/False
# Description:  Check if a given file is a plaintext
#               If #matches/#words >= threshold --> True
#                   otherwise --> False
#               If invalid threshold given, default is 0.9
#               An empty string is assumed to be non-plaintext.
#-----------------------------------------------------------
def is_plaintext(text, dictList, threshold):
    if text == '':
        return False
    result = analyze_text(text, dictList)
    percentage = result[0]/(result[0]+result[1])
    if threshold < 0 or threshold > 1:
        threshold = 0.9
    if percentage >= threshold:
        return True
    return False

#-----------------------------------------------------------------------------
# Parameters:   text (string)
#               size (int)
# Return:       list of strings
# Description:  Break a given string into strings of given size
#               Result is provided in a list
#------------------------------------------------------------------------------
def text_to_blocks(text,size):
    return [text[i*size:(i+1)*size] for i in range(math.ceil(len(text)/size))]

#-----------------------------------------------------------------------------
# Parameters:   file1 (string)
#               file2 (string)
# Return:       Comparison Result
# Description:  Compares contents of file1 against contents of file2
#               if identical --> return 'Identical'
#               if non-identical --> return line number where mismatch occured
#------------------------------------------------------------------------------
def compare_files(file1,file2):
    f1 = open(file1,'r')
    f2 = open(file2,'r')
    counter = 1
    line1 = 'a'
    line2 = 'b'
    while True:
        line1 = f1.readline()
        line2 = f2.readline()
        if line1 == '' and line2 == '':
            return 'Identical'
        if line1 != line2:
            return 'Mismatch Line '+str(counter)
        counter+=1 
    f1.close()
    f2.close()
    return

#-----------------------------------
# Parameters:   text (string)
# Return:       modifiedText (string)
# Description:  Removes all non-alpha characters from the given string
#               Returns a string of only alpha characters
#-----------------------------------
def remove_nonalpha(text):
    modifiedText = ''
    for char in text:
        if char.isalpha():
            modifiedText += char
    return modifiedText

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
    nonalphaList = []
    for i in range(len(text)):
        if not text[i].isalpha():
            nonalphaList.append([text[i],i])
    return nonalphaList

#-----------------------------------
# Parameters:   text (str)
#               2D list: [[char1,pos1], [char2,pos2],...]
# Return:       modifiedText (string)
# Description:  inserts a list of nonalpha characters in the positions
#-----------------------------------
def insert_nonalpha(text, nonAlpha):
    modifiedText = text
    for item in nonAlpha:
        modifiedText = modifiedText[:item[1]]+item[0]+modifiedText[item[1]:]
    return modifiedText
