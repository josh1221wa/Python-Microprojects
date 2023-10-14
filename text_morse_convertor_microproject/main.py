from data import text_to_code, code_to_text
import os
from art import art
import time

repeat = True

while repeat:
    print(art)
    ch = int(input("1. Text to Morse\n2. Morse to Text\nEnter Choice: "))
    if ch == 1:
        string = input("Enter string to convert: ").lower()
        for char in string:
            print(text_to_code[char], end=" ")
        print()

    elif ch == 2:
        morse = input("Enter morse code: ").split()
        for char in morse:
            print(code_to_text[char], end="")
        print()

    else:
        print("Given a wrong input, please try again.")
        time.sleep(5)
        os.system('cls')
        continue

    ch = input("Do you want to try another convertion? (Yes/No): ")
    if ch == 'Yes':
        os.system("cls")
    else:
        repeat = False
