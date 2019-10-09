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

    keys = ['35', 'R', 'ON', 'Jug', 'FORD',
            'PEACE', 'Jellyfish', 'ENVIORNMENT']

    for key in keys:
        ciphertext = ''
        plaintext2 = ''
        print('Key: ', key)
        print('Encryption:')
        ciphertext = solution_A2.e_vigenere(plaintext, key)
        print(ciphertext[:100])
        print('Decrpyption:')
        plaintext2 = solution_A2.d_vigenere(ciphertext, key)
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
        print('remove_nonalpha (converted to upper case):')
        c = c.upper()
        print(c)
        blocks = solution_A2.text_to_blocks(c, len(keys[i]))
        print('Blocks =')
        print(blocks)
        baskets = solution_A2.blocks_to_baskets(blocks)
        print('Baskets =')
        print(baskets)
        I = solution_A2.get_indexOfCoin(c)
        print('I = {:.5f}'.format(I))
        k1 = solution_A2.getKeyL_friedman(c)
        print('Key Length (Friedman) = ', k1)
        k2 = solution_A2.getKeyL_shift(c)
        print('Key Length (Shift) = ', k2)
        print()

    print("-------------------------------------------")
    print()
    return

#----------------------------------------------------
# Test Q3: Block Rotation Cipher
#---------------------------------------------------


def test_q3():
    print("-------------------------------------------")
    print("Testing Q3: Block Rotation Cipher")
    print()

    print('Testing adjust Key:')
    print('({},{})\t--> '.format(4, 3.5), end='')
    print('{}'.format(solution_A2.adjustKey_blockRotate((4, 3.5))))
    print('{}\t--> '.format([4, 5]), end='')
    print('{}'.format(solution_A2.adjustKey_blockRotate([4, 5])))
    print('{}\t--> '.format(10), end='')
    print('{}'.format(solution_A2.adjustKey_blockRotate(10)))
    print('({},{})\t--> '.format(-2, 1), end='')
    print('{}'.format(solution_A2.adjustKey_blockRotate((-2, 1))))
    print('({},{})\t--> '.format(5, 7), end='')
    print('{}'.format(solution_A2.adjustKey_blockRotate((5, 7))))
    print('({},{})\t--> '.format(3, 11), end='')
    print('{}'.format(solution_A2.adjustKey_blockRotate((3, 11))))
    print('({},{})\t--> '.format(7, -6), end='')
    print('{}'.format(solution_A2.adjustKey_blockRotate((7, -6))))
    print()

    print('Testing get_nonalpha:')
    inputStr = 'Done'
    print('{} --> {}'.format(inputStr, solution_A2.get_nonalpha(inputStr)))
    inputStr = 'Wonderful!'
    print('{} --> {}'.format(inputStr, solution_A2.get_nonalpha(inputStr)))
    inputStr = 'Do you have 3 cents?'
    print('{} --> {}'.format(inputStr, solution_A2.get_nonalpha(inputStr)))
    print()

    print('Testing insert_nonalpha:')
    inputStr = 'Done'
    nonalpha = []
    print('{} into {} --> {}'.format(nonalpha, inputStr,
                                     solution_A2.insert_nonalpha(inputStr, nonalpha)))
    inputStr = 'Wonderful'
    nonalpha = [['!', 9]]
    print('{} into {} --> {}'.format(nonalpha, inputStr,
                                     solution_A2.insert_nonalpha(inputStr, nonalpha)))
    inputStr = 'ABCDEF'
    nonalpha = [['1', 0], [' ', 2], ['$', 5], ['?', 100]]
    print('{} into {} --> {}'.format(nonalpha, inputStr,
                                     solution_A2.insert_nonalpha(inputStr, nonalpha)))
    print()

    print('Testing e_blockRotate and d_blockRotate:')
    key = (4, 3)
    print('Key = ', key)
    plaintext = utilities_A2.get_lower()
    print('plaintext = ', end='\t\t')
    print(plaintext)
    ciphertext = solution_A2.e_blockRotate(plaintext, key)
    print('After encryption:', end='\t')
    print(ciphertext)
    print('After Decryption:', end='\t')
    recovered = solution_A2.d_blockRotate(ciphertext, key)
    print(recovered)
    print()

    key = (10, 6)
    print('Key = ', key)
    plaintext = 'The internet, our greatest tool of emancipation, has been transformed into '
    plaintext += 'the most dangerous facilitator of totalitarianism we have ever seen'
    print('plaintext = ')
    print(plaintext)
    ciphertext = solution_A2.e_blockRotate(plaintext, key)
    print('After encryption:')
    print(ciphertext)
    print('After Decryption:')
    recovered = solution_A2.d_blockRotate(ciphertext, key)
    print(recovered)
    print()

    key = (8, 5)
    print('Key = ', key)
    plaintext = 'One must acknowledge with cryptography '
    plaintext += 'no amount of violence will ever solve a math problem.'
    print('plaintext = ')
    print(plaintext)
    ciphertext = solution_A2.e_blockRotate(plaintext, key)
    print('After encryption:')
    print(ciphertext)
    print('After Decryption:')
    recovered = solution_A2.d_blockRotate(ciphertext, key)
    print(recovered)
    print()

    print('Testing cryptanalysis_blockRotate:')
    ciphertext = 'andiUnderstch aingb-locko ugonm ake sy ssy, omadun leo urous tart yqq qqwncultq'
    print('Ciphertext:')
    print(ciphertext)
    print('Cryptanalysis Result:')
    plaintext, key = solution_A2.cryptanalysis_blockRotate(ciphertext, 2, 15)
    print()

    ciphertext = utilities_A2.file_to_text('ciphertext1.txt')
    print('Contents of Ciphertext1:')
    print(ciphertext)
    print('Cryptanalysis Result:')
    plaintext, key = solution_A2.cryptanalysis_blockRotate(ciphertext, 2, 10)
    print()

    ciphertext = utilities_A2.file_to_text('ciphertext2.txt')
    print('Contents of Ciphertext2:')
    print(ciphertext)
    print('Cryptanalysis Result:')
    plaintext, key = solution_A2.cryptanalysis_blockRotate(ciphertext, 2, 20)
    print()

    print("-------------------------------------------")
    return

#----------------------------------------------------
# Test Q4: Cipher Detector
#----------------------------------------------------


def test_q4():
    print("-------------------------------------------")
    print("Testing Q4: Cipher Detector")
    print('Cipher Type for an Empty String  :', end=' ')
    print(solution_A2.get_cipherType(''))
    for i in range(2, 9):
        filename = 'ciphertext'+str(i)+'.txt'
        ciphertext = utilities_A2.file_to_text(filename)
        print('Cipher Type for ', filename, ':', end=' ')
        print(solution_A2.get_cipherType(ciphertext))
    print("-------------------------------------------")
    return

#----------------------------------------------------
# Test Q5:
#----------------------------------------------------


def test_q5():
    print("-------------------------------------------")
    print("Testing Q5: Playfair Square Cipher")
    print()

    texts = ['No Dust', 'Mill Bed', 'Border Line']
    square = utilities_A2.get_playfairSquare()

    for text in texts:
        print('{}\t{}'.format('Input Text', text))
        plainStream = solution_A2.formatInput_playfair(text)
        print('{}\t{}'.format('plaintext:', plainStream))
        ciphertext = solution_A2.e_playfair(text, square)
        print('{}\t{}'.format('ciphertext:', ciphertext))
        plaintext = solution_A2.d_playfair(ciphertext, square)
        print('{}\t{}'.format('plaintext:', plaintext))
        print()

    print("-------------------------------------------")
    return
