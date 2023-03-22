import Task_1
from Task_2 import Task_2


# print(Task_1.text(), end= "\n")

# print(f"Amount of sentences in the text is: {Task_1.amount_of_sentences(Task_1.text())}")
# print(
#     f"Amount of non-declarative sentences is the text is: {Task_1.amount_of_nondec_sentences(Task_1.text())}"
# )
# print(f"Average length of the sentence is: {Task_1.average_length_of_sentence(Task_1.text())}")
# print(f"Average length of word in the text is: {Task_1.average_length_of_word(Task_1.text())}")

# k = input("Enter number of N-grams in the output: ")
# n = input("Enter N for N-grams: ")

# sorted_n_gramms = Task_1.top_K_N_grams(Task_1.text(), k, n)
# print(f"Here are top {k} rated {n}-gramms: ")

# size = 0
# if int(k) > len(sorted_n_gramms):
#     size = len(sorted_n_gramms)
# else:
#     size = int(k)

# for i in range(size):
#     space = (50 - len(sorted_n_gramms[i][0])) * "-"
#     print(f"{i + 1}. {sorted_n_gramms[i][0]} {space}> {sorted_n_gramms[i][1]}")

A = Task_2()
