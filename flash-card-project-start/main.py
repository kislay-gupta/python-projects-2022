import random

import pandas

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
from pandas import *
import random

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")

    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def random_words():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer = window.after(3000, func=change)


def change():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_image)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    random_words()


window = Tk()
window.title("Flashy", )
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
flip_timer = window.after(3000, func=change)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=front_image, )

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40,))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, )
# Buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=random_words)
wrong_button.grid(row=1, column=0)

random_words()

window.mainloop()
