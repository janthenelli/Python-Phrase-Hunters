# Create your Game class logic in here.
import random
import re
from phrase import Phrase

class Game:
    def __init__(self, phrases):
        self.phrases = [Phrase(phrase) for phrase in phrases]
        self.selected_phrase = random.choice(self.phrases)
        self.lives = 5
        self.game_active = True


    def current_game_state(state):
        if state == 'start':
            self.game_active = True
        elif state == 'stop':
            self.game_active = False
        return self.game_active


    def get_player_input(self):
        while True:
            answer = input("Please guess a letter:  ")
            if not re.search(r'[a-z]', answer, re.IGNORECASE):
                print(f"{answer} is not a valid guess, try again.")
            elif len(answer) != 1:
                print(f"{answer} is too long. Please enter only one character per guess.")
        return answer.lower()

    def check_win_loss(self):
        if self.lives == 0:
            self.current_game_state('stop')
            print('Oh no, you have run out of guesses!')      
        elif self.selected_phrase.solved:
            self.current_game_state('stop')
            print('Congratulations! You guessed the phrase correctly!')


