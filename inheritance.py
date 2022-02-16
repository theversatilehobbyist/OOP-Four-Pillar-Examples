class LeafType:
    def __init__(self, trainer):
        self.trainer = trainer

    def control_over_plants(self):
        print("The Pokemon helped the flower grow!")

    def fight(self):
        print("Your Pokemon attacked the other Pokemon, the opponent lost 50 XP")

    def defend(self):
        print("Your Pokemon defended itself successfully from the other Pokemon.")

    def sleep(self):
        print("After a long day of fighting, your Pokemon went to sleep")

leaftype1 = LeafType("Ash")
print("Regular LeafType Pokemon")
leaftype1.control_over_plants()
leaftype1.fight()
leaftype1.defend()
leaftype1.sleep()
print()
print("--------------------------------------------------------------------------------------------------------")
print()

class Bulbasaur(LeafType):
    def fight(self):
        print("Your Bulbasaur used its secret ability, Chlorophyll, to attack the other Pokemon, the opponent lost 75 XP")

    def defend(self):
        print("Your Bulbasaur whacked the opponent with its bulb and lashed with its vines")
bulbasaur1 = Bulbasaur("Ash")
print("Bulbasaur")
bulbasaur1.control_over_plants()
bulbasaur1.fight()
bulbasaur1.defend()
bulbasaur1.sleep()
