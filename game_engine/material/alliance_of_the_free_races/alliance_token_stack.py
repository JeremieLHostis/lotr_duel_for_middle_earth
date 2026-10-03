import random


class AllianceTokenStack:

    def __init__(self, race, tokens):
        # Crée une pile de trois jetons appartenant à la même race,
        # disposés dans un ordre aléatoire.
        self.race = race
        self.tokens = tokens
        random.shuffle(self.tokens)

    def __str__(self):
        s = "Pile des " + self.get_race().get_name() + " :\n"
        for token in self.get_tokens():
            s += str(token) + "\n"
        return s

    def get_race(self):
        # Retourne la race à laquelle appartient la pile.
        return self.race

    def get_tokens(self):
        # Retourne les jetons actuellement présents dans la pile.
        return self.tokens

    def reveal_top(self):
        # Révèle le premier jeton de la pile sans le retirer.
        return self.get_tokens()[0]

    def reveal_top_two(self):
        # Révèle les deux premiers jetons de la pile sans les retirer.
        return self.get_tokens()[:2]

    def take(self, token):
        # Retire de la pile le jeton choisi.
        self.get_tokens().remove(token)