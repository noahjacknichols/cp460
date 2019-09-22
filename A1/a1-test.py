import solution_A1
import test_A1
##A1 TEST
x = solution_A1.e_scytale("abcdefghi", 2)
print(x)
x = solution_A1.d_scytale(x, 2)
print(x)



##A2 TEST
# dict = solution_A1.load_dictionary("engmix.txt")
# print(len(dict))

##A3 TEST
# text = "this is a test dummy"
# word_list = solution_A1.text_to_words(text)
# print(word_list)

##A4 TEST
# text = "this is a test fdsfasf"
# dictFile = "engmix.txt"
# matches, mismatches = solution_A1.analyze_text(text, dictFile)
# print(matches, mismatches)

##A5 TEST

# test = "this is a test dummy"
# x = solution_A1.cryptanalysis_scytale("ciphertext1.txt", "engmix.txt", 4, 50, 0.8)
# print(x)

#test_A1.test_q1()