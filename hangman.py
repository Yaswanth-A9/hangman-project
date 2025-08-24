
# coding: utf-8

# In[ ]:


import random

# Word list
word_list = ["lion", "cheetah", "tiger"]
chosen_word = random.choice(word_list)
lives = 6

# Hangman stages
stages = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========
    ''',  # 6 lives left
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    ''',  # 5 lives
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    ''',  # 4 lives
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    ''',  # 3 lives
    '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    ''',  # 2 lives
    '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    ''',  # 1 life
    '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    '''   # 0 lives (game over)
]

# Set up the display
display = ['_' for _ in chosen_word]
print(" ".join(display))

# Game loop
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")

    print(" ".join(display))
    print(stages[6 - lives])  # Show hangman art based on lives

    if '_' not in display:
        game_over = True
        print("You win!!! 🎉")

    if lives == 0:
        game_over = True
        print("You lose!!! 💀")
        print(f"The word was: {chosen_word}")

