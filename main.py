import random
from hangman_art import stages
from hangman_words import word_list

lives = 6

# rondomly choose a word and from the word_list 
# and assign to avariable called choosen_word.

choosen_word = random.choice(word_list)

display = []
word_lenght = len(choosen_word)
for _ in range(word_lenght):
	display += "_"
#print(choosen_word)
print(display)

end_of_game = False
# Ask the user to guess a letter and assign their 
# answer to a variable called guess. Make guess lowercase.
while not end_of_game:
	guess = input("guess a letter from the word\n").lower()
	# Check if the letter the user guessed (guess) 
	# is one of the letters in choosen_word


	for position in range(word_lenght):
		letter = choosen_word[position]
		if letter == guess:
			display[position] = letter
	print(display)
	if lives > 0:
		if guess not in choosen_word:
			lives -= 1
			print(stages[lives])
			print("The choosen letter is not in the word")
			print(f"lives left: {lives}")
	else:
		end_of_game = True
		print("You lose")
	

	if "_" not in display:
		end_of_game = True
		print("You win")



