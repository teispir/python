word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
word_with_vowels = input("Inserisci la parola:")
word_with_vowels = word_with_vowels.upper()

for letter in word_with_vowels:
    # Complete the body of the loop.
    if letter in 'AEIOU':
        continue
    else:
        word_without_vowels += letter
    
# Print the word assigned to word_without_vowels.
print(word_without_vowels)