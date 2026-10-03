class Effect:

    def __init__(self, name, quantity=None):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        if self.get_quantity() is None:
            return self.get_name()
        return self.get_name() + " : " + str(self.get_quantity())

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity