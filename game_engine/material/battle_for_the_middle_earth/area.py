class Area:

    def __init__(self, name, id, units=0):
        # Crée une des sept zones de la terre du milieu.
        # L'id permet de créer les connexions sur le plateau via sa matrice d'adjacence (cf map.py)
        # L'occupation par troupes et forteresses est modélisée ainsi : l'int est positif si l'élement est à la communauté; négatif s'il est à Sauron
        self.name = name
        self.id = id
        self.units = units
        self.fortress = 0

    def __str__(self):
        s = "La zone " + self.name + " contient " + str(abs(self.units)) + " unités" + "."*(self.units==0) + " de"*(self.units!=0) + " la Communauté"*(self.units>0) + " Sauron"*(self.units<0) + "."*(self.fortress==0) + " et une forteresse de"*(self.fortress!=0) + " la Communauté."*(self.fortress==1)+ " Sauron."*(self.fortress==-1)
        return s

    def units_amount(self):
        return abs(self.units)

    def has_fellowship_units_in(self):
        return self.units > 0

    def has_sauron_units_in(self):
        return self.units < 0

    def has_fellowship_fortress_in(self):
        return self.fortress == 1

    def has_sauron_fortress_in(self):
        return self.fortress == -1

    def is_occupied_by_fellowship(self):
        return self.has_fellowship_fortress_in() or self.has_fellowship_units_in()

    def is_occupied_by_sauron(self):
        return self.has_sauron_fortress_in() or self.has_sauron_units_in()

    """ Les trois méthodes suivantes ne sont peut-être pas nécessaires """

    # def has_units_in(self):
    #     return self.units != 0

    # def has_fortress_in(self):
    #     return self.fortress != 0

    # def is_occupied(self):
    #     return self.has_fortress_in() or self.has_units_in()

    """ """

    def units_in(self,incoming_units):
        # Mets à jour le décompte d'unité si incoming_units unités entrent dans la zone
        # Si self.units est de signe contraire de incoming_units, un conflit est déclenché,
            # mais la méthode le résoud selon les règles automatiquement !
        # incoming_units > 0 : unités de la Communauté
        # incoming_units < 0 : unités de Sauron
        self.units += incoming_units

    def units_out(self,outcoming_units):
        # Mets à jour le décompte d'unité si incoming_units unités sortent de la zone, selon le même principe que move_units_in
        self.units -= outcoming_units

    def builds_fellowship_fortress(self):
        self.fortress = 1

    def builds_sauron_fortress(self):
        self.fortress = -1

    def destroy_fortress(self):
        self.fortress = 0