from tkinter import *


eng_low = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
eng_high = 'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?'
eng_num = '`1234567890-=~!@#$%^&*()_+'
rus_low = 'йцукенгшщзхъфывапролджэячсмитьбю.'
rus_high = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,'
rus_num = 'ё1234567890-=Ё!"№;%:?*()_+'
backspace = '<Backspace>'
space = '<Space>'


def get_keys():
    keys_lst = list(eng_low + eng_high + eng_num + rus_low + rus_high + rus_num)
    keys_lst.append(backspace)
    keys_lst.append(space)
    return set(keys_lst)


class RepeaterEvents:
    def __init__(self, root):
        self._root = root

    def bind(self, func):
        self._root.bind(sequence='<key>', func=func)
