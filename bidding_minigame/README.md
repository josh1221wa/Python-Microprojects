# Auction Bid Winner Finder

This documentation explains a simple Python script that allows users to input bids from multiple bidders and find the winner with the highest bid.

## Purpose

The purpose of this script is to facilitate an auction-style bidding process where users can enter the names of bidders and their respective bids. The script then determines the winner with the highest bid.

## Dependencies

To run this script, you only need two dependencies:

- `os`: The `os` module is used to clear the console screen for better user interaction.
- `art`: The `art` module is used to display an ASCII art logo at the beginning of the program.

## Usage

1. The script starts by displaying an ASCII art logo using the `art` module.
2. Users are prompted to enter the names of bidders and their corresponding offers.
3. Bidders and their offers are stored in a dictionary, with the bidder's name as the key and the offer amount as the value.
4. Users are asked if there are any more bidders. If the answer is "no," the bidding process ends, and the script proceeds to find the winner.
5. The winner is determined by identifying the bidder with the highest offer using the `find_highest` function.
6. The script clears the screen using `os.system('cls')` for a cleaner user experience.
7. The winner's name and the highest offer are displayed.

## `find_highest` Function

The `find_highest` function is defined at the beginning of the script and is responsible for finding the bidder with the highest offer. It iterates through the dictionary of offers and returns the name and offer amount of the highest bidder.

## Considerations

- This script is a basic example of an auction-style bidding process and doesn't include advanced features like error handling or input validation.
- It assumes that all user inputs are valid (e.g., offer amounts are integers), which may not be the case in real-world applications.
- Users should be aware that the script uses a simple screen-clearing command (e.g., `os.system('cls')`), which is platform-specific. You may need to adjust it for compatibility with different operating systems.

## ASCII Art

The script uses the `art` module to display an ASCII art logo. The ASCII art can be customized, replaced, or removed according to your preferences.

## License

This script is provided for educational and personal use. Please respect any licensing and usage restrictions associated with the dependencies and ASCII art used in the script.

Enjoy finding the highest bidder with this simple Python tool!
