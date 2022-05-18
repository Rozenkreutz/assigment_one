import random

from graphic import *
from hangman_game import *


# refresh the screen with the supplied game state
def refresh(state):
    os.system('cls')

    for line in FRAMES[state.state]:
        print(line)

    if state.is_hung():
        print("Argh! The man is hung ! The word was : " + state.word + "\r")
    elif state.is_winner():
        print("Congratulation you won and save a man from an horrible death!\r")
    else:
        print(state.solution)
        if state.is_display_hint():
            print("Hint :" + HINTS[state.word])


# Initialise and return the game object
def start_game():
    splash()
    os.system('cls')
    gstate = HangManGame(WORDS[random.randrange(0, len(WORDS) - 1)])
    return gstate


# main routine to play the game
if __name__ == '__main__':

    game_state = start_game()

    while True:
        refresh(game_state)
        in_letter = input("Please attempt a letter ({} attempt(s) left) : ".format(game_state.attempt_left()))

        # ignore non-letter or blank
        if in_letter in ['', None] or not in_letter.isalpha():
            continue

        # Take the first letter and ignore the rest
        game_state.evaluate_letter(in_letter[0].lower())
        refresh(game_state)
        print("\n")
        if game_state.is_hung() or game_state.is_winner():
            again = input("Play again [y,n] ?")
            if again.lower() == 'y':
                game_state = start_game()
            else:
                print("Au revoir - Arrivederci - See you !")
                break
