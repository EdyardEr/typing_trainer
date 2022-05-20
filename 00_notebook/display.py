from tkinter import *


class Repeater:
    def __init__(self):
        self.main_text = ''
        self.main_row = self.create_row(self.main_text, autopack=True)
        self.first_row = self.create_row('first_row', autopack=True)
        self.second_row = self.create_row('second_row', autopack=True)
        self.third_row = self.create_row('third_row', autopack=True)

    def write_in_main_row(self, symb):
        self.main_text += symb
        self.main_row.config(text=self.main_text)

    def clear_main_row(self):
        self.main_text = ''
        self.main_row.config(text=self.main_text)

    def create_row(self, text='', fg="#eee", bg="#333", autopack=False):
        row = Label(text=text, fg=fg, bg=bg)
        if autopack:
            row.pack()
        return row

    def next_word(self, word):
        self.actual_row(word)

    def actual_row(self, word='', stage=0):
        print(word, stage)
        first = second = third = word
        if stage > 0:
            third = ''
        if stage > 1:
            second = ''

        self.first_row.config(text=first)
        self.second_row.config(text=second)
        self.third_row.config(text=third)



