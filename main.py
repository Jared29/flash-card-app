from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)
lang_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

# Buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0)
right.grid(column=1, row=2)
wrong = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong.grid(column=0, row=2)


window.mainloop()
