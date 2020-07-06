# Create your Character class logic in here.

class Character:
    def __init__(self, char):
        self.original = char
        self.was_guessed = False


    def char_was_guessed(guess):
        if guess == self.original:
            self.was_guessed = True
        return self.was_guessed


    def show_char(self):
        if self.was_guessed or self.original == ' ':
            return str(self)
        else:
            return '_'
