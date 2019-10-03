#--------------------------
# CP460 (Fall 2019)
# Assignment 1 Testing File
#--------------------------

import solution_A2
import utilities_A2

#----------------------------------------------------
# Test Q1: Vigenere Cipher (Version 2)
#---------------------------------------------------
def test_q1():
    print("-------------------------------------------")
    print("Testing Q1: Vigenere Cipher 1")
    print()

    print('Reading plaintext:')
    plaintext = utilities_A2.file_to_text('plaintext1.txt')
    print(plaintext[:100])
    print()
    
    keys = ['35','R','ON','Jug','FORD','PEACE','Jellyfish','ENVIORNMENT']

    for key in keys:
        ciphertext = ''
        plaintext2 = ''
        print('Key: ',key)
        print('Encryption:')
        ciphertext = solution_A2.e_vigenere(plaintext,key)
        print(ciphertext[:100])
        print('Decrpyption:')
        plaintext2 = solution_A2.d_vigenere(ciphertext,key)
        print(plaintext2[:100])
        print()
        
    print("-------------------------------------------")
    print()
    return

#----------------------------------------------------
# Test Q2: Vigenere Cryptanalysis Utilities
#---------------------------------------------------
def test_q2():
    print("-------------------------------------------")
    print("Testing Q2: Vigenere Cryptanalysis Utilities")
    print()

    keys = ['tap', 'crypto', 'joyfulday']
    cipher = utilities_A2.file_to_text('ciphertext1.txt')
    ciphertext = cipher.split('\n')
    for i in range(len(ciphertext)):
        c = solution_A2.remove_nonalpha(ciphertext[i])
        print('remove_nonalpha:')
        print(c)
        blocks = solution_A2.text_to_blocks(c,len(keys[i]))
        print('Blocks =')
        print(blocks)
        baskets = solution_A2.blocks_to_baskets(blocks)
        print('Baskets =')
        print(baskets)
        I = solution_A2.get_indexOfCoin(c)
        print('I = {:.5f}'.format(I))
        k1 = solution_A2.getKeyL_friedman(c)
        print('Key Length (Friedman) = ',k1)
        k2 = solution_A2.getKeyL_shift(c)
        print('Key Length (Shift) = ',k2)
        print()
    
    print("-------------------------------------------")
    print()
    return

#----------------------------------------------------
# Test Q3: 
#---------------------------------------------------
def test_q3():
    print("-------------------------------------------")
    print("Testing Q3: ")
    print()
    

    print()
    print("-------------------------------------------")
    return

#----------------------------------------------------
# Test Q4:
#----------------------------------------------------
def test_q4():
    print("-------------------------------------------")
    print("Testing Q4: ")
    print()

    print("-------------------------------------------")
    return
    
#----------------------------------------------------
# Test Q5: 
#----------------------------------------------------
def test_q5():
    print("-------------------------------------------")
    print("Testing Q5: ")
    print()

    print("-------------------------------------------")
    return
