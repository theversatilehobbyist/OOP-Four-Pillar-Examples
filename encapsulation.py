class Bulbasaur:
    def __init__(self, trainer):
        self.trainer = trainer

    def __stats(self): #You wouldn't want to tell people your pets stats, so you keep it hidden or encapsulated!
        hp = 45
        attack = 49
        defense = 49
        speed = 45
        ability = "Overgrow"
        hidden_ability = "Chlororphyll"
        print(hp, attack, defense, speed, ability, hidden_ability, self.trainer)


bulbasaur1 = Bulbasaur("Ash")
bulbasaur1.__stats()
