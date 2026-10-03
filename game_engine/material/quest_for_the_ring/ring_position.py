class RingPosition:

    def __init__(self, faction):
        self.faction = faction
        self.position = 0

    def get_faction(self):
        return self.faction

    def get_position(self):
        return self.position

    def move_one_step(self):
        if self.position < 14:
            self.position += 1

    def move(self, steps):
        for step in range (steps):
            self.move_one_step()