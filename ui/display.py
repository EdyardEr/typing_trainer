from tkinter import *


class Window:
    def __init__(self, title='', size='300x250'):
        self._root = Tk()
        self._root.title(title)
        self._root.geometry(size)

    def start(self):
        self._root.mainloop()

    def get_root(self):
        return self._root


class String:
    def __init__(self, text='', fg='#eee', bg='#333', pack=True):
        self.row = Label(text=text, fg=fg, bg=bg)
        if pack:
            self.row.pack()

    def pack(self):
        self.row.pack()

    def hide(self):
        self.row.config(text='')