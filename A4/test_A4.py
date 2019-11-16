#--------------------------
# CP460 (Fall 2019)
# Assignment 4 Testing File
#--------------------------

import solution_A4
import utilities_A4
import mod
import matrix

#----------------------------------------------------
# Test Q1: Modular Arithmetic Library
#---------------------------------------------------
def test_q1():
    print("-------------------------------------------")
    print("Testing Q1: Modular Arithmetic Library")
    filename = 'q1_solution.txt'
    outFile = open(filename,'w')
    print()

    outFile.write('1- Testing residue_set:\n')
    outFile.write('residue_set({}) =  {}\n'.format(10,mod.residue_set(10)))
    outFile.write('residue_set({}) =   {}\n'.format(1,mod.residue_set(1)))
    outFile.write('residue_set({}) =  '.format(-5))
    outFile.write('{}\n'.format(mod.residue_set(-5)))
    outFile.write('residue_set({}) = '.format([5]))
    outFile.write('{}\n'.format(mod.residue_set([5])))
    outFile.write('\n')

    outFile.write('2- Testing residue:\n')
    outFile.write('residue({},{}) =  {}\n'.format(17,5,mod.residue(17,5)))
    outFile.write('residue({},{}) = '.format(3.4,5))
    outFile.write('{}\n'.format(mod.residue(3.4,5)))
    outFile.write('residue({},{}) = '.format(13,-5))
    outFile.write('{}\n'.format(mod.residue(13,-5)))
    outFile.write('\n')

    outFile.write('3- Testing is_congruent:\n')
    outFile.write('is_congruent({},{},{})= {}\n'.format(22,33,11,mod.is_congruent(22,33,11)))
    outFile.write('is_congruent({},{},{}) =   {}\n'.format(7,9,3,mod.is_congruent(7,9,3)))
    outFile.write('is_congruent({},{},{})=  '.format(3.4,5,9))
    outFile.write('{}\n'.format(mod.is_congruent(3.4,5,9)))
    outFile.write('is_congruent({},{},{}) =  '.format(3,5,-9))
    outFile.write('{}\n'.format(mod.is_congruent(3,5,-9)))
    outFile.write('\n')

    outFile.write('4- Testing add:\n')
    outFile.write('add({},{},{}) =  {}\n'.format(17,23,7,mod.add(17,23,7)))
    outFile.write('add({},{},{}) = {}\n'.format(-17,23,7,mod.add(-17,23,7)))
    outFile.write('add({},{},{}) = {}\n'.format(17,-23,7,mod.add(17,-23,7)))
    outFile.write('add({},{},{}) =   '.format(9,17,0))
    outFile.write('{}\n'.format(mod.add(9,17,0)))
    outFile.write('add({},{},{}) = '.format([9],17,7))
    outFile.write('{}\n'.format(mod.add([9],17,7)))
    outFile.write('add({},{},{}) = '.format(9,17.1,8))
    outFile.write('{}\n'.format(mod.add(9,17.1,8)))
    outFile.write('\n')

    outFile.write('5- Testing sub:\n')
    outFile.write('sub({},{},{}) =  {}\n'.format(17,23,7,mod.sub(17,23,7)))
    outFile.write('sub({},{},{}) = {}\n'.format(-17,23,7,mod.sub(-17,23,7)))
    outFile.write('sub({},{},{}) = {}\n'.format(17,-23,7,mod.sub(17,-23,7)))
    outFile.write('sub({},{},{}) =   '.format(9,17,0))
    outFile.write('{}\n'.format(mod.sub(9,17,0)))
    outFile.write('sub({},{},{}) = '.format([9],17,7))
    outFile.write('{}\n'.format(mod.sub([9],17,7)))
    outFile.write('sub({},{},{}) = '.format(9,17.1,8))
    outFile.write('{}\n'.format(mod.sub(9,17.1,8)))
    outFile.write('\n')

    outFile.write('6- Testing additive inverse:\n')
    outFile.write('add_inv({},{}) =   {}\n'.format(3,5,mod.add_inv(3,5)))
    outFile.write('add_inv({},{}) =   {}\n'.format(6,1,mod.add_inv(6,1)))
    outFile.write('add_inv({},{})=  {}\n'.format(22,10,mod.add_inv(22,10)))
    outFile.write('add_inv({},{}) =  '.format(6,-1))
    outFile.write('{}\n'.format(mod.add_inv(6,-1)))
    outFile.write('add_inv({},{}) = '.format(6.2,6))
    outFile.write('{}\n'.format(mod.add_inv(6.2,6)))
    a = 4
    b = 2
    m = 5
    result = mod.sub(a,b,m) == mod.add(a,mod.add_inv(b,m),m)
    outFile.write('sub({0},{1},{2}) == add({0},add_inv({1},{2}),{2})? = {3}\n'.format(a,b,m,result))
    outFile.write('\n')

    outFile.write('7- Testing Addition Table:\n')
    outFile.write('Addition Table for mode {} =\n'.format(5))
    addTab = mod.add_table(5)
    for i in range(len(addTab)):
        outFile.write(str(addTab[i]))
        outFile.write('\n')
    outFile.write('Addition Table for mode {} =\n'.format(8))
    addTab = mod.add_table(8)
    for i in range(len(addTab)):
        outFile.write(str(addTab[i]))
        outFile.write('\n')
    outFile.write('Addition Table for mode {} =\n'.format(0))
    outFile.write(mod.add_table(0))
    outFile.write('\n')
    outFile.write('\n')

    outFile.write('8- Testing Subtraction Table:\n')
    outFile.write('Subtraction Table for mode {} =\n'.format(5))
    subTab = mod.sub_table(5)
    for i in range(len(subTab)):
        outFile.write(str(subTab[i]))
        outFile.write('\n')
    outFile.write('Subtraction Table for mode {} =\n'.format(8))
    subTab = mod.sub_table(8)
    for i in range(len(subTab)):
        outFile.write(str(subTab[i]))
        outFile.write('\n')
    outFile.write('Subtraction Table for mode {} =\n'.format([5]))
    outFile.write(mod.sub_table([5]))
    outFile.write('\n')
    outFile.write('\n')
    
    outFile.write('9- Testing Addition Inverse Table:\n')
    outFile.write('Addition Inverse Table for mode {} =\n'.format(5))
    addInvTab = mod.add_inv_table(5)
    outFile.write(str(addInvTab[0]))
    outFile.write('\n')
    outFile.write(str(addInvTab[1]))
    outFile.write('\n')
    outFile.write('Addition Inverse Table for mode {} =\n'.format(26))
    addInvTab = mod.add_inv_table(26)
    outFile.write(str(addInvTab[0]))
    outFile.write('\n')
    outFile.write(str(addInvTab[1]))
    outFile.write('\n')
    outFile.write('Addition Inverse Table for mode {} =\n'.format(-2))
    outFile.write(mod.add_inv_table(-2))
    outFile.write('\n')
    outFile.write('\n')

    outFile.write('10- Testing mul:\n')
    outFile.write('mul({},{},{}) =    {}\n'.format(3,5,5,mod.mul(3,5,5)))
    outFile.write('mul({},{},{}) =    {}\n'.format(8,3,7,mod.mul(8,3,7)))
    outFile.write('mul({},{},{})=   {}\n'.format(17,-3,7,mod.mul(17,-3,7)))
    outFile.write('mul({},{},{}) =   '.format(9,17,0))
    outFile.write('{}\n'.format(mod.mul(9,17,0)))
    outFile.write('mul({},{},{}) = '.format([9],17,7))
    outFile.write('{}\n'.format(mod.mul([9],17,7)))
    outFile.write('mul({},{},{}) = '.format(9,17.1,8))
    outFile.write('{}\n'.format(mod.mul(9,17.1,8)))
    outFile.write('\n')

    outFile.write('11- Testing Multiplication Table:\n')
    outFile.write('Multiplication Table for mode {} =\n'.format(4))
    mulTab = mod.mul_table(4)
    for i in range(len(mulTab)):
        outFile.write(str(mulTab[i]))
        outFile.write('\n')
    outFile.write('Multiplication Table for mode {} =\n'.format(5))
    mulTab = mod.mul_table(5)
    for i in range(len(mulTab)):
        outFile.write(str(mulTab[i]))
        outFile.write('\n')
    outFile.write('Multiplication Table for mode {} =\n'.format(-5))
    outFile.write(mod.mul_table(-5))
    outFile.write('\n')
    outFile.write('\n')

    outFile.write('12- Testing is_prime:\n')
    outFile.write('is_prime({}) =  {}\n'.format(97,mod.is_prime(97)))
    outFile.write('is_prime({}) = {}\n'.format(479,mod.is_prime(479)))
    outFile.write('is_prime({})= {}\n'.format(1044,mod.is_prime(1044)))
    outFile.write('is_prime({}) =   {}\n'.format(0,mod.is_prime(0)))
    outFile.write('is_prime({}) = {}\n'.format(-17,mod.is_prime(-17)))
    outFile.write('\n')

    outFile.write('13- Testing gcd:\n')
    outFile.write('gcd({},{}) =  {}\n'.format(629,357,mod.gcd(629,357)))
    outFile.write('gcd({},{}) =  {}\n'.format(440,700,mod.gcd(440,700)))
    outFile.write('gcd({},{}) =  {}\n'.format(-30,700,mod.gcd(-30,700)))
    outFile.write('gcd({},{}) = {}\n'.format(540,-539,mod.gcd(540,-539)))
    outFile.write('gcd({},{})   = '.format(711,0))
    outFile.write(mod.gcd(711,0))
    outFile.write('\n')
    outFile.write('gcd({},{})   = '.format(0,311))
    outFile.write(mod.gcd(0,311))
    outFile.write('\n')
    outFile.write('gcd({},{})  = '.format([9],27))
    outFile.write(mod.gcd([9],27))
    outFile.write('\n')
    outFile.write('\n')
    
    outFile.write('14- Testing is_relatively_prime:\n')
    outFile.write('is_relatively_prime({},{}) =     {}\n'.format(4,5,mod.is_relatively_prime(4,5)))
    outFile.write('is_relatively_prime({},{})=  {}\n'.format(540,539,mod.is_relatively_prime(540,539)))
    outFile.write('is_relatively_prime({},{}) =   {}\n'.format(18,26,mod.is_relatively_prime(18,26)))
    outFile.write('is_relatively_prime({},{}) =    {}\n'.format(0,26,mod.is_relatively_prime(0,26)))
    outFile.write('is_relatively_prime({},{}) =  '.format([1],26))
    outFile.write(mod.is_relatively_prime([1],26))
    outFile.write('\n')
    outFile.write('\n')

    outFile.write('15- Testing has_mul_inv:\n')
    outFile.write('has_mul_inv({},{}) =     {}\n'.format(4,5,mod.has_mul_inv(4,5)))
    outFile.write('has_mul_inv({},{}) =   {}\n'.format(17,26,mod.has_mul_inv(17,26)))
    outFile.write('has_mul_inv({},{}) =   {}\n'.format(18,26,mod.has_mul_inv(18,26)))
    outFile.write('has_mul_inv({},{}) =    {}\n'.format(0,26,mod.has_mul_inv(0,26)))
    outFile.write('has_mul_inv({},{}) =  '.format([1],26))
    outFile.write(mod.has_mul_inv([1],26))
    outFile.write('\n')
    outFile.write('\n')

    outFile.write('16- Testing EEA:\n')
    outFile.write('eea({},{}) =   {}\n'.format(700,440,mod.eea(700,440)))
    outFile.write('eea({},{}) =     {}\n'.format(88,35,mod.eea(88,35)))
    outFile.write('eea({},{}) =     {}\n'.format(35,88,mod.eea(35,88)))
    outFile.write('eea({},{}) =    {}\n'.format(-88,35,mod.eea(-88,35)))
    outFile.write('eea({},{}) =    {}\n'.format(88,-35,mod.eea(88,-35)))
    outFile.write('eea({},{}) =     '.format(0,777))
    outFile.write(mod.eea(0,777))
    outFile.write('\n')
    outFile.write('\n')

    outFile.write('17- Testing mul_inv:\n')
    outFile.write('mul_inv({},{}) =   {}\n'.format(23,26,mod.mul_inv(23,26)))
    outFile.write('mul_inv({},{}) =     {}\n'.format(5,6,mod.mul_inv(5,6)))
    outFile.write('mul_inv({},{}) =   {}\n'.format(24,26,mod.mul_inv(24,26)))
    outFile.write('mul_inv({},{}) = {}\n'.format(700,440,mod.mul_inv(700,440)))
    outFile.write('mul_inv({},{}) =   {}\n'.format(0,777,mod.mul_inv(700,440)))
    outFile.write('mul_inv({},{}) =  '.format(1,[99]))
    outFile.write(mod.mul_inv(1,[99]))
    outFile.write('\n')
    outFile.write('mul_inv({},{}) =  '.format([1],99))
    outFile.write(mod.mul_inv([1],99))
    outFile.write('\n')
    outFile.write('\n')

    outFile.write('18- Testing Multiplicative Inverse Table:\n')
    outFile.write('Multiplicative Inverse Table for mode {} =\n'.format(5))
    mulInvTab = mod.mul_inv_table(5)
    outFile.write(str(mulInvTab[0]))
    outFile.write('\n')
    outFile.write(str(mulInvTab[1]))
    outFile.write('\n')
    outFile.write('Multiplicative Inverse Table for mode {} =\n'.format(26))
    mulInvTab = mod.mul_inv_table(26)
    outFile.write(str(mulInvTab[0]))
    outFile.write('\n')
    outFile.write(str(mulInvTab[1]))
    outFile.write('\n')
    outFile.write('Multiplicative Inverse Table for mode {} =\n'.format(-2))
    outFile.write(mod.mul_inv_table(-2))
    outFile.write('\n')
    outFile.write('\n')

    outFile.close()
    print('Comparing q1_solution with q1_sample:')
    print(utilities_A4.compare_files('q1_solution.txt','q1_sample.txt'))
    print()
    print("-------------------------------------------")

    return

