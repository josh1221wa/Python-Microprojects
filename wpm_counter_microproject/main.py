import customtkinter as ctk
from customtkinter import END
import random

COUNT = 60
SCORE = 0


def start_game():
    change_word()
    start_button.configure(state="disabled")
    word_entry.configure(state="normal")
    word_entry.focus_set()
    app.after(1000, countdown)


def countdown():
    global COUNT
    COUNT -= 1
    if COUNT == 10:
        countdown_label.configure(text_color='red')
    if COUNT == -1:
        word_entry.delete(0, END)
        word_label.configure(text="TIME UP")
        word_entry.configure(state="disabled")
        reset_button.configure(state="enabled")
        return
    countdown_label.configure(text="Countdown: " + str(COUNT))
    app.after(1000, countdown)


def change_word():
    global word
    word = random.choice(data)
    word_label.configure(text=word)


def check_word(*args):
    if entry_word.get() == word and COUNT == -1:
        increase_point()
        word_entry.configure(state="disabled")
    if entry_word.get() == word and COUNT != -1:
        increase_point()
        change_word()
        word_entry.delete(0, END)
    elif word.find(entry_word.get()) == -1:
        word_label.configure(text_color="red")
    elif word.find(entry_word.get()) == 0:
        word_label.configure(text_color="white")


def increase_point():
    global SCORE
    SCORE += 1
    score_label.configure(text="WPM: "+str(SCORE))


def reset_game():
    global COUNT, SCORE
    COUNT = 5
    SCORE = 0
    countdown_label.configure(text="Countdown: 60", text_color="white")
    word_label.configure(text="Press START to begin!")
    score_label.configure(text="WPM: 0")
    start_button.configure(state="enabled")
    reset_button.configure(state="disabled")


app = ctk.CTk()
app.geometry("350x430")
app.title("WPM Counter")

with open("data.txt", "r") as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i][:-1]


ctk.CTkLabel(app, text="Words Per Minute Counter", font=(
    "Times New Roman", 25, 'bold')).pack(pady=(20, 0))

countdown_label = ctk.CTkLabel(
    app, text="Countdown: 60", font=("Times New Roman", 20, "normal"))
countdown_label.pack(pady=(20, 0))

word_label = ctk.CTkLabel(app, text="Press START to begin!", font=(
    "Times New Roman", 18, "normal"))
word_label.pack(pady=20)

start_button = ctk.CTkButton(
    app, text="Start", command=start_game)
start_button.pack(pady=20)

entry_word = ctk.StringVar()
entry_word.trace("w", check_word)
word_entry = ctk.CTkEntry(app, textvariable=entry_word)
word_entry.pack(pady=20)

score_label = ctk.CTkLabel(app, text="WPM: 0", font=(
    "Times New Roman", 18, "normal"))
score_label.pack(pady=20)

reset_button = ctk.CTkButton(
    app, text="Reset", command=reset_game, state="disabled")
reset_button.pack(pady=20)

app.mainloop()
