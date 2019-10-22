#--------------------------
# CP460 (Fall 2019)
# Midterm (Testing File)
#--------------------------

#-----------------------------------------------
# DO NOT CHANGE THE CONTENTS OF THIS FILE
# ----------------------------------------------

#----------------------------------------------
import solution
import utilities
#----------------------------------------------

# main function: Call this function for testing
def main():
    print('------------- File Matching -------------')
    files = solution.match_files()
    print()

    print('------------- Vigenere Cipher -------------')
    test_q1(files[0][0],files[0][1])
    print()

    print('---------- Substitution Cipher ------------')
    test_q2(files[1][0],files[1][1])
    print()

    print('------------- Xshift Cipher -------------')
    test_q3(files[2][0],files[2][1])
    print()
    
    print('------------- Xcrypt Cipher -------------')
    test_q4(files[3][0],files[3][1])
    print()

    return

# Q1: Vigenere Cipher
def test_q1(file1,file2):
    print('Testing Encryption/decryption against sample file:')
    plaintext   = utilities.file_to_text('plaintext_vigenere_sample.txt')
    ciphertext  = utilities.file_to_text('ciphertext_vigenere_sample.txt')
    key = 'disposition'
    ciphertext2 = solution.e_vigenere(plaintext,key)
    if ciphertext == ciphertext2:
        print('\tEncryption Successful')
    else:
        print('\tEncryption failed')
    plaintext2 = solution.d_vigenere(ciphertext2,key)
    if plaintext == plaintext2:
        print('\tDecryption Successful')
    else:
        print('\tDecryption failed')
    print()
    print('Cryptanalysis for Sample File:')
    key,plaintext = solution.cryptanalysis_vigenere(ciphertext)
    print('found key = ',key)
    print()

    plaintext = ''
    ciphertext = ''
    ciphertext2 = ''
    plain1 = file1
    cipher1 = file2
    key = 0
    ciphertext = utilities.file_to_text(cipher1)
    print('Cryptanalysis of {}:'.format(cipher1))
    key,plaintext = solution.cryptanalysis_vigenere(ciphertext)
    print('Key found: ',key)
    print()
    print('Plaintext:')
    print(plaintext[:150])
    print()
    print('Verifying cryptanalysis results: ',end='')
    ciphertext2 = solution.e_vigenere(plaintext,key)
    if ciphertext == ciphertext2:
        print('OK')
    else:
        print('Something is not right!')
    print()

    solution.comments_q1()
    return

# Q2: Substitution Cipher
def test_q2(file1,file2): 
    print('Testing Encryption/decryption against sample file:')
    plaintext   = utilities.file_to_text('plaintext_subcipher_sample.txt')
    ciphertext  = utilities.file_to_text('ciphertext_subcipher_sample.txt')
    key = utilities.adjust_key("""poejiqsrbltxwaznfcdhmvgkuy:'" !.?,-#;""")
    ciphertext2 = solution.e_substitution(plaintext,key)
    if ciphertext == ciphertext2:
        print('\tEncryption Successful')
    else:
        print('\tEncryption failed')
    plaintext2 = solution.d_substitution(ciphertext2,key)
    if plaintext == plaintext2:
        print('\tDecryption Successful')
    else:
        print('\tDecryption failed')
    print()

    # this is given you do not need to do anything for it
    print('Cryptanalysis for Sample File:') 
    key = '''poejiqsrbltxwaznfcdhmvgkuy:'" !.?,-#;'''
    print('found key = ',key)
    print()

    # Cryptanalysis of your file
    plaintext = ''
    ciphertext = ''
    ciphertext2 = ''
    plain1 = file1
    cipher1 = file2
    key = 0
    ciphertext = utilities.file_to_text(cipher1)
    print('Cryptanalysis of {}:'.format(cipher1))
    key,plaintext = solution.cryptanalysis_substitution(ciphertext)
    print('Key found: ',utilities.adjust_key(key))
    print()
    print('Plaintext:')
    print(plaintext[:150])
    print()
    print('Verifying cryptanalysis results: ',end='')
    ciphertext2 = solution.e_substitution(plaintext,key)
    if ciphertext == ciphertext2:
        print('OK')
    else:
        print('Something is not right!')
    print()

    solution.comments_q2()
    return


# Q3: Xshift Cipher
def test_q3(file1,file2): 
    print('Testing Encryption/decryption against sample file:')
    plaintext   = utilities.file_to_text('plaintext_xshift_sample.txt')
    ciphertext  = utilities.file_to_text('ciphertext_xshift_sample.txt')
    key = ('ABCDEFGHIJKLMNOPQRSTUVWXYZzyxwvutsrqponmlkjihgfedcba',30)
    ciphertext2 = solution.e_xshift(plaintext,key)
    if ciphertext == ciphertext2:
        print('\tEncryption Successful')
    else:
        print('\tEncryption failed')
    plaintext2 = solution.d_xshift(ciphertext2,key)
    if plaintext == plaintext2:
        print('\tDecryption Successful')
    else:
        print('\tDecryption failed')
    print()
    print('Cryptanalysis for Sample File:')
    key,plaintext = solution.cryptanalysis_xshift(ciphertext)
    print('found key = ',key)
    print()

    plaintext = ''
    ciphertext = ''
    ciphertext2 = ''
    plain4 = file1
    cipher4 = file2
    key = 0
    ciphertext = utilities.file_to_text(cipher4)
    print('Cryptanalysis of {}:'.format(cipher4))
    key,plaintext = solution.cryptanalysis_xshift(ciphertext)
    print('Key found: ',key)
    print()
    print('Plaintext:')
    print(plaintext[:500])
    print()
    print('Cryptanalysis Successful? ',end='')
    ciphertext2 = solution.e_xshift(plaintext,(key[0],int(key[1])))
    if ciphertext == ciphertext2:
        print('Yes')
    else:
        print('No')
    print()

    solution.comments_q3()
    return
    
# Q4: Xcrypt Cipher
def test_q4(file1,file2):
    print('Testing encryption over sample file:')
    plaintext   = utilities.file_to_text('plaintext_xcrypt_sample.txt')
    ciphertext  = utilities.file_to_text('ciphertext_xcrypt_sample.txt')
    key = 82
    ciphertext2 = solution.e_xcrypt(plaintext,key)
    if ciphertext == ciphertext2:
        print('Encryption Successful')
    else:
        print('Encryption failed')
    plaintext2 = solution.d_xcrypt(ciphertext2,key)
    if plaintext == plaintext2:
        print('Decryption Successful')
    else:
        print('Decryption failed')
    print()
    
    print('Testing decryption over sample file:')
    plaintext2 = solution.d_xcrypt(ciphertext2,key)
    if plaintext == plaintext2:
        print('Decryption Successful')
    else:
        print('Decryption failed')
    print()
    
    plaintext = ''
    ciphertext = ''
    ciphertext2 = ''
    plain4 = file1
    cipher4 = file2
    key = 0
    ciphertext = utilities.file_to_text(cipher4)
    print('Cryptanalysis of {}:'.format(cipher4))
    key,plaintext = solution.cryptanalysis_xcrypt(ciphertext)
    print('Key found: ',key)
    print()
    print('Plaintext:')
    print(plaintext[:150])
    print()
    print('Cryptanalysis Successful? ',end='')
    ciphertext2 = solution.e_xcrypt(plaintext,key)
    if ciphertext == ciphertext2:
        print('Yes')
    else:
        print('No')
    print()

    solution.comments_q4()
    return

