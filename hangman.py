import customtkinter as ctk
import random

ctk.set_default_color_theme('dark-blue')

word_list = ['sun']

word = random.choice(word_list)
hidden_word = list(len(word) * '*')

root = ctk.CTk()
root.geometry('500x500')


def guess():
    letter = letter_input.get()
    index = word.find(letter)
    while index != -1:
        hidden_word[index] = letter
        buf = ''.join(hidden_word)
        hidden_word_extra.set(buf)
        index = word.find(letter, index + 1)





hidden_word_extra = ctk.StringVar()
hidden_word_extra.set(len(word) * '*')

hidden_word_view = ctk.CTkLabel(master=root, textvariable=hidden_word_extra, font=('Arial', 60))
hidden_word_view.pack()

letter_input = ctk.CTkEntry(master=root)
letter_input.pack()

button = ctk.CTkButton(master=root, text='Guess the letter', command=guess)
button.pack()





root.mainloop()