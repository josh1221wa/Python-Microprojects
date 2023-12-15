# Microproject - Flash Cards

Flashy is a vocabulary flashcard app designed to help users learn and practice French words in an interactive and engaging manner.

## Description

Flashy utilizes a simple Tkinter-based interface to present users with French words on a flashcard. The app allows users to flip the card, revealing the English translation, and provides buttons to indicate whether the user knows the word or not. The app tracks the words to be learned and saves progress.

## Introduction

Flashy is built using Python and relies on Tkinter for the graphical user interface. It reads French words from a CSV file, allowing users to learn from a pre-defined set of words. The application provides an interactive and visual way to improve French vocabulary.

## Program Flow

1. The app starts by attempting to read a CSV file containing words to learn. If the file is not found, it defaults to using a pre-defined set of French words.

2. The main window displays a flashcard with a French word.

3. After a delay, the app flips the card to reveal the English translation.

4. Users can click the "Right" button if they know the word or the "Wrong" button to skip it.

5. The app removes known words from the list to focus on the ones that need learning.

6. The process repeats with a new word, allowing users to iteratively learn and reinforce vocabulary.

## Dependencies

Flashy relies on the following dependencies:

- **Python**: The programming language used to build the application.
- **Tkinter**: The GUI toolkit for building the graphical user interface.
- **pandas**: A library for data manipulation and analysis.
  
Ensure that Python and the required dependencies are installed before running the application.

## Conclusion

Flashy provides an effective and visually engaging way to learn and practice French vocabulary. With its simple design and interactive features, it offers an enjoyable learning experience. Feel free to contribute to the project or report any issues.

Happy learning! 🇫🇷✨
