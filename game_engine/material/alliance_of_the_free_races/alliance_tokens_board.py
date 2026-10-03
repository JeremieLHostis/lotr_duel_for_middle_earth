from game_engine.material.alliance_of_the_free_races.alliance_token import AllianceToken
from game_engine.material.alliance_of_the_free_races.alliance_token_stack import (
    AllianceTokenStack,
)
from game_engine.material.alliance_of_the_free_races.race import Race
from game_engine.material.effect import Effect


class AllianceTokensBoard:

    def __init__(self):
        # Crée les six races.
        self.elves = Race("Elfs")
        self.dwarfs = Race("Dwarfs")
        self.hobbits = Race("Hobbits")
        self.humans = Race("Humans")
        self.ents = Race("Ents")
        self.wizards = Race("Wizards")

        # Crée les trois jetons de chaque race.
        # Les effets seront complétés ultérieurement.
        """à coder: prise en compte de la condition en type de coup dans effect.py, puis modification des effets conditionnels ci-dessous en conséquence"""
        elven_1 = AllianceToken(self.elves, Effect("yellow card -> extra turn"))
        elven_2 = AllianceToken(self.elves, Effect("red card -> put units anywhere"))
        """ à coder : les ressources, pour faire de l'effet ci-dessous un ajout d'objet skill """
        elven_3 = AllianceToken(self.elves, Effect("any skill"))

        dwarf_1 = AllianceToken(self.dwarfs, Effect("landmark -> no additionnal cost"))
        dwarf_2 = AllianceToken(self.dwarfs, Effect("landmark -> extra turn"))
        dwarf_3 = AllianceToken(self.dwarfs, Effect("green card -> double map move"))

        hobbit_1 = AllianceToken(self.hobbits, Effect("eagles -> extra race"))
        hobbit_2 = AllianceToken(self.hobbits, Effect("blue card -> unit", 1))
        hobbit_3 = AllianceToken(self.hobbits, Effect("card through chain -> coin", 3))

        human_1 = AllianceToken(self.humans, Effect("yellow card -> ring step", 1))
        human_2 = AllianceToken(self.humans, Effect("red card -> addtionnal unit", 1))
        human_3 = AllianceToken(self.humans, Effect("discarded card -> double reward"))

        ent_1 = AllianceToken(self.ents, Effect("extra turn"))
        ent_2 = AllianceToken(self.ents, Effect("destroys fortress"))
        ent_3 = AllianceToken(self.ents, Effect("maneuver"))

        wizard_1 = AllianceToken(self.wizards, Effect("ring step", 2))
        wizard_2 = AllianceToken(self.wizards, Effect("unit", 2))
        wizard_3 = AllianceToken(self.wizards, Effect("take in discard"))

        # Crée une pile pour chaque race.
        self.stacks = {
            self.elves: AllianceTokenStack(
                self.elves, [elven_1, elven_2, elven_3]
            ),
            self.dwarfs: AllianceTokenStack(
                self.dwarfs, [dwarf_1, dwarf_2, dwarf_3]
            ),
            self.hobbits: AllianceTokenStack(
                self.hobbits, [hobbit_1, hobbit_2, hobbit_3]
            ),
            self.humans: AllianceTokenStack(
                self.humans, [human_1, human_2, human_3]
            ),
            self.wizards: AllianceTokenStack(
                self.wizards, [wizard_1, wizard_2, wizard_3]
            ),
            self.ents: AllianceTokenStack(
                self.ents, [ent_1, ent_2, ent_3]
            )
        }

    def __str__(self):
        s = "Voici l'état courant des jetons d'alliance :\n"
        for stack in self.get_stacks().values():
            s += str(stack) + "\n"
        return s

    def get_stacks(self):
        # Retourne les six piles de jetons.
        return self.stacks

    def get_stack(self, race):
        # Retourne la pile correspondant à une race.
        return self.get_stacks()[race]