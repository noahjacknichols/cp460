import cryptoUtil

def get_outWheel(pointer):
    outWheel = cryptoUtil.get_lower().upper()
    for i in range(10):
        outWheel +=str(i)

    pointerIndex = outWheel.index(pointer)
    outWheel = cryptoUtil.shift)string(outWheel, pointerIndex, 'l')
    return outWheel

def get_inWheel(pointer):
    inWheel = 'k0'
    return inWheel

def e_alberti(plaintext, key):
    ciphertext = ''
    
    outWheel = get_outWheel(key[0])
    inWheel = get_inWheel(key[1])

    for chr in plaintext:
        if chr.upper() in outWheel:
            indx = outWheel.index(chr.upper())
            ciphertext+= inWheel[indx]
        else:
            ciphertext+=chr
    return ciphertext

def d_alberti(ciphertext, key):
    plaintext = ''
        
    outWheel = get_outWheel(key[0])
    inWheel = get_inWheel(key[1])
    for chr in ciphertext:
        if chr.lower() in inWheel:
            indx = inWheel.index(char.lower())
            plaintext = outWheel[indx]
        else:
            plaintext+=char
    return plaintext

def cryptanalysis_alberti(ciphertext, outWheel, inWheel):
    plaintext = ''
    for i in range(len(outWheel)):
        for j in range(len(inWheel)):
            key = outwheel[0] +inWheel[0]
            plaintext = d_alberti(ciphertext, key)
            result = cryptoUtil.is_plaintext(plaintext, "engmix.txt", 0.8)
            if result:
                break
            else:
                print("Key:", key, "failed")
                inWheel = cryptoUtil.shift_string(inWheel, 1, 'l')
        outWheel = cryptoUtil.shift_string(outWheel, 1, 'l')
    return key, plaintext
    

