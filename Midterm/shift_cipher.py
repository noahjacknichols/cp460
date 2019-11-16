def e_shift(plaintext, key):
    alphabet = get_lower()
    ciphertext = ''
    shifts, direction = key
    if shifts < 0:
        shifts*=-1
        direction = 'l' if direction == 'r' else 'r'
    shifts = shifts % 26
    shifts = shifts if direction == 'l' else 26-shifts
    ciphertext = ''
    for char in plaintext:
        if char.lower() in alphabet:
            plainIndx = alphabet.index(char.lower())
            cipherIndx = (plainIndx + shifts)%26
            cipherChar = alphabet[cipherIndx]
            ciphertext+= cipherChar.upper() if char.isupper() else cipherChar

    return ciphertext

def d_shift(ciphertext, key):
    direction = 'l' if key[1] == 'r' else 'r'
    return e_shift(ciphertext, (key[0], direction))

def cryptanalysis_shift(ciphertext):
    alphabet = get_lower()
    for i in range(26):
        plaintext = d_shift(ciphertext, (i, 'l'))
        if is_plaintext(plaintext, "engmix.txt", 0.8):
            print("key found:", (i, 'l'))
            return (i, 'l'), plaintext
    print("Cryptanalysis failed! No key found.")
    return '', ''


def cryptanalysis2_shift(ciphertext):
    charCount = get_charCount(ciphertext)
    alphabet = get_lower()

    maxChar = 0

    for i in range(1, len(charCount)):
        if charCount[i] > charCount[maxChar]:
            maxChar = i

    freqLetter = ['e','t','a']
    for letter in freqLetter:
        key = alphabet.index(alphabet[maxChar]) - alphabet.index(letter)
        key = (key*-1, 'r') if key < 0 else (key, 'l')
        plaintext = d_shift(ciphertext, key)
        if is_plaintext(plaintext, "engmix.txt", 0.8):
            print('Key found:', key, '\nplaintext:', plaintext)
            return key, plaintext
    print('Cryptanalyssi failed! No key found')
    return '',''

def cryptanalys3_shift(ciphertext):
    chiList = [get_chiSquared(d_shift(ciphertext, (i,'l'))) for i in range(26)]
    key = chiList.index(min(chiList))
    key = (key, 'l')
    plaintext = d_shift(ciphertext, key)
    return key, plaintext
    


def get_freqTable():
    freqTable = [0.08167,0.01492,0.02782, 0.04253, 0.12702,0.02228, 0.02015,
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
    0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
    return freqTable


def get_chiSquared(text):
    freqtable = get_freqTable()
    charCount = get_charCount(text)
    result = 0
    for i in range(26):
        Ci = charCount[i]
        Ei = freqTable[i]*len(text)
        result+= ((Ci-Ei) **2)/Ei
    return result

def e_ROT13(plaintext, key):
    return e_shift(plaintext, (13,'l'))

def d_ROT13(ciphertext, key):
    return e_ROT13(ciphertext, key)
