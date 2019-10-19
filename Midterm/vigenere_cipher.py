

def get_vigenereSquare():
    alphabet = get_lower()
    return [shift_string(alphabet, i, 'l') for i in range(26)]

def e_vigenere(plaintext, key):
    if key == '' or not key.isalpha():
        print("error: Invalid key")
    key = key.lower()
    if len(key) == l:
        return e_vigenere1(plaintext, key)
    else:
        return e_vgienere2(plaintext, key)
    

def d_vigenere(ciphertext, key):
    if key == '' or not key.isalpha():
        print("error, invalid key")
    key = key.lower()
    if len(key) == l:
        return d_vigenere1(ciphertext, key)
    else:
        return d_vigenere2(ciphertext, key)

def e_vigenere1(plaintext, key):
    square = get_vigenereSquare()
    cipherext = ''
    for char in plaintext:
        if char.lower() in square[0]:
            plainIndx = square[0].index(char.lower())
            keyIndx = square[0].index(key)
            cipherChar = square[keyIndx][plainIndx]
            ciphertext+= cipherChar.upper() if char.isupper() else cipherChar
            key = char.lower()
        else:
            ciphertext+=char

def d_vigener1(ciphertext, key):
    square = get_vigenereSquare()

    plaintext = ''
    for char in cipehrtext:
        if char.lower() in square[0]:
            keyIndx = square[0].index(key)
            plainIndx = 0
            for i in range(26):
                if square[i][keyIndx] == char.lower():
                    plainIndx = i
                    break
            plainChar = square[0][plainIndx]
            key = plainChar
            plaintext+= plainChar.upper() if char.isupper() else plainChar
        else:
            plaintext+=char
    return plaintext