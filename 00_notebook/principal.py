from display import *
from get_word import *


class Principal(Repeater, GetterWords):
    def __init__(self, words):
        super().__init__()
        self.words = words
        self.next_word()

    def push_key(self, event):
        print(f'event {event.keysym}')
        print(event)
        actual_symb = self.take_symb()
        if event.char == actual_symb:
            self.write_in_main_row(actual_symb)
            self.correct()
        else:
            self.clear_main_row()
            self.incorrect()

    def take_symb(self):
        return self.word[self.ind] if self.word else False

    def correct(self):
        print('correct')
        if self.ind == self.len_word - 1:
            print('finish_word')
            self.finish_word()
        else:
            self.ind += 1

    def incorrect(self):
        print('incorrect')
        self.ind = 0
        self.repetitions = 0
        self.actual_row(self.word, self.repetitions)

    def finish_word(self):
        self.clear_main_row()
        if self.repetitions >= 2:
            self.finish_set()
        else:
            self.repetitions += 1
            self.ind = 0
            self.actual_row(self.word, self.repetitions)

    def finish_set(self):
        print('finish_set')
        self.next_word()

    def next_word(self):
        self.word = next(self.words)
        self.len_word = len(self.word)
        self.ind = 0
        self.repetitions = 0
        super().next_word(self.word)