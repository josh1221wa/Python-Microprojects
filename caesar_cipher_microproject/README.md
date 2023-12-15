# Microproject - Caesar Cipher

The Caesar Cipher program is a simple implementation of the classic Caesar cipher encryption and decryption algorithm. It performs the following steps:

1. **Logo Display:**

   - Displays an ASCII art logo using the `art` library.

2. **Caesar Cipher Function:**

   - Defines a function `caesar_cipher` that takes the input text, shift value, and direction (encode or decode).
   - Iterates through each character in the input text.
   - Shifts each alphabetical character by the specified shift value based on the chosen direction (encode or decode).
   - Maintains non-alphabetic characters unchanged.
   - Prints the result.

3. **User Interaction Loop:**

   - Utilizes a `while` loop for continuous user interaction.
   - Asks the user to choose between encryption ('encode') or decryption ('decode').
   - Takes the message input from the user.
   - Takes the shift value for encryption or decryption.
   - Calls the `caesar_cipher` function with the user input.

4. **Continue or Exit:**
   - Asks the user if they want to continue with another operation.
   - Breaks out of the loop if the user chooses to exit.

The code is well-documented, and the Caesar Cipher algorithm provides a basic illustration of substitution cipher techniques.

For more details, refer to the code comments and instructions provided during the program execution.
