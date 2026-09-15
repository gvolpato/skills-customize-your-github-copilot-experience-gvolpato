
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic word-guessing game using strings, loops, conditionals, and user input in Python. This activity will help you practice random selection, string manipulation, and game-state tracking.

## 📝 Tasks

### 🛠️ Create the Word Selection and Game Setup

#### Description
Create the initial structure of the Hangman game by defining a list of words, selecting one at random, and preparing the hidden word display.

#### Requirements
The completed program must:

- Use a predefined list of words and choose one randomly.
- Display the hidden word as underscores, such as `_ _ _ _ _`.
- Keep track of the letters already guessed by the player.
- Ask the player to enter a letter and validate the input.

### 🛠️ Implement the Game Logic and End Conditions

#### Description
Develop the main gameplay loop so the player can guess letters until the word is revealed or the attempts run out.

#### Requirements
The completed program must:

- Show the current progress after each guess, e.g. `H _ N _ A _`.
- Count incorrect attempts and reduce the remaining lives.
- Allow repeated guesses without losing progress for correctly repeated letters.
- End the game when the word is fully guessed or when the player runs out of tries.
- Display a win message when the word is completed and a loss message when the attempts are exhausted.