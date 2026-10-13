from game_engine.material.battle_for_the_middle_earth.area import Area


class Map:

    def __init__(self):
        # Crée le plateau représentant la terre du milieu, avec toutes les adjacences entre les zones.
        # Les zones sont accessibles directement par leur nom.
        # Les zones de départ des deux camps sont directement instanciées avec leur unités de départ.
        self.areas = {
            "Lindon": Area("Lindon"),
            "Arnor": Area("Arnor", 2),
            "Rhovanion": Area("Rhovanion"),
            "Rohan": Area("Rohan"),
            "Enedwaith": Area("Enedwaith"),
            "Gondor": Area("Gondor"),
            "Mordor": Area("Mordor", -2)
        }

        self.adjacencies = {
            "Lindon": {"Arnor"},
            "Arnor": {"Lindon", "Rhovanion", "Enedwaith"},
            "Rhovanion": {"Arnor", "Rohan", "Enedwaith"},
            "Rohan": {"Rhovanion", "Enedwaith", "Gondor", "Mordor"},
            "Enedwaith": {"Arnor", "Rhovanion", "Rohan", "Gondor"},
            "Gondor": {"Rohan", "Enedwaith", "Mordor"},
            "Mordor": {"Rohan", "Gondor"}
        }

    def __str__(self):
        s = "Voici l'état courant de la Terre du Milieu :\n"
        for area in self.areas.values():
            s += str(area) + "\n"
        balance = self.occupation_balance()
        if balance > 0:
            s += "La Communauté mène de " + str(balance) + "."
        elif balance < 0:
            s += "Sauron mène de " + str(-balance) + "."
        else:
            s += "Les deux factions sont à égalité."
        return s

    def get_area(self, name):
        return self.areas[name]

    def adjacency(self, area_name):
        return self.adjacencies[area_name]

    def are_adjacent(self, area_1_name, area_2_name):
        return area_2_name in self.adjacency(area_1_name)

    def adjacent_areas(self, area_name):
        return list(self.adjacency(area_name))

    def see_adjacent_areas(self, area_name):
        for adjacent_area in self.adjacent_areas(area_name):
            print(self.get_area(adjacent_area))

    def put_units(self, recruited_units, area_name):
        # Place les unités dans la zone indiquée, éventuellement en déclenchant un conflit.
        # recruited_units > 0 : unités de la Communauté
        # recruited_units < 0 : unités de Sauron
        area = self.get_area(area_name)
        area.units_in(recruited_units)

    def kill_units(self, killed_units, area_name):
        # Tue les unités dans la zone indiquée, si c'est légal.
        # killed_units > 0 : meurtre par Sauron
        # killed_units < 0 : meurtre par la Communauté
        area = self.get_area(area_name)
        presence = area.units
        if (
            presence * killed_units >= 0
            and abs(presence) >= abs(killed_units)
        ):
            area.units_out(killed_units)
        else:
            raise ValueError(
                "Meurtre impossible : mauvais camp, "
                "ou pas assez d'unités à tuer"
            )

    def move_units(self, moving_units, area_1_name, area_2_name):
        # Déplace les unités (1 -> 2), si le déplacement est légal.
        area_1 = self.get_area(area_1_name)
        area_2 = self.get_area(area_2_name)
        presence = area_1.units
        if (
            presence * moving_units >= 0
            and abs(presence) >= abs(moving_units)
            and self.are_adjacent(area_1_name, area_2_name)
        ):
            area_1.units_out(moving_units)
            area_2.units_in(moving_units)
        else:
            raise ValueError(
                "Déplacement impossible : mauvais camp, "
                "pas assez d'unités à déplacer, "
                "ou zones non adjacentes")

    def fellowship_control(self):
        # Renvoie le nombre de zones occupées par la Communauté
        control = 0
        for area in self.areas.values():
            control += area.fellowship_occupies()
        return control

    def sauron_control(self):
        # Renvoie le nombre de zones occupées par Sauron
        control = 0
        for area in self.areas.values():
            control += area.sauron_occupies()
        return control

    def occupation_balance(self):
        # Positif : avantage de la Communauté
        # Négatif : avantage de Sauron
        # 0 : égalité
        return self.fellowship_control() - self.sauron_control()