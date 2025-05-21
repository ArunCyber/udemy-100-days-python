import random

words = ['one', 'eats', 'mouse']
chosen_word = random.choice(words)

# def fill_guess_letter_in_word(letter):
#     while 

print(chosen_word)

dashes = []
for w in words:
    dashes += "_"

print(''.join(dashes))
guess_word = ''.join(dashes)

guess = input("Guess a letter? ").lower()
# print(input("Guess a letter? "))

for letter in chosen_word:
    if letter == guess:
        print(f'Exists')
        chosen_word_index = chosen_word.index(guess)
        dashes.insert(chosen_word_index, guess)
        print(''.join(dashes))
        guess_word = ''.join(dashes)
    else:
        print(f'Noo')


