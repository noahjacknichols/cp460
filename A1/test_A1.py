#--------------------------
# CP460 (Fall 2019)
# Assignment 1 Testing File
#--------------------------

import solution_A1

#----------------------------------------------------
# Test Q1: Spartay Scytale Cipher Decryption
#---------------------------------------------------
def test_q1():
    print("-------------------------------------------")
    print("Testing Q1: Decryption of Scytale Cipher")
    print()
    
    plaintext = ''
    ciphertext = ''
    key = 4
    plaintext = solution_A1.file_to_text("plaintext1.txt")  
    print("Plaintext1:", plaintext)
    ciphertext = solution_A1.e_scytale(plaintext,key)
    print("Encryption using (k =",key,"):", ciphertext)
    plaintext = solution_A1.d_scytale(ciphertext,key)
    print("Decryption using (k =",key,"):", plaintext)
    plaintext = solution_A1.d_scytale(ciphertext,8)
    print("Decryption using (k =",8,"):", plaintext)
    print()

    plaintext = ''
    ciphertext = ''
    key = 5
    plaintext = solution_A1.file_to_text("plaintext2.txt")  
    print("Plaintext2:", plaintext)
    ciphertext = solution_A1.e_scytale(plaintext,key)
    print("Encryption using (k =",key,"):", ciphertext)
    plaintext = solution_A1.d_scytale(ciphertext,key)
    print("Decryption using (k =",key,"):", plaintext)
    print()

    plaintext = ''
    ciphertext = ''
    key = 8
    plaintext = solution_A1.file_to_text("plaintext3.txt")  
    print("Plaintext3:\n", plaintext)
    ciphertext = solution_A1.e_scytale(plaintext,key)
    print("Encryption using (k =",key,"):\n", ciphertext)
    plaintext = solution_A1.d_scytale(ciphertext,key)
    print("Decryption using (k =",key,"):\n", plaintext)
    print()

    plaintext = ''
    ciphertext = ''
    key = 10
    ciphertext = solution_A1.file_to_text("ciphertext1.txt")
    plaintext = solution_A1.d_scytale(ciphertext,key)
    print("Decrypting ciphertext1 using (key =",key,"):\n")
    print(plaintext)
    
    print("-------------------------------------------")
    print()
    return

#----------------------------------------------------
# Test Q2: Plaintext Detection
#---------------------------------------------------
def test_q2():
    print("-------------------------------------------")
    print("Testing Q2: Plaintext Detection")
    print()

    dicList = solution_A1.load_dictionary("engmix.txt")
    print('Testing load_dictionary:')
    print("Word #111:\t",dicList[111])
    print("Word #2222:\t",dicList[2222])
    print("Word #2700:\t",dicList[2700])
    print("Word #35000:\t",dicList[35000])
    print("Word #64000:\t",dicList[64000])
    print()
    
    print("Testing text_to_words:")
    plaintext1 = solution_A1.file_to_text("plaintext1.txt")
    wordList = solution_A1.text_to_words(plaintext1)
    print("plaintext1:", wordList)

    plaintext2 = solution_A1.file_to_text("plaintext2.txt")
    wordList = solution_A1.text_to_words(plaintext2)
    print("plaintext2:")
    print(wordList)

    plaintext3 = solution_A1.file_to_text("plaintext3.txt")
    wordList = solution_A1.text_to_words(plaintext3)
    print("plaintext3:")
    print(wordList)
    print()

    print("Testing analyze_text:")
    result = solution_A1.analyze_text(plaintext2,"engmix.txt")
    print("Analyzing plaintext2:", result)
    result = solution_A1.analyze_text(plaintext3,"engmix.txt")
    print("Analyzing plaintext3:", result)
    plaintext4 = solution_A1.file_to_text("plaintext4.txt")
    result = solution_A1.analyze_text(plaintext4,"engmix.txt")
    print("Analyzing plaintext4:", result)
    ciphertext1 = solution_A1.file_to_text("ciphertext1.txt")
    result = solution_A1.analyze_text(ciphertext1,"engmix.txt")
    print("Analyzing ciphertext1:", result)
    print()
    
    print("Testing is_plaintext:")
    result = solution_A1.is_plaintext(plaintext2,"engmix.txt",0.85)
    print("plaintext2 (0.85):", result)
    result = solution_A1.is_plaintext(plaintext3,"engmix.txt",1.1)
    print("plaintext3 (1.10):", result)
    result = solution_A1.is_plaintext(plaintext3,"engmix.txt",0.96)
    print("plaintext3: (0.96)", result)
    result = solution_A1.is_plaintext(plaintext4,"engmix.txt",0.91)
    print("plaintext4: (0.91)", result)
    result = solution_A1.is_plaintext(plaintext4,"engmix.txt",0.82)
    print("plaintext4: (0.82)", result)
    result = solution_A1.is_plaintext(ciphertext1,"engmix.txt",0.7)
    print("ciphertext1: (0.7)", result)
    
    print("-------------------------------------------")
    print()
    return

#----------------------------------------------------
# Test Q3: Scytale Cipher Cryptanalysis
#---------------------------------------------------
def test_q3():
    print("-------------------------------------------")
    print("Testing Q3: Scytale Cipher Cryptanalysis")
    print()
    
    dictFile = "engmix.txt"
    cipherFile = "ciphertext1.txt"
    startKey = 4
    endKey = 300
    threshold = 0.8
    
    print('Case 1:',cipherFile, dictFile, startKey,'-',endKey, threshold,":")
    key = solution_A1.cryptanalysis_scytale(cipherFile,dictFile,startKey,endKey,threshold)
    print('Returned Key = ',key)
    print()

    startKey = 3
    endKey = 50
    threshold = 1.2
    print('Case 2:',cipherFile, dictFile, startKey,'-',endKey, threshold,":")
    key = solution_A1.cryptanalysis_scytale(cipherFile,dictFile,startKey,endKey,threshold)
    print('Returned Key = ',key)
    print()

    startKey = 7
    endKey = 70
    threshold = 0.8
    print('Case 3:',cipherFile, dictFile, startKey,'-',endKey, threshold,":")
    key = solution_A1.cryptanalysis_scytale(cipherFile,dictFile,startKey,endKey,threshold)
    print('Returned Key = ',key)
    print()

    startKey = 20
    endKey = 28
    threshold = 0.8
    print('Case 4:',cipherFile, dictFile, startKey,'-',endKey, threshold,":")
    key = solution_A1.cryptanalysis_scytale(cipherFile,dictFile,startKey,endKey,threshold)
    print('Returned Key = ',key)
    print()

    startKey = 7
    endKey = 17
    threshold = 0.9
    print('Case 5:',cipherFile, dictFile, startKey,'-',endKey, threshold,":")
    key = solution_A1.cryptanalysis_scytale(cipherFile,dictFile,startKey,endKey,threshold)
    print('Returned Key = ',key)
    print()

    startKey = 30
    endKey = 50
    threshold = 0.9
    cipherFile = "ciphertext2.txt"
    print('Case 6:',cipherFile, dictFile, startKey,'-',endKey, threshold,":")
    key = solution_A1.cryptanalysis_scytale(cipherFile,dictFile,startKey,endKey,threshold)
    print('Returned Key = ',key)
    print()
    print("-------------------------------------------")
    return

#----------------------------------------------------
# Test Q4: Polybius Square Encryption
#----------------------------------------------------
def test_q4():
    print("-------------------------------------------")
    print("Testing Q4: Polybius Square Encryption")
    print()

    print("Testing get_polybius_square")
    print("Polybius Square is:")
    print(solution_A1.get_polybius_square())
    print()

    plaintext = solution_A1.file_to_text("plaintext1.txt")
    print("plaintext1: ",plaintext)
    print("ciphertext: ",solution_A1.e_polybius(plaintext,None))
    print()

    plaintext = solution_A1.file_to_text("plaintext2.txt")
    print("plaintext2:")
    print(plaintext)
    print("ciphertext:")
    print(solution_A1.e_polybius(plaintext,None))
    print()

    plaintext = solution_A1.file_to_text("plaintext3.txt")
    print("plaintext3:")
    print(plaintext)
    print("ciphertext:")
    print(solution_A1.e_polybius(plaintext,None))
    print()

    print("-------------------------------------------")
    return
    
#----------------------------------------------------
# Test Q5: Polybius Square Decryption
#----------------------------------------------------
def test_q5():
    print("-------------------------------------------")
    print("Testing Q5: Polybius Square Decryption")
    print()
    
    print("Decrypting: 7561627411627411716865825362767412")
    ciphertext = '7561627411627411716865825362767412'
    plaintext = solution_A1.d_polybius(ciphertext,None)
    print(plaintext)
    print()

    print("Decrypting:")
    print('75616274\n6274\n716865825362767412\n')
    ciphertext = '75616274\n6274\n716865825362767412\n'
    plaintext = solution_A1.d_polybius(ciphertext,None)
    print(plaintext)

    print("Decrypting: 7561ABC5825362767412")
    ciphertext = '7561ABC5825362767412'
    plaintext = solution_A1.d_polybius(ciphertext,None)
    print(plaintext)

    print("Decrypting:")
    print('75616274\n6274\n71686582536277412\n')
    ciphertext = '75616274\n6274\n71686582536277412\n'
    plaintext = solution_A1.d_polybius(ciphertext,None)
    print(plaintext)
    
    print("Decrypting file ciphertext3.txt")
    ciphertext = solution_A1.file_to_text("ciphertext3.txt")
    plaintext = solution_A1.d_polybius(ciphertext,None)
    print(plaintext)
    print()

    print("-------------------------------------------")
    return
