from tkinter import *


class Row:
    def __init__(self, text='', fg="#eee", bg="#333", autopack=False):
        self.row = Label(text=text, fg=fg, bg=bg)
        if autopack:
            self.pack()

    def config(self, text=''):
        self.row.config(text=text)

    def pack(self):
        self.row.pack()
