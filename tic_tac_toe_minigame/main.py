from tabulate import tabulate
import art
from time import sleep
import os

global board
board = [[" "]*3 for i in range(3)]


def print_board():
    print(tabulate(board, tablefmt="grid"))


def check_board(symbol):
    for i in board:
        if i.count(symbol) == 3:
            return True

    if [board[0][0], board[1][1], board[2][2]].count(symbol) == 3:
        return True

    if [board[x][0] for x in range(3)].count(symbol) == 3 or [board[x][1] for x in range(3)].count(symbol) == 3 or [board[x][2] for x in range(3)].count(symbol) == 3:
        return True

    return False


def no_space():
    for row in board:
        if " " in row:
            return False

    return True


print(art.logo)
sleep(5)

turn = "X"
while not no_space():
    print(f'It is {turn} turn')
    print_board()
    pos = input('Enter x-y position to be filled: ')
    x, y = int(pos.split()[0]), int(pos.split()[1])
    try:
        if board[x][y] != " ":
            os.system('cls')
            print("That space is already filled!\n")
        else:
            board[x][y] = turn
            if check_board(turn):
                os.system('cls')
                print(f"{turn} has won the game!")
                break
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            os.system('cls')
    except IndexError:
        os.system('cls')
        print("That's an invalid position!\n")

print(art.end)
