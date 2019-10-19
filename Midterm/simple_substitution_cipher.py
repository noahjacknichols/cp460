#----------------
# CP460 Fall 2019
# Simple Subtitution Cipher
# Monoalphabetic Substitution
# Qutaiba Albluwi
#----------------

import random

#-----------------------------------------------------------
# Parameters:   None 
# Return:       alphabet (string)
# Description:  Return a string of lower case alphabet
#-----------------------------------------------------------
def get_lower():
    return "".join([chr(ord('a')+i) for i in range(26)])

#--------------------------------
# Parametes:    None
# Return:       baseString (str)
# Description:  Generates the base string that will be used in
#               simple sbustitution cipher, e.g. lower alphabet
#               should be modified for different usages
#----------------------------------
def get_baseString():
    return get_lower()

#--------------------------------
# Parametes:    baseString (str)
# Return:       randomKey (str)
# Description:  Generates a random key which is a random
#               order of the given baseString
#----------------------------------
def get_randomKey(baseString):
    key = ''
    baseList = list(baseString)
    counter = len(baseString)
    for i in range(counter):
        num = random.randint(0,len(baseList)-1)
        key+= baseList[num]
        baseList.remove(baseList[num])
    return key

#--------------------------------
# Parametes:    password (str)
#               baseString (str)
# Return:       Substitution key (str)
# Description:  Align the password (omit repeated chars) with basestring
#               The rest is the missing characters of the baseString
#----------------------------------
def get_subKey(password,baseString):
    subKey = ''
    
    for passChar in password:
        if passChar not in subKey:
            subKey+= passChar

    for baseChar in baseString:
        if baseChar not in subKey:
            subKey+= baseChar
            
    return subKey

#-----------------------------------------
# Parametes:    plaintext (str)
#               key (subString (str),baseString(str))
# Return:       ciphertext (str)
# Description:  Encryption using simple substitution Cipher
#               Key is a tuple of base string and substutition string
#               upper and lower case chars map to same char in baseline which is lower case)
#               characters not in base string are not encrypted
#-----------------------------------------
def e_substitution(plaintext,key):
    baseString  = key[0]
    subString   = key[1]

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

#-----------------------------------------
# Parametes:    ciphertext (str)
#               key (subString (str),baseString(str))
# Return:       plaintext (str)
# Description:  Decryption using simple substitution Cipher
#               Key is a tuple of base string and substutition string
#               upper and lower case chars map to same char in baseline which is lower case)
#               characters not in base string are not decrypted
#-----------------------------------------
def d_substitution(ciphertext,key):
    return e_substitution(ciphertext,(key[1],key[0]))

# valid commands: replace x with y
#                 end
def debug_substitution(ciphertext,baseString):
    subString = ['-' for i in range(len(baseString))]
    plaintext = ['-' for i in range(len(ciphertext))]
    print('Ciphertext:',ciphertext)
    print()
    command = input('Debug Mode: Enter Command: ')
    print()
    
    while command != 'end':
        subChar = command[8].lower()
        baseChar  = command[15].lower()

        if baseChar in baseString:
            indx = baseString.index(baseChar)
            subString[indx] = subChar
        else:
            print('(Error): Base Character does not exist!\n')

        print('Base:',end='')
        for i in range(len(baseString)):
            print('{} '.format(baseString[i]),end='')
        print()
        print('Sub :',end='')
        for i in range(len(subString)):
            print('{} '.format(subString[i]),end='')
        print('\n')

        print('ciphertext:',ciphertext)
        for i in range(len(plaintext)):
            if ciphertext[i].lower() == subChar:
                plaintext[i] = baseChar
        print('plaintext :',"".join(plaintext))
        command = input('Enter Command: ')
        print()
    return

#-----------------------------------

def test_substitution():
    baseString = get_lower()
    
    password = input('Enter password: ')
    subString = get_subKey(password.lower(),baseString)
    key = (baseString,subString)
    
    print('Base String:',baseString)
    print('SubString:  ',subString)

    plaintext = 'What are you doing today for lunch?'
    print('plaintext = ',plaintext)
    ciphertext = e_substitution(plaintext,key)
    print('ciphertext= ',ciphertext)
    plaintext2 = d_substitution(ciphertext,key)
    print('plaintext = ',plaintext2)
    print()

    return

def test_debug():
    ciphertext = 'Vwqp qni yjr ajchl pjaqy bjn frhtw?'
    baseString = get_lower()
    debug_substitution(ciphertext,baseString)
    return
