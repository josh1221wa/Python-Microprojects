# Minigame - Celebrity Follower Guesser

The Celebrity Follower Guesser is a simple number comparison game where the player needs to guess which of two celebrities has a higher number of followers. The game includes the following features:

1. **Logo Display:**

   - Displays an ASCII art logo using the `art` library.

2. **Game Data:**

   - Imports a list of game data containing information about various items, including their names, descriptions, countries, and follower counts.

3. **Function to Choose B:**

   - Defines a function `chooseB(A)` to randomly select item B while ensuring it is not equal to item A.

4. **Game Loop:**

   - Utilizes a `while` loop to keep the game running until the player loses.
   - Randomly selects item A and calls the `chooseB` function to get item B.
   - Displays information about both items (A and B) to the player.
   - Takes user input to guess which item has more followers (A or B).
   - Checks if the guess is correct, updates the score, and continues the game.
   - If the guess is incorrect, ends the game and displays the final score.

5. **User Interface:**
   - Clears the console screen using the `os` library for a clean display after each round.
   - Provides feedback to the player, indicating whether their guess was correct and displaying the current score.

The code is well-documented, and the game provides an entertaining experience for users to test their knowledge of follower counts.