#----------------------------------------------------
# Test Q2: Decimation Cipher
#---------------------------------------------------
def test_q2():
    print("-------------------------------------------")
    print("Testing Q2: Decimation Cipher")
    print()

    alphabet = utilities_A4.get_lower()

    baseStr = alphabet
    k = 5
    plaintext = 'Strike in progress'
    key = (baseStr,k)
    print('key = ',key)
    print('plaintext =  ',plaintext)
    ciphertext = solution_A4.e_decimation(plaintext,key)
    print('ciphertext=  ',ciphertext)
    plaintext2 = solution_A4.d_decimation(ciphertext,key)
    print('plaintext2=  ',plaintext2)
    print()

    baseStr = alphabet + ' ?!'
    k = 46
    plaintext = 'Is mission accomplished?'
    key = (baseStr,k)
    print('key = ',key)
    print('plaintext =  ',plaintext)
    ciphertext = solution_A4.e_decimation(plaintext,key)
    print('ciphertext=  ',ciphertext)
    plaintext2 = solution_A4.d_decimation(ciphertext,key)
    print('plaintext2=  ',plaintext2)
    print()

    baseStr = alphabet + ' ?!.'
    k = 10
    plaintext = 'Plan B ... initiated'
    key = (baseStr,k)
    print('key = ',key)
    print('plaintext = ',plaintext)
    print('ciphertext=  ',end = '')
    solution_A4.e_decimation(plaintext,key)
    print('plaintext2=  ',end = '')
    solution_A4.d_decimation(plaintext,key)
    print()

    print('Testing cryptanalysis:')
    ciphertext = 'Mrhoyu on xhsehumm'
    plaintext,key = solution_A4.cryptanalysis_decimation(ciphertext)
    if plaintext != '':
        print('Key found = ',key)
        print('plaintext = ',plaintext)
    print()

    plaintext = 'There are two kinds of cryptography in this world: cryptography that will stop your kid sister '
    plaintext+= 'from reading your files, and cryptography that will stop major governments from reading your files.'
    baseString = utilities_A4.get_baseString()[:35]
    key = (baseString,33)
    ciphertext = solution_A4.e_decimation(plaintext,key)
    plaintext,key = solution_A4.cryptanalysis_decimation(ciphertext)
    if plaintext != '':
        print('Key found = ',key)
        print('plaintext = ',plaintext)
    print("-------------------------------------------")
    print()
    return

