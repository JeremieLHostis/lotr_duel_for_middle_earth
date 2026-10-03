class RingPosition:

    def __init__(self, faction):
        self.faction = faction
        self.position = 0

    def __str__(self):
        s = "La Communauté"*(self.get_faction()=="Fellowship") + "Sauron"*(self.get_faction()=="Sauron")
        s += " a avancé de " + str(self.get_position()) + " cases sur sa piste de l'Anneau."
        return s

    def get_faction(self):
        return self.faction

    def get_position(self):
        return self.position

    def move_one_step(self):
        # Avance le pion concerné (Frodon ou le Nazgul selon la faction) d'une case. 
        # Si la 14ème case est atteinte, la quête est déjà terminée (Montagne du Destin atteinte ou Frodon rattrapé selon la faction)
        # donc la méthode ne fait rien.
        if self.get_position() < 14:
            self.position += 1
    
    def move(self, steps):
        # Avance le pion concerné de steps cases, ou jusqu'à accomplissement de la quête si cela en demande moins.
        # Retourne les cases traversées, dans l'ordre.
        positions_crossed = []
        for step in range(steps):
            if self.get_position() >= 14:
                break
            self.move_one_step()
            positions_crossed.append(self.get_position())
        return positions_crossed

if __name__ == "__main__":
    pos = RingPosition("Fellowship")
    print(pos)
    print(pos.move(2))
    print(pos)
    print(pos.move(1))
    print(pos)
    print(pos.move(4)) # (impossible, seulement là pour tester un cas)
    print(pos)
    print(pos.move(999)) # (impossible, seulement là pour tester un cas)
    print(pos)