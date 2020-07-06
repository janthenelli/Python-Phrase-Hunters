# Create your Game class logic in here.
import random
import re
from phrase import Phrase
from phraseslist import RANDOM_PHRASES

class Game:
    def __init__(self, phrases):
        self.phrases = [Phrase(phrase) for phrase in phrases]
        self.selected_phrase = random.choice(self.phrases)
        self.lives = 5
        self.game_active = True


    def current_game_state(self, state):
        if state == 'start':
            self.game_active = True
        elif state == 'stop':
            self.game_active = False
        return self.game_active


    def get_player_input(self):
        no_input = True
        while no_input:
            answer = input("Please guess a letter:  ")
            if not re.search(r'[a-z]', answer, re.IGNORECASE):
                print(f"'{answer}' is not a valid guess, try again.\n")
            elif len(answer) != 1:
                print(f"'{answer}'' is too long. Please enter only one character per guess.\n")
            else:
                no_input = False
        return answer.lower()

    def check_win_loss(self):
        if self.lives == 0:
            self.current_game_state('stop')
            print('Oh no, you have run out of guesses!')      
        elif self.selected_phrase.solved:
            self.current_game_state('stop')
            print(self.selected_phrase.show_phrase())
            print('\nCongratulations! You guessed the phrase correctly!')

    def play_game(self):
        print("\nWelcome to Phrase Hunters!\n")
        while self.game_active:
            print(self.selected_phrase.show_phrase() + '\n')
            player_guess = self.get_player_input()
            print('\n')
            if player_guess not in self.selected_phrase.phrase:
                self.lives -= 1
                print("Oops, that's not in the phrase. You now have {} lives left out of 5\n".format(self.lives))
                self.check_win_loss()
            else:
                for letter in self.selected_phrase.characters_in_phrase:
                    letter.check_char_guessed(player_guess)
                self.selected_phrase.check_phrase_solved()
                self.check_win_loss()
        self.ask_to_replay()

    def ask_to_replay(self):
        while True:
            replay = input("\nWould you like to play again? Y/N:  ")
            if replay.lower() == 'y':
                self.current_game_state('start')
                break
            elif replay.lower() == 'n':
                self.current_game_state('stop')
                print("\nThanks for playing!\n")
                break
            else:
                print("Please enter either 'Y' or 'N'\n")
        if self.game_active:
            self.restart_game()

    def restart_game(self):
        new_game = Game(RANDOM_PHRASES)
        new_game.play_game()