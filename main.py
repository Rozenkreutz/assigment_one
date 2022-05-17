import os
import random

from splash import FRAMES
from splash import splash

HINTS = {"pirate": "some lives in caraibean ",
         "sword": "whom live by it will die by it",
         "ship": "",
         "sail": "live by the wind",
         "rum": "give the mariner comfort",
         "swashbuckler": "",
         "mutiny": "rebellion aboard a ship",
         "booty": "reward",
         "buccaneer": "who takes the fast lane to wealth and success",
         "hijack": "to take control and lead",
         "plunder": "lottering"}

WORDS = ("swashbuckler", "mutiny", "pirate", "sword", "ship", "sail", "rum", "booty", "buccaneer", "hijack", "plunder")


class HangManGameState:

    def __init__(self, word):
        self.word = word
        self.solution = "-" * len(word)
        self.threshold = 10
        self.state = 0

    def attempt_left(self):
        return self.threshold - self.state

    def is_hung(self):
        return self.state >= self.threshold

    def is_winner(self):
        return self.solution == self.word

    def evaluate_letter(self, letter: str):
        indices = [i for i, c in enumerate(self.word) if c == letter]
        if len(indices) > 0:
            self.update_solution(indices, letter)
        else:
            self.state += 1

    def update_solution(self, indices: [], letter: str):
        for idx in indices:
            self.solution = self.solution[:idx] + letter + self.solution[idx + 1:]


def refresh(state):
    os.system('cls')
    for line in FRAMES[state.state]:
        print(line)

    if state.is_hung():
        print("Argh! The man is hung ! The word was : " + state.word)
    elif state.is_winner():
        print("Congratulation you won !")
    else:
        print(state.solution)


def start_game():
    splash()
    os.system('cls')
    gstate = HangManGameState(WORDS[random.randrange(0, len(WORDS) - 1)])
    return gstate


if __name__ == '__main__':

    game_state = start_game()

    while True:
        refresh(game_state)
        in_letter = input("Please input a letter ({} attempt(s) left) : ".format(game_state.attempt_left()))
        if in_letter in ['', None] or not in_letter.isalpha():
            continue
        game_state.evaluate_letter(in_letter[0].lower())

        refresh(game_state)

        if game_state.is_hung() or game_state.is_winner():
            again = input("Play Again [y,n] ?")
            if again.lower() == 'y':
                splash()
                os.system('cls')
                game_state = HangManGameState(WORDS[random.randrange(0, len(WORDS) - 1)])
            else:
                print("Au revoir !")
                break