#----------------------------------------------------
# Test Q3: Affine Cipher
#---------------------------------------------------
def test_q3():
    print("-------------------------------------------")
    print("Testing Q3: Affine Cipher")
    print()

    alphabet = utilities_A4.get_lower()

    baseStr = alphabet
    k = [5,8]
    plaintext = 'AFFINE CIPHER'
    key = (baseStr,k)
    print('key = ',key)
    print('plaintext =  ',plaintext)
    ciphertext = solution_A4.e_affine(plaintext,key)
    print('ciphertext=  ',ciphertext)
    plaintext2 = solution_A4.d_affine(ciphertext,key)
    print('plaintext2=  ',plaintext2)
    print()

    baseStr = alphabet + ' ?!'
    k = [45,3]
    plaintext = 'Is mission accomplished?'
    key = (baseStr,k)
    print('key = ',key)
    print('plaintext =  ',plaintext)
    ciphertext = solution_A4.e_affine(plaintext,key)
    print('ciphertext=  ',ciphertext)
    plaintext2 = solution_A4.d_affine(ciphertext,key)
    print('plaintext2=  ',plaintext2)
    print()

    baseStr = alphabet + ' ?!.'
    k = [10,19]
    plaintext = 'Plan B ... initiated'
    key = (baseStr,k)
    print('key = ',key)
    print('plaintext = ',plaintext)
    print('ciphertext=  ',end = '')
    solution_A4.e_affine(plaintext,key)
    print('plaintext2=  ',end = '')
    solution_A4.d_affine(plaintext,key)
    print()

    print('Testing cryptanalysis:')
    plaintext = 'There are two kinds of cryptography in this world: cryptography that will stop your kid sister '
    plaintext+= 'from reading your files, and cryptography that will stop major governments from reading your files.'
    baseString = utilities_A4.get_baseString()[:26]
    key = (baseString,[3,9])
    ciphertext = solution_A4.e_affine(plaintext,key)
    plaintext,key = solution_A4.cryptanalysis_affine(ciphertext)
    if plaintext != '':
        print('Key found = ',key)
        print('plaintext = ',plaintext)
    print()
    baseString = utilities_A4.get_baseString()[:27]
    key = (baseString,[17,11])
    ciphertext = solution_A4.e_affine(plaintext,key)
    plaintext,key = solution_A4.cryptanalysis_affine(ciphertext)
    if plaintext != '':
        print('Key found = ',key)
        print('plaintext = ',plaintext)
    
    print("-------------------------------------------")
    print()
    return

