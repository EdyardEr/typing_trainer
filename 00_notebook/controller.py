from tkinter import *
from row_under import Row
from principal import Principal
from display import *

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

symbols = '1234567890-_=qwertyuiop[]asdfghjkl;\'zxcvbnm,./'
over_key = ['<Return>', '<space>']
words = iter(('w ', 'word_two ', 'word_three '))

princip = Principal(words)

for key in symbols:
    root.bind(key, princip.push_key)

for key in over_key:
    root.bind(key, princip.push_key)

root.mainloop()