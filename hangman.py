import random, string, os, sys
import time
from words import words

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 10

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        os.system('cls')
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(f'You have {lives} ❤  lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word 😳.')
                time.sleep(1.5)
                os.system('cls')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter 😝.')
            time.sleep(1.5)
            os.system('cls')

        else:
            print('\nThat is not a valid letter ❌.')
            time.sleep(1.5)
            os.system('cls')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(f'Game Over, sorry 😞. The word was {word}.')
        time.sleep(5)
        os.system('cls')
    else:
        print(f'YAY 🎉! You guessed the word {word}!')
        time.sleep(5)
        os.system('cls')

def play_again():
    while True:
        replay = input("Would you like to play again? (y/n): ").lower()
        if replay == 'y':
            hangman()
        elif replay == 'n':
            sys.exit("Bye bye then... 👋")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

hangman()
play_again()