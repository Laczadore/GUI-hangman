import customtkinter as ctk
import random

ctk.set_default_color_theme('dark-blue')

word_list = ['sun']


def guess():
    pass


word = random.choice(word_list)
hidden_word = list(len(word) * '*')

root = ctk.CTk()
root.geometry('500x500')

hidden_word_view = ctk.CTkLabel(master=root, text=hidden_word, font=('Arial', 60))
hidden_word_view.pack()

letter_input = ctk.CTkEntry(master=root)
letter_input.pack()

button = ctk.CTkButton(master=root, text='Guess the letter', command=lambda:guess())
button.pack()




root.mainloop()