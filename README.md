# The Perfect Guess

This Python script implements a simple random number guessing game. The computer selects a random number between 1 and 100, and the player tries to guess the correct number. The game provides feedback to the player after each guess, indicating whether the guessed number is higher or lower than the target.

## How to Play

  1. Run the script:
  
     ```bash
     python random_number_guessing.py
     ```
  2. The computer will choose a random number between 1 and 100.
  3. You will be prompted to guess the number.
  4. After each guess, the game will provide feedback on whether the correct number is higher or lower.
  5. The game ends when you correctly guess the number.

## Code Overview
  The code uses a while loop to continuously prompt the player for guesses until the correct number is guessed. The game provides feedback based on the user's input, helping them refine their guesses.

## Example Output
  ```less
                  Computer is choosing a random number
  
  Guess the number: 50
  You guessed it wrong! Choose a LOWER number.
  
  Guess the number: 25
  You guessed it wrong! Choose a HIGHER number.
  
  Guess the number: 37
  You guessed it wrong! Choose a HIGHER number.
  
  Guess the number: 43
  Congratulations! You guessed it right.
  It took you 4 guesses to win.
  ```
## High Score (Commented Out)
  The code includes commented-out sections related to a high score feature. By uncommenting and modifying these sections, you can implement a system to track and record the best scores.

## License
  This project is open-source and available under the MIT License. Feel free to modify and use the code according to your needs.
