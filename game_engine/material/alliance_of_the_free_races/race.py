class Race:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.get_name()

    def get_name(self):
        # Retourne le nom de la race.
        return self.name