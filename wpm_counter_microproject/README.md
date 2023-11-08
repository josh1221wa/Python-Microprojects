# Microproject - Words Per Minute (WPM) Counter

This documentation explains a Python application that measures the user's typing speed in words per minute (WPM). Users are provided with a random word, and they need to type it as quickly as possible to get an accurate WPM score.

## Purpose

The purpose of this application is to provide a simple WPM test for users. It displays a random word and measures how quickly the user can type it. The application then calculates the WPM score and updates it in real-time.

## Dependencies

- `customtkinter`: This module provides a custom extension of the `tkinter` library for GUI development.
- `random`: The `random` module is used to select random words from a text file.
- A data file named "data.txt" is used to store a list of words for the test.

## Usage

1. The application opens with the title "Words Per Minute Counter" and provides a "Start" button to begin the WPM test.
2. Users can click the "Start" button to start the test.
3. The application displays a countdown timer (60 seconds by default) and a random word to type.
4. Users need to type the displayed word as quickly as possible and press Enter.
5. The application calculates and displays the current WPM score based on the words typed and the time taken.
6. If the word is typed correctly, the user's score increases by 1.
7. The "Reset" button allows users to start a new test.
8. The application provides feedback on the test by displaying the WPM score.

## Game Logic

- The application selects random words from the "data.txt" file for the test.
- It measures how quickly the user can type the displayed word.
- If the word is typed correctly, the user's score increases by 1.
- The timer counts down, and the game ends when the timer reaches 0.

## Considerations

- The application provides a simple text-based typing test to measure typing speed in words per minute.
- Users can customize the countdown timer by changing the `COUNT` variable.
- The `data.txt` file can be updated with different words for the test.

## License

This application is provided for educational and personal use. Please respect any licensing and usage restrictions associated with the dependencies, data file, and custom extensions used in the application.

Enjoy testing your typing speed with this simple Python WPM Counter application!
