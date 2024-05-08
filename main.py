MAX_WORDS = 6

with open('valid-wordle-words.txt', 'r') as file:
    wordle_words = {word.strip().lower() for word in file}

input_words = []

print("Enter 5-letter words (press Enter without typing anything to finish):")

while len(input_words) < MAX_WORDS - 1:
    user_input = input("Enter a 5-letter word: ").strip().lower()
    
    if len(user_input) == 0:
        break
    if len(user_input) != 5:
        print("Please enter a 5-letter word.")
    elif user_input not in wordle_words:
        print("Word is not a valid wordle word")
    elif user_input in input_words:
        print("Word has already been entered")
    else:
        input_words.append(user_input)

print(f"\nYou entered the following words: {', '.join(input_words)}")

valid_words = []

for wordle_word in wordle_words:
    valid = True
    for input_word in input_words:
        for letter in input_word:
            if letter in wordle_word:
                valid = False
    if valid:
        valid_words.append(wordle_word)

if len(valid_words) != 0:
    print(sorted(valid_words))
else:
    print("No valid words")


