#---------------------
#CP460 (Fall 2019)
#Noah Nichols
#---------------------
import cryptoUtil

#------------------------
#Parameters: plaintext(string)
#            key(string)
#Return:     ciphertext(string)
#Description:Encryption using Atbash cipher. There is no key (None)
#------------------------
def e_atbash(plaintext, key):
    ciphertext = ""
    alphabet = cryptoUtil.getAlphabet()

    for plainChar in plaintext:
        if plainChar.isalpha():
            upper = True if plainChar.isupper() else False
            cipherChar = alphabet[25- alphabet.index(plainChar.lower())]
            ciphertext+= cipherChar.upper() if upper else cipherChar
        else:
            ciphertext+=plainChar

    return ciphertext

def test_atbash():
    print("testing Atbash Cipher\n")
    plainTextFile = input("Enter plaintext file name: ")
    plaintext = cryptoUtil.file_to_text(plainTextFile)
    print("plaintext before encryption:")
    print(plaintext)
    print()

    ciphertext = e_atbash(plaintext, None)
    print("Ciphertext after encryption:")
    print(ciphertext)
    print()

    plaintext = d_atbash(ciphertext, None)
    print("Plaintext after decryption:")
    print(plaintext)
    print()

    return 


#------------------------
#Parameters: ciphertext(string)
#            key(string)
#Return:     plaintext(string)
#Description:Decryption using Atbash cipher. There is no key (None)
def d_atbash(ciphertext, key):
    plaintext = e_atbash(ciphertext, None)
    return plaintext


test_atbash()