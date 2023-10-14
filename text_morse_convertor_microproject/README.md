# MicroProject - Text Morse Convertor

This documentation provides an explanation of a Python script that allows users to convert text to Morse code and Morse code back to text using a command-line interface.

## Purpose

The purpose of this script is to provide a simple tool for converting text to Morse code and vice versa. Users can input a text string and receive the corresponding Morse code, or input Morse code and receive the decoded text.

## Dependencies

To run this script, you need the following dependencies:

- `data` module: This module contains functions `text_to_code` and `code_to_text` for converting between text and Morse code.
- `os`: The `os` module is used to clear the console screen for a cleaner user experience.
- `art`: The `art` module is used to display ASCII art, providing a visual element to the program.
- `time`: The `time` module is used for pausing the program briefly after an incorrect choice for better user interaction.

## Usage

1. The script begins by presenting an ASCII art title and a menu for the user to choose an action.
2. The user can choose between two options:
   - Option 1: Text to Morse
     - The user is prompted to enter a text string to convert to Morse code.
     - The script iterates through the input string, converting each character to its Morse code representation and displaying the results.
   - Option 2: Morse to Text
     - The user is prompted to enter Morse code, with individual Morse code symbols separated by spaces.
     - The script parses the Morse code, converts it to text, and displays the decoded text.
   - If the user chooses an incorrect option, they are prompted to try again after a 5-second pause.
3. After successful conversion or displaying results, the user is asked if they want to perform another conversion. Typing "Yes" clears the screen and allows the user to continue. Typing "No" exits the program.

## Considerations

- The script is designed to be a simple Morse code conversion tool for educational and entertainment purposes.
- It provides a basic command-line interface, and the functionality is limited to text-to-Morse and Morse-to-text conversion.
- The script assumes that input text contains only lowercase alphabetic characters, and Morse code input is space-separated.
- Users should be aware that the Morse code generated follows a basic Morse code representation and might not conform to specific Morse code standards or include special characters.

## ASCII Art

The script uses the `art` module to display ASCII art. The ASCII art used can be customized to your preference and replaced with other ASCII art or removed entirely.

## License

This script is provided for educational and personal use. Please respect any licensing and usage restrictions associated with the dependencies and ASCII art used in the script.

Enjoy Morse code conversion with this simple Python tool!
