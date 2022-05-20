from ui.display import String
from tkinter import *

class RepeaterGui:
    def __init__(self):
        self.main_str = String('главная строка')
        self.one_str = String('первая строка')
        self.two_str = String('вторая строка')
        self.three_str = String('третья строка')
        message = StringVar()
        self.test_str = Entry(textvariable=message)
        self.test_str.pack()
        self.test_str.place(relx=.5, rely=.1, anchor="c", height=100)

        def show_message():
            print(message.get())

        message_button = Button(text="start", command=show_message)
        message_button.place(relx=.5, rely=.5, anchor="c")