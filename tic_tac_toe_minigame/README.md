# Minigame - Tic-Tac-Toe

This documentation explains a Python script that allows users to play a simple game of Tic-Tac-Toe in a command-line interface.

## Purpose

The purpose of this script is to provide a basic implementation of the classic Tic-Tac-Toe game where two players take turns to place their symbols (X and O) on a 3x3 grid. The script checks for a win or a draw and displays the result.

## Dependencies

To run this script, you need the following dependencies:

- `tabulate`: This library is used to display the Tic-Tac-Toe board in a tabulated format.
- `art`: The `art` module is used to display an ASCII art logo and a game over message.
- `time`: The `time` module is used to add delays for better user interaction.
- `os`: The `os` module is used to clear the console screen for a cleaner user experience.

## Usage

1. The script starts by displaying an ASCII art logo using the `art` module.
2. The game initializes a 3x3 board represented as a list of lists.
3. Players take turns to enter their moves by specifying the x-y position on the board (e.g., "0 1" for the first row and second column).
4. The script checks for invalid positions and filled spaces and provides appropriate feedback to the player.
5. The game continues until there is a winner or a draw.
6. When a player wins, the game displays a message indicating the winner.
7. If there's no more space left on the board, and there is no winner, the game ends in a draw.
8. The script uses the `tabulate` library to display the board in a grid format.
9. An ASCII art message is shown at the end of the game.

## Considerations

- This script provides a basic implementation of Tic-Tac-Toe and doesn't include advanced features like multiple rounds or AI opponents.
- It assumes two human players taking turns.
- The script is designed for educational and entertainment purposes.
- The ASCII art and game flow can be customized and extended according to your preferences.

## ASCII Art

The script uses the `art` module to display an ASCII art logo and a game over message. You can customize the ASCII art or replace it with your own.

## License

This script is provided for educational and personal use. Please respect any licensing and usage restrictions associated with the dependencies and ASCII art used in the script.

Enjoy playing Tic-Tac-Toe in your terminal with this simple Python game!
