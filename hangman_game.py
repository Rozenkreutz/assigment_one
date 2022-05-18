HINTS = {"pirate": "can be found on any seas",
         "sword": "whom live by it will die by it",
         "ship": "a large seagoing vessel",
         "sail": "live by the wind",
         "rum": "give the mariner comfort",
         "swashbuckler": "is heroic, daring, and idealistic",
         "mutiny": "rebellion aboard a ship",
         "booty": "a reward",
         "buccaneer": "who takes the fast lane to wealth and success",
         "hijack": "to take control and lead",
         "plunder": "lottering"}

WORDS = ("swashbuckler", "mutiny", "pirate", "sword", "ship", "sail", "rum", "booty", "buccaneer", "hijack", "plunder")


# represent the  state of a hangman game
class HangManGame:

    def __init__(self, word):
        self.word = word
        self.solution = "-" * len(word)
        self.threshold = 10
        self.state = 0

    # get the current attempt number against the threshold
    def get_grade(self):
        return self.state / self.threshold

    # return whether to show the hint (after 8 attempt / 10)
    def is_display_hint(self):
        return self.state / self.threshold >= 0.8

    def attempt_left(self):
        return self.threshold - self.state

    def is_hung(self):
        return self.state >= self.threshold

    def is_winner(self):
        return self.solution == self.word

    # Evaluate user input against the quiz word
    def evaluate_letter(self, letter: str):

        indices = [i for i, c in enumerate(self.word) if c == letter]
        if len(indices) > 0:
            self.update_solution(indices, letter)
        else:
            self.state += 1

    # insert found letter at relevant indexes
    def update_solution(self, indices: [], letter: str):

        for idx in indices:
            self.solution = self.solution[:idx] + letter + self.solution[idx + 1:]
