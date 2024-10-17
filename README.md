# Hangman Game in Python

## Overview
Welcome to the Hangman game! This is a simple console-based implementation of the classic word-guessing game, built using Python.

## Features
- Randomly selected words from a predefined text file
- Simple console interface
- Keeps track of incorrect guesses
- Displays the current state of the word being guessed
- Option to play again after finishing a game

## Requirements
- Python 3.x installed on your machine

## Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/HangMan.git
```
Navigate into the directory:
```
cd hangman-game
```
Usage:
Run the game by executing:

```
python hangman.py
```
Follow the prompts to guess letters until you either reveal the word or run out of attempts!

How to Play:
You will see a series of underscores representing the letters of a hidden word.
Enter a letter to guess. If it's in the word, it will be revealed; if not, your incorrect guess count will increase.
Keep guessing until you either reveal the entire word or make a predetermined number of incorrect guesses.
After each game, you can choose to play again.
Code Structure
hangman.py: The main game logic and user interface.
words.py: A module containing a list of words used in the game.
Contributing
Feel free to submit issues or pull requests if you want to improve the game!

License:
This project is licensed under the MIT License.

Enjoy the game!
