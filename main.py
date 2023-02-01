import secrets
import string
import tkinter
from tkinter import *

# by l1nuvv

# tkinter window
window = Tk()
window.title("Password Generator by l1nuvv")
window.geometry('500x500')

Label(window, font=('bold', 20), text='Password Generator by l1nuvv').pack()

# constants

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
password_length = 12
alphabet = letters + digits + special_chars


# generator password
def password_generate():
    password = ''.join(secrets.choice(alphabet))
    label = Label(window, text=password, font=('bold', 20))
    label.place(x=190, y=50)


len1 = tkinter.IntVar()


def get_len():
    while True:
        password = ''
        for i in range(password_length):
            password += ''.join(secrets.choice(alphabet))
            label = Label(window, text=password, font=('Helvetica', 20))  # displaying password
            label.place(x=160, y=50)

        if (any(char in special_chars for char in password) and
                sum(char in digits for char in password) >= 2):
            break
def select_all():  # to select all text inside Text box
    password1.tag_add("sel", "1.0", "end")  # all text selected
    password1.tag_config("sel", background="green", foreground="red")


Button(window, text='Generate', font=("normal", 10), bg='pink', command=get_len).place(x=200, y=100)
window.mainloop()
