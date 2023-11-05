# Minigame - Blackjack

This documentation explains a Python script that simulates a game of Blackjack. Players can play against a computer-controlled dealer to get as close to 21 as possible without going over.

## Purpose

The purpose of this script is to provide a text-based version of the popular card game Blackjack. Players can play the game, make decisions to hit or stand, and compete against a computer-controlled dealer.

## Dependencies

This script does not require any external dependencies other than the built-in Python libraries.

## Usage

1. The script starts by asking the user if they want to play a game of Blackjack.
2. If the user agrees to play, the game begins with the dealer and the player receiving two initial cards each.
3. The player's current score and one of the dealer's cards are displayed.
4. The player is given the option to request another card ('hit') or to pass ('stand').
5. The game continues with the player requesting cards until they decide to pass or until their total score exceeds 21.
6. After the player's turn, the dealer takes their turn. The dealer must keep drawing cards until their total score reaches at least 16.
7. The final hands and scores of both the player and the dealer are displayed.
8. The game outcome is determined:
   - If the player's score exceeds 21, they lose.
   - If the dealer's score exceeds 21, the player wins.
   - If the dealer's score is greater than the player's, the player loses.
   - If the player's score is greater than the dealer's, the player wins.
   - If both the player and dealer have the same score, it's a draw.

## Game Logic

- The game simulates the basic rules of Blackjack.
- Blackjack (an Ace and a 10-value card) is detected for both the player and the dealer.
- The player can decide to 'hit' (request another card) or 'stand' (pass).
- The dealer is forced to 'hit' until their score reaches at least 16.

## Considerations

- The script provides a simple text-based interface for playing Blackjack.
- It doesn't implement advanced features such as multiple rounds, split hands, or doubling down.

## License

This script is provided for educational and personal use. Please respect any licensing and usage restrictions associated with Python libraries and packages used in the script.

Enjoy playing Blackjack against the computer with this simple Python game!