#----------------------------------------------------
# Test Q4: Matrix Library
#---------------------------------------------------
def test_q4():
    print("-------------------------------------------")
    print("Testing Q4: Matrix Library")
    filename = 'q4_solution.txt'
    outFile = open(filename,'w')
    print()

    outFile.write('1- Testing is_vector:\n')
    outFile.write('is_vector({}) =  {}\n'.format([],matrix.is_vector([])))
    outFile.write('is_vector({}) =  {}\n'.format([10],matrix.is_vector([10])))
    outFile.write('is_vector({}) =  {}\n'.format([10,20],matrix.is_vector([10,20])))
    outFile.write('is_vector({}) =  {}\n'.format(10,matrix.is_vector(10)))
    outFile.write('is_vector({}) =  {}\n'.format([3,4.5],matrix.is_vector([3,4.5])))
    outFile.write('is_vector({}) =  {}\n'.format([[]],matrix.is_vector([[]])))
    outFile.write('is_vector({}) =  {}\n'.format([[1,2],[3,4]],matrix.is_vector([[1,2],[3,4]])))
    outFile.write('\n')

    outFile.write('2- Testing is_matrix')
    A = []
    outFile.write('is_matrix({}) =  {}\n'.format(A,matrix.is_matrix(A)))
    A = [5]
    outFile.write('is_matrix({}) =  {}\n'.format(A,matrix.is_matrix(A)))
    A = [[1,2],[3,4]]
    outFile.write('is_matrix({}) =  {}\n'.format(A,matrix.is_matrix(A)))
    A = [[1],[2],[3]]
    outFile.write('is_matrix({}) =  {}\n'.format(A,matrix.is_matrix(A)))
    A = [[1,2,3],[4,5,6]]
    outFile.write('is_matrix({}) =  {}\n'.format(A,matrix.is_matrix(A)))
    A = 5
    outFile.write('is_matrix({}) =  {}\n'.format(A,matrix.is_matrix(A)))
    A = [5.5]
    outFile.write('is_matrix({}) =  {}\n'.format(A,matrix.is_matrix(A)))
    A = [[1,2,3],[4,5]]
    outFile.write('is_matrix({}) =  {}\n'.format(A,matrix.is_matrix(A)))
    outFile.write('\n')

    print('3- Testing print_matrix')
    A = []
    print('print_matrix({})='.format(A))
    matrix.print_matrix(A)
    A = [10,20,30]
    print('print_matrix({})='.format(A))
    matrix.print_matrix(A)
    A = [[10],[20],[30]]
    print('print_matrix({})='.format(A))
    matrix.print_matrix(A)
    A = [[10,20,30],[40,50,60],[70,80,10]]
    print('print_matrix({})='.format(A))
    matrix.print_matrix(A)
    A = [[10,20,30],[40,50,60],[70,80]]
    print('print_matrix({})='.format(A))
    print(matrix.print_matrix(A))
    print()
    
    outFile.write('4/5/6- Testing size functions\n')
    A = []
    outFile.write('get_rowCount({})    =  {}\n'.format(A,matrix.get_rowCount(A)))
    outFile.write('get_ColumnCount({}) =  {}\n'.format(A,matrix.get_columnCount(A)))
    outFile.write('get_size({})        =  {}\n'.format(A,matrix.get_size(A)))
    outFile.write('\n')

    A = [1,2,3]
    outFile.write('get_rowCount({})    =  {}\n'.format(A,matrix.get_rowCount(A)))
    outFile.write('get_ColumnCount({}) =  {}\n'.format(A,matrix.get_columnCount(A)))
    outFile.write('get_size({})        =  {}\n'.format(A,matrix.get_size(A)))
    outFile.write('\n')

    A = [[1,2],[3,4],[5,6]]
    outFile.write('get_rowCount({})    =  {}\n'.format(A,matrix.get_rowCount(A)))
    outFile.write('get_ColumnCount({}) =  {}\n'.format(A,matrix.get_columnCount(A)))
    outFile.write('get_size({})        =  {}\n'.format(A,matrix.get_size(A)))
    outFile.write('\n')

    A = [[1,2],[3]]
    outFile.write('get_rowCount({})    =  {}\n'.format(A,matrix.get_rowCount(A)))
    outFile.write('get_ColumnCount({}) =  {}\n'.format(A,matrix.get_columnCount(A)))
    outFile.write('get_size({})        =  {}\n'.format(A,matrix.get_size(A)))
    outFile.write('\n')

    outFile.write('7- Testing is_square\n')
    A = []
    outFile.write('is_square({})    =  {}\n'.format(A,matrix.is_square(A)))
    A = [5]
    outFile.write('is_square({})    =  {}\n'.format(A,matrix.is_square(A)))
    A = [5,6]
    outFile.write('is_square({})    =  {}\n'.format(A,matrix.is_square(A)))
    A = [[1,2],[3,4]]
    outFile.write('is_square({})    =  {}\n'.format(A,matrix.is_square(A)))
    A = [5.5]
    outFile.write('is_square({})    =  {}\n'.format(A,matrix.is_square(A)))
    outFile.write('\n')

    outFile.write('8/9/10- Testing getter functions\n')
    A = [[1,2,3],[4,5,6]]
    i = 0
    j = 1
    outFile.write('get_row({},{})    = {}\n'.format(A,i,matrix.get_row(A,i)))
    outFile.write('get_Column({},{}) = {}\n'.format(A,j,matrix.get_column(A,j)))
    outFile.write('get_element({},{},{}) = {}\n'.format(A,i,j,matrix.get_element(A,i,j)))
    outFile.write('\n')
    
    i = 2
    j = 2
    outFile.write('get_row({},{})    = {}\n'.format(A,i,matrix.get_row(A,i)))
    outFile.write('get_Column({},{}) = {}\n'.format(A,j,matrix.get_column(A,j)))
    outFile.write('get_element({},{},{}) = {}\n'.format(A,i,j,matrix.get_element(A,i,j)))
    outFile.write('\n')

    i = 1
    j = 3
    outFile.write('get_row({},{})    = {}\n'.format(A,i,matrix.get_row(A,i)))
    outFile.write('get_Column({},{}) = {}\n'.format(A,j,matrix.get_column(A,j)))
    outFile.write('get_element({},{},{}) = {}\n'.format(A,i,j,matrix.get_element(A,i,j)))
    outFile.write('\n')

    A = [[1,2,3],[]]
    outFile.write('get_row({},{})    = {}\n'.format(A,i,matrix.get_row(A,i)))
    outFile.write('get_Column({},{}) = {}\n'.format(A,j,matrix.get_column(A,j)))
    outFile.write('get_element({},{},{}) = {}\n'.format(A,i,j,matrix.get_element(A,i,j)))
    outFile.write('\n')

    outFile.write('11- Testing new_matrix\n')
    r=0
    c=0
    pad=0
    outFile.write('new_matrix({},{},{})=\n{}\n'.format(r,c,pad,matrix.new_matrix(r,c,pad)))
    c=1
    outFile.write('new_matrix({},{},{})=\n{}\n'.format(r,c,pad,matrix.new_matrix(r,c,pad)))
    r=1
    outFile.write('new_matrix({},{},{})=\n{}\n'.format(r,c,pad,matrix.new_matrix(r,c,pad)))
    r=2
    c=1
    outFile.write('new_matrix({},{},{})=\n{}\n'.format(r,c,pad,matrix.new_matrix(r,c,pad)))
    c=2
    r=1
    outFile.write('new_matrix({},{},{})=\n{}\n'.format(r,c,pad,matrix.new_matrix(r,c,pad)))
    c=3
    r=3
    outFile.write('new_matrix({},{},{})=\n{}\n'.format(r,c,pad,matrix.new_matrix(r,c,pad)))
    r=-1
    outFile.write('new_matrix({},{},{})=\n{}\n'.format(r,c,pad,matrix.new_matrix(r,c,pad)))
    r=3
    c=-5
    outFile.write('new_matrix({},{},{})=\n{}\n'.format(r,c,pad,matrix.new_matrix(r,c,pad)))
    c=5
    pad = 3.5
    outFile.write('new_matrix({},{},{})=\n{}\n'.format(r,c,pad,matrix.new_matrix(r,c,pad)))
    outFile.write('\n')

    outFile.write('12- Testing get_I\n')
    size = -1
    outFile.write('get_I({})    = {}\n'.format(size,matrix.get_I(size)))
    size = 0
    outFile.write('get_I({})    =  {}\n'.format(size,matrix.get_I(size)))
    size = 1
    outFile.write('get_I({})    =  {}\n'.format(size,matrix.get_I(size)))
    size = 2
    outFile.write('get_I({})    =  {}\n'.format(size,matrix.get_I(size)))
    size = 3
    outFile.write('get_I({})    =  {}\n'.format(size,matrix.get_I(size)))
    outFile.write('\n')

    outFile.write('13- Testing is_identity\n')
    A = [1]
    outFile.write('is_identity({}) = {}\n'.format(A,matrix.is_identity(A)))
    A = matrix.get_I(3)
    outFile.write('is_identity({}) = {}\n'.format(A,matrix.is_identity(A)))
    A = [[1,0],[1,1]]
    outFile.write('is_identity({}) = {}\n'.format(A,matrix.is_identity(A)))
    A = [[1,0],[0,1,0]]
    outFile.write('is_identity({}) = {}\n'.format(A,matrix.is_identity(A)))
    outFile.write('\n')

    outFile.write('14- Testing scalar_mul\n')
    A = [[1,2],[3,4]]
    c = 10
    outFile.write('scalar_mul({},{}) = {}\n'.format(A,c,matrix.scalar_mul(c,A)))
    A = [1,2,3,4]
    outFile.write('scalar_mul({},{}) = {}\n'.format(A,c,matrix.scalar_mul(c,A)))
    A = []
    outFile.write('scalar_mul({},{}) = {}\n'.format(A,c,matrix.scalar_mul(c,A)))
    A = [1,2,3,[4]]
    outFile.write('scalar_mul({},{}) = {}\n'.format(A,c,matrix.scalar_mul(c,A)))
    A = [[1,2],[3,4]]
    c = [10]
    outFile.write('scalar_mul({},{}) = {}\n'.format(A,c,matrix.scalar_mul(c,A)))
    outFile.write('\n')

    outFile.write('15- Testing mul\n')
    A = [[1,2],[3,4]]
    B = [[10,20],[30,40]]
    outFile.write('mul({},{})=\n{}\n'.format(A,B,matrix.mul(A,B)))
    A = [[1,2,3],[5,6,7]]
    B = [[10,20],[30,40],[50,60]]
    outFile.write('mul({},{})= {}\n'.format(A,B,matrix.mul(A,B)))
    A = [5]
    B = [10]
    outFile.write('mul({},{})= {}\n'.format(A,B,matrix.mul(A,B)))
    A = [0,1,2]
    B = [[0],[1],[2]]
    outFile.write('mul({},{})= {}\n'.format(A,B,matrix.mul(A,B)))
    A = [[0],1]
    B = [1,0]
    outFile.write('mul({},{})= {}\n'.format(A,B,matrix.mul(A,B)))
    A = [1,0] 
    B = [[0],1]
    outFile.write('mul({},{})= {}\n'.format(A,B,matrix.mul(A,B)))
    A = [[1,2,3],[5,6,7]]
    B = [[10,20],[30,40],[50,60]]
    outFile.write('mul({},{})= {}\n'.format(B,A,matrix.mul(B,A)))
    A = [[1,2,3],[5,6,7]]
    B = [[10,20],[30,40]]
    outFile.write('mul({},{})= {}\n'.format(A,B,matrix.mul(A,B)))
    outFile.write('\n')

    outFile.write('16- Testing matrix_mod\n')
    A = [[1,2],[3,4]]
    m = 2
    outFile.write('matrix_mod({},{})= {}\n'.format(A,m,matrix.matrix_mod(A,m)))
    A = [1,2,3,4]
    m = 2
    outFile.write('matrix_mod({},{})= {}\n'.format(A,m,matrix.matrix_mod(A,m)))
    A = [[3],[5]]
    m = 3
    outFile.write('matrix_mod({},{})= {}\n'.format(A,m,matrix.matrix_mod(A,m)))
    A = [[3],[5]]
    m = 0
    outFile.write('matrix_mod({},{})= {}\n'.format(A,m,matrix.matrix_mod(A,m)))
    A = [3,[5]]
    m = 6
    outFile.write('matrix_mod({},{})= {}\n'.format(A,m,matrix.matrix_mod(A,m)))
    outFile.write('\n')

    outFile.write('17- Testing det\n')
    A = [[1,2],[3,4]]
    outFile.write('det({})= {}\n'.format(A,matrix.det(A)))
    A = [10]
    outFile.write('det({})= {}\n'.format(A,matrix.det(A)))
    A = [[1,1,1],[2,2,2],[3,3,3]]
    outFile.write('det({})= {}\n'.format(A,matrix.det(A)))
    A = [[1,1,1],[2,2]]
    outFile.write('det({})= {}\n'.format(A,matrix.det(A)))
    outFile.write('\n')

    outFile.write('18- Testing inverse\n')
    A = [[1,4],[8,11]]
    m = 26
    outFile.write('inverse({},{})= {}\n'.format(A,m,matrix.inverse(A,m)))
    A = [[4,3],[1,1]]
    m = 5
    outFile.write('inverse({},{})= {}\n'.format(A,m,matrix.inverse(A,m)))
    A = [[1,4],[8,10]]
    m = 26
    outFile.write('inverse({},{})= {}\n'.format(A,m,matrix.inverse(A,m)))
    A = [1,4,8,10]
    m = 15
    outFile.write('inverse({},{})= {}\n'.format(A,m,matrix.inverse(A,m)))
    A = [[4,3],[1,1]]
    m = -5
    outFile.write('inverse({},{})= {}\n'.format(A,m,matrix.inverse(A,m)))
    A = [[1,2,3],[4,5,6],[7,8,9]]
    m = 7
    outFile.write('inverse({},{})= {}\n'.format(A,m,matrix.inverse(A,m)))
    A = [[1,2,3],[4,5]]
    m = 7
    outFile.write('inverse({},{})= {}\n'.format(A,m,matrix.inverse(A,m)))
    
    outFile.close()
    print('Comparing q4_solution with q4_sample:')
    print(utilities_A4.compare_files('q4_solution.txt','q4_sample.txt'))
    print()
    print("-------------------------------------------")
    return

#----------------------------------------------------
# Test Q5: Hill Cipher
#---------------------------------------------------
def test_q5():
    print("-------------------------------------------")
    print("Testing Q5: Hill Cipher")
    print()

    plaintext = ['Lunch','Brunch','Breakfast','dinner','Lunch Bag',
                 'empty water bottle?','Full plates..of salad']
    key = ['pear','apple','fig','mellon','apricot','cherry','prune']
    for i in range(len(plaintext)):
        print('key = ',key[i])
        print('plaintext =  ',plaintext[i])
        ciphertext = solution_A4.e_hill(plaintext[i],key[i])
        print('ciphertext=  ',ciphertext)
        plaintext2 = solution_A4.d_hill(ciphertext,key[i])
        print('plaintext2=  ',plaintext2)
        print()

    print("-------------------------------------------")
