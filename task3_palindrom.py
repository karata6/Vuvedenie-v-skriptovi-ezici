words_input = input("Enter words: ")
words = words_input.split()

palindromes = []

for w in words:
    if w == w[::-1]:
        palindromes.append(w)

print("palindromes:", palindromes)
