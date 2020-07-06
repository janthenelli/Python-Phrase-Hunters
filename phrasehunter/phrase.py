# Create your Phrase class logic here.
import re

from character import Character

class Phrase:
    def __init__(self, phrase):
        self.solved = False
        self.phrase = phrase
        self.characters_in_phrase = []
        for letter in phrase:
            self.characters_in_phrase.append(Character(letter))

    def check_phrase_solved(self):
        characters_guessed = []
        for letter in self.characters_in_phrase:
            if letter != ' ':
                characters_guessed.append(letter.was_guessed)
        if all(characters_guessed):
            self.solved = True
        else:
            self.solved = False
        return self.solved
        
    def show_phrase(self):
        phrase_format = ''
        for letter in self.characters_in_phrase:
            phrase_format += letter.show_char() + ' '
        return phrase_format

