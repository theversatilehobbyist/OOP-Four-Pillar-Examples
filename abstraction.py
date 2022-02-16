class Pokemon:
    def __init__(self, type, species, trainer):
        self.type = type
        self.species = species
        self.trainer = trainer

    def introduce(self):
        print("Hi! I'm", self.species, "!") #We only care about what it is saying, we don't care about how it is saying this

pokemon1 = Pokemon("Earth-type", "Bulbasaur", "Ash")
pokemon1.introduce()
