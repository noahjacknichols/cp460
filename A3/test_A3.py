#--------------------------
# CP460 (Fall 2019)
# Assignment 3 Testing File
#--------------------------

import solution_A3
import utilities_A3

#----------------------------------------------------
# Test Q1: Columnar Transposition
#---------------------------------------------------
def test_q1():
    print("-------------------------------------------")
    print("Testing Q1: Columnar Transposition")
    print()

    print('Testing get_keyOrder_columnarTrans:')
    keys = [34, ['O','N'],'', '034','?=!', 'r','K','Dad','Face','apple','good day','German']
    for key in keys:
        print('Key order for {} ='.format(key),end=' ')
        keyOrder = solution_A3.get_keyOrder_columnarTrans(key)
        print(keyOrder)

    print()
    print('Testing Encryption/Decryption:')
    key = 'German'
    print('key = ',key)
    plaintext = 'DEFENDEASTERNWALLOFTHECASTLE'
    print('plaintext =  ',plaintext)
    ciphertext = solution_A3.e_columnarTrans(plaintext,key)
    print('ciphertext = ',ciphertext)
    plaintext2 = solution_A3.d_columnarTrans(ciphertext,key)
    print('plaintext2 = ',plaintext2)
    print()

    key = 'Truth Seeker'
    print('key = ',key)
    print('Key order = {}'.format(solution_A3.get_keyOrder_columnarTrans(key)))
    print('plaintext1 =')
    plaintext = utilities_A3.file_to_text('plaintext1.txt')
    print(plaintext[:103])
    ciphertext = solution_A3.e_columnarTrans(plaintext,key)
    print('ciphertext = ')
    print(ciphertext[:103])
    plaintext2 = solution_A3.d_columnarTrans(ciphertext,key)
    print('plaintext2 = ')
    print(plaintext2[:103])
    print("-------------------------------------------")
    print()
    return
