class GetterWords:
    def __init__(self):
        self.words = iter('word_one', 'word_two', 'word_three')


    def get_word(self):
        next(self.words)