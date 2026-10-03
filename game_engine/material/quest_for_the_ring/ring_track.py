from game_engine.material.effect import Effect
from game_engine.material.quest_for_the_ring.ring_position import RingPosition


class RingTrack:

    def __init__(self):
        # Crée la piste de l'Anneau, de structure confondue pour les deux factions, avec ses effets spéciaux.
        self.effects_at_positions = {
            3: Effect("coin", 1),
            6: Effect("unit", 1),
            9: Effect("extra turn"),
            12: Effect("destroys fortress"),
            14: Effect("quest achieved")
        }
        self.positions = {
            "Frodo": RingPosition("Fellowship"),
            "Nazgul": RingPosition("Sauron")
        }
    
    def __str__(self):
        return str(self.get_frodo()) + "\n" + str(self.get_nazgul())
    
    def get_frodo(self):
        return self.positions["Frodo"]
    
    def get_frodo_position(self):
        # Retourne le nombre d'anneaux récoltés par la Communauté.
        return self.get_frodo().get_position()
    
    def get_nazgul(self):
        return self.positions["Nazgul"]
    
    def get_nazgul_position(self):
        # Retourne le nombre d'anneaux récoltés par Sauron.
        return self.get_nazgul().get_position()
    
    def effect_at(self, step):
        # Retourne, s'il y en a un, l'effet de la case numérotée step.
        return self.effects_at_positions.get(step)

    def effect_in_path(self, positions_crossed):
        for position in positions_crossed:
            effect = self.effect_at(position)
            if effect is not None:
                return effect

    def fellowship_gets_rings(self, rings):
        # Avance le pion de la Communauté de rings cases,
        # et retourne l'effet d'une des cases traversées s'il y a lieu.
        # La faction en bénéficiant devrait bien être la Communauté car les règles s'assureront de la bonne structure du tour !
        return self.effect_in_path(self.get_frodo().move(rings))
    
    def sauron_gets_rings(self, rings):
        # Avance le pion de Sauron de rings cases,
        # et retourne l'effet d'une des cases traversées s'il y a lieu.
        # La faction en bénéficiant devrait bien être Sauron car les règles s'assureront de la bonne structure du tour !
        return self.effect_in_path(self.get_nazgul().move(rings))


