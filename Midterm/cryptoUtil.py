#---------------------
#CP460 (Fall 2019)
#Noah Nichols
#---------------------
import string
import itertools

#------------------------
#Parameters: None
#Return:     alphabet (string)
#Description:Return a string containing lower case alphabet
#------------------------
def getAlphabet():

    #Method 1: through string library
    #alphabet = string.ascii_lowercase()

    #Method 2: standard for loop
    #alphabet = ""
    # for i in range(26):
    #     charNum = ord('a') + i
    #     char = chr(charNum)
    #     alphabet+=char
    # return alphabet

    #method 3: list comprehension
    alphabet = "".join([chr(ord('a')+i) for i in range(26)])
    return alphabet

#------------------------
#Parameters: filename (string)
#Return:     text (string)
#Description:Read the entire contents of a given file
#            return a string of the contents
#------------------------
def file_to_text(filename):
    inFile = open(filename, 'r')
    contents = inFile.read()
    inFile.close()
    return contents


#------------------------
#Parameters: text (string), filename (string)
#Return:     None
#Description:write text to a given file
#------------------------
def text_to_file(text, filename):
    outFile = open(filename, 'w')
    outFile.write(text)
    outFile.close()
    return

def get_string_perm(s):
    #method 1: built-in function
    permList = list(itertools.permutations(s))
    for i in range(len(permList)):
        permList[i] = "".join(permList[i])
    return permList