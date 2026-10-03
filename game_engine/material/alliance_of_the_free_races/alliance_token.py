class AllianceToken:

    def __init__(self, race, effect):
        self.race = race
        self.effect = effect

    def __str__(self):
        return "Jeton " + self.get_race().get_name() + " : " + str(self.get_effect())

    def get_race(self):
        # Retourne la race à laquelle appartient le jeton.
        return self.race

    def get_effect(self):
        # Retourne l'effet du jeton.
        return self.effect