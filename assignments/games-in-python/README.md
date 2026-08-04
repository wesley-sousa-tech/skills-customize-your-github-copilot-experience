
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game in Python to practice string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️ Implement Word Selection and Game Setup

#### Descrição
Create the initial game setup by defining a word list, selecting one word at random, and initializing the game state.

#### Requisitos
O programa concluído deve:

- Select one word randomly from a predefined list.
- Initialize the hidden word display using underscores (for example: `_ _ _ _`).
- Set the starting number of incorrect attempts allowed.

### 🛠️ Build the Guessing Loop and End Conditions

#### Descrição
Implement the main game loop to receive letter guesses, update progress, and end the game with a clear result.

#### Requisitos
O programa concluído deve:

- Accept letter guesses from the user one at a time.
- Reveal correctly guessed letters in the current word display.
- Decrease remaining attempts only when the guess is incorrect.
- End with a victory message when the word is fully guessed.
- End with a defeat message when attempts reach zero.