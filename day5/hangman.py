import random
from typing import final
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ['hangman','keyboard','computer','python','airplane','spiderman']
chosen_word = random.choice(word_list)
print(chosen_word)
display = []

'''for char in chosen_word:
    display.append("_")'''
for char in range(len(chosen_word)):
    display.append("_")

print(display)
end_of_game = True
lives = 6

while end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"You have {lives} lives")
        if lives == 0:
            end_of_game = False
            print("You lose")
    print(display)

    if "_" not in display:
        end_of_game = False
        print("You win")
        final_word = ''
        for element in display:
            final_word += element
        print(f"Secret word was {final_word}")
        

    

    



