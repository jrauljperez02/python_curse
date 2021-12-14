import random


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

def random_choice_word():
    word_list = ['hangman','keyboard','computer','python','airplane','spiderman']
    return random.choice(word_list)

def create_display(chosen_word):
    display = []
    for char in range(len(chosen_word)):
        display.append("_")
    
    return display

def check_character(chosen_word,display,stages):
    #if letter is in chosen_word

    end_of_game = True
    lives = 6

    while end_of_game:
        guess = input("Guess a letter: ").lower()

        for position in range(len(chosen_word)):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter
        
        #if letter is not in chosen_word
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
        

chosen_word = random_choice_word()
print(chosen_word)
display_out_function = create_display(chosen_word)
print(display_out_function)
check_character(chosen_word,display_out_function,stages)

    

    
    

