import customtkinter as ctk
import random

ctk.set_default_color_theme('dark-blue')

word_list_easy = ['sun', 'dog', 'fish', 'chair', 'book', 'tree', 'sky', 'table', 'floor', 'wind']

word_list_medium = ['remote', 'computer', 'elephant', 'bicycle', 'keyboard', 'rainbow', 'sandwich', 'umbrella', 'scissors', 'backpack']

word_list_hard = ['encyclopedia', 'relationship', 'photography', 'communication', 'organization', 'independence', 'architecture', 'establishment', 'university', 'responsibility']

guessed_letters = []

word = random.choice(word_list_easy)
hidden_word = list(len(word) * '*')

root = ctk.CTk()
root.geometry('500x500')

#define guess function
def guess():

    global notification
    global hidden_word
    global guessed_letters
    global counter


    
    
    letter = input_var.get().lower()

    
    
    if not letter:
        notification.set('Please enter a letter')
        return
    
    elif len(letter) != 1:
        notification.set('guess only 1 letter. Not more, not less')
        return


    elif letter in guessed_letters:
        notification.set('you have already guessed this letter')

    elif not letter .isalpha():
        notification.set('type in a letter, not number or anything else')

    elif letter not in word:
        notification.set('That is not right guess')
        guessed_letters.append(letter)
        counter.set(counter.get() + 1)
    if counter.get() == 6:
        guess_button.configure(state='disabled')
        notification.set(f'You lost! Password was {word.upper()} ')
    
    else:
        index = word.find(letter)
        while index != -1:
            hidden_word[index] = letter
            buf = ''.join(hidden_word)
            hidden_word_extra.set(buf)
            index = word.find(letter, index + 1)

            if buf == word:
                notification.set('YOU WON! Congratulations')
                input_var.set('')
                guess_button.configure(state='disabled')
                return

    
        
    input_var.set('')


    guessed_letters_view.configure(text=f'Guessed Letters: {", ".join(guessed_letters)}', font=('Arial', 20))

#define restart function
def restart():
    global notification
    global hidden_word
    global guessed_letters
    global counter
    global word
    
    if radiobutton_value.get() == 0:
        notification.set('Choose the difficulty for your next run')
        return
    
    if radiobutton_value.get() == 1:
        word = random.choice(word_list_easy)
    elif radiobutton_value.get() == 2:
        word = random.choice(word_list_medium)
    elif radiobutton_value.get() == 3:
        word = random.choice(word_list_hard)
    hidden_word = list(len(word) * '*')
    hidden_word_extra.set('*' * len(word))
    guessed_letters = []
    counter.set(0)
    notification.set('New Game started. Good Luck!')
    guess_button.configure(state='normal')



#create hidden password variable
hidden_word_extra = ctk.StringVar()
hidden_word_extra.set(len(word) * '*')

#display hidden password in a label
hidden_word_view = ctk.CTkLabel(master=root, textvariable=hidden_word_extra, font=('Arial', 60))
hidden_word_view.pack()

#create input so user can guess letters
input_var = ctk.StringVar()
letter_input = ctk.CTkEntry(master=root, textvariable=input_var)
letter_input.pack()

#create notification label so we can communicate with user
notification = ctk.StringVar()
notification_view = ctk.CTkLabel(master=root, textvariable=notification)
notification_view.pack()

#create counter variable
counter = ctk.IntVar()

#display counter in a label
counter_view = ctk.CTkLabel(master=root, text='COUNTER', textvariable=counter)
counter_view.pack()

guessed_letters_var = ctk.StringVar()
guessed_letters_view = ctk.CTkLabel(master=root, text='Guessed Letters: ', font=('Arial', 20))
guessed_letters_view.pack()

#create button
guess_button = ctk.CTkButton(master=root, text='Guess the letter', command=guess)
guess_button.pack()

restart_button = ctk.CTkButton(master=root, text='Restart the game', command=restart)
restart_button.pack(padx=10, pady=10)


#allowing user to choose dificulty
radiobutton_value = ctk.IntVar(value=0)

choose_difficulty = ctk.CTkLabel(master=root, text='Choose Difficulty. To apply it - click the restart button')
choose_difficulty.pack(pady=5)

radiobutton_easy = ctk.CTkRadioButton(master=root, text='easy', variable=radiobutton_value, value=1)
radiobutton_medium = ctk.CTkRadioButton(master=root, text='medium', variable=radiobutton_value, value=2)
radiobutton_hard = ctk.CTkRadioButton(master=root, text='hard', variable=radiobutton_value, value=3)

radiobutton_easy.pack(pady=5)
radiobutton_medium.pack(pady=5)
radiobutton_hard.pack(pady=5)





root.mainloop()