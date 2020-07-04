class Pokemon:

    #TODO see if stats change with species or if you need to overwrite those as well
    def __init__(self, species, level, move1, move2, move3, move4):
        self.species = species
        self.level = level
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4

    def get_species(self):
        return self.species

    def get_level(self):
        return self.level

    def get_move1(self):
        return self.move1

    def get_move2(self):
        return self.move2

    def get_move3(self):
        return self.move3

    def get_move4(self):
        return self.move4